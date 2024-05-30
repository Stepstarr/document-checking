# service/upload_service.py
from flask import Blueprint, request, current_app, jsonify
from werkzeug.utils import secure_filename
import os
import shutil
from os.path import splitext

get_templates_bp = Blueprint('get_templates_bp', __name__)

@get_templates_bp.route('/get-templates', methods=['GET'])
def get_templates():
    '''
    返回文件夹中保存的所有模板的文件名
    '''
    save_path = os.path.join(current_app.root_path, 'templates')
    files = os.listdir(save_path)
    json_files = [splitext(file)[0] for file in files if file.endswith('.json')]
    return jsonify({'filenames':json_files}),200