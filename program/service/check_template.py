# service/upload_service.py
from flask import Blueprint, request, current_app, jsonify
from werkzeug.utils import secure_filename
import os
import shutil
from os.path import splitext
import json

check_template_bp = Blueprint('check_template_bp', __name__)

@check_template_bp.route('/check-template', methods=['GET'])
def check_template():
    '''
    根据模板文件名返回对应的模板名和模板数据
    '''
    filename = request.args.get('filename')
    if not filename:
        return "No file name provided", 400
    save_path = os.path.join(current_app.root_path, 'templates',filename+'.json')
    with open(save_path, 'r', encoding='utf-8') as json_file:
        file_data = json.load(json_file)
    
    return jsonify({'filename':filename,'filedata':file_data}),200