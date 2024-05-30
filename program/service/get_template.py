# service/upload_service.py
from flask import Blueprint, request, current_app, jsonify
from werkzeug.utils import secure_filename
import os
import shutil
from os.path import splitext
import json


gettemplate_bp = Blueprint('gettemplate_bp', __name__)

@gettemplate_bp.route('/get-template', methods=['POST'])
def get_template():
    '''
    从前端接收模板文件，存储在/static文件夹中，采用模板解析方法将模板具体信息存储在json文件中，存储路径为/templats，#TODO:模板解析
    '''
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    base_filename, extension = splitext(file.filename)
    save_path = os.path.join(current_app.root_path, 'static',file.filename)
    backup_path = os.path.join(current_app.root_path, 'templates', base_filename+'.json')

    # file.save(save_path)
    # shutil.copy(save_path, backup_path)  # 使用shutil来复制文件
    print(backup_path)
    with open(backup_path, 'r', encoding='utf-8') as json_file:
        file_data = json.load(json_file)
    
    
    return jsonify({'filename':base_filename,'filedata':file_data}),200