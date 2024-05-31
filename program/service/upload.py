# service/upload_service.py
from flask import Blueprint, request, current_app, jsonify
from werkzeug.utils import secure_filename
import os
import shutil
from os.path import splitext


upload_bp = Blueprint('upload_bp', __name__)

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    '''
    考虑到文件需要经历 检测 - 修改（or批注）两个阶段，如果在同一个文件上操作可能会存在错误，所以上传后将其存储在了两个位置
    1.filename.docx存入static
    2.filename+_addcomment存入static
    #TODO: 文件名的安全性，以及这里直接存filename,如果用户上传两个一样的filename的处理（待学习其他系统的文件存储处理方法）
    :return: 上传的文件保存路径
    '''
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    base_filename, extension = splitext(file.filename)
    save_path = os.path.join(current_app.root_path, 'static',file.filename)
    backup_path = os.path.join(current_app.root_path, 'static', base_filename+'_addcomment'+'.docx')

    file.save(save_path)
    shutil.copy(save_path, backup_path)  # 使用shutil来复制文件
    return jsonify({'filepath':save_path,'addpath':backup_path}),200
