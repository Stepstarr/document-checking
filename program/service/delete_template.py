# service/upload_service.py
from flask import Blueprint, request, current_app, jsonify
from werkzeug.utils import secure_filename
import os
import shutil
from os.path import splitext


delete_template_bp = Blueprint('delete_template_bp', __name__)

@delete_template_bp.route('/delete-template', methods=['POST'])
def delete_template():
    '''
    接收前端传来的模板文件名，删除/templates路径的对应模板文件
    '''
    data = request.json
    filename = data.get('fileName')

    if not filename:
        return jsonify({'error': 'File name is required'}), 400
    
    save_path = os.path.join(current_app.root_path, 'templates', filename+'.json')
    if not os.path.exists(save_path):
        return jsonify({'error': 'File not found'}), 404

    try:
        os.remove(save_path)
        return jsonify({'message': 'File deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    