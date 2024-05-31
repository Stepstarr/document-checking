# service/upload_service.py
from flask import Blueprint, request, current_app, jsonify
from werkzeug.utils import secure_filename
import os
import shutil
from os.path import splitext
import json

save_template_bp = Blueprint('save_template_bp', __name__)

@save_template_bp.route('/save-template', methods=['POST'])
def save_template():
    '''
    接收前端的文件名和模板数据，将其存储在/templates文件夹，返回存储的文件名
    '''
    data = request.json
    filename = data.get('fileName')
    jsondata = data.get('jsonData')
    if not filename or not jsondata:
        return jsonify({'error': 'File name and JSON data are required'}), 400
    
    try:
        save_path = os.path.join(current_app.root_path, 'templates', filename+'.json')
        with open(save_path, 'w', encoding="utf-8") as json_file:
            json.dump(jsondata, json_file, ensure_ascii=False, indent=4)
        return jsonify({'filename': filename}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    