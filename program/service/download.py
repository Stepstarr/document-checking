# -*- coding: utf-8 -*-
# @Time    : 2024/4/19 9:49
# @Author  : Stepstar
# @FileName: download.py
# @Software: PyCharm
from flask import Blueprint, send_from_directory, current_app
import os
download_bp = Blueprint('download_bp', __name__)
from flask import Blueprint
import os

download_bp = Blueprint('download_bp', __name__)

from flask import Flask, request, send_file, abort

@download_bp.route('/download')
def download_file():

    filepath = request.args.get('downloadpath', None)

    if not filepath:
        return "No file path provided.", 400

    # 安全检查：确保文件路径在预定的安全边界内
    # 例如，确保文件路径是一个绝对路径，且位于某个特定的文件夹内
    #allowed_path = '/your/allowed/directory'  # 修改为你允许访问的目录
    #absolute_path = os.path.abspath(filepath)

   # if not absolute_path.startswith(allowed_path):
    #    return abort(403)  # 如果文件路径不在允许的目录内，则拒绝访问

    # 检查文件是否存在
    if not os.path.exists(filepath ):
        return "File not found.", 404

    try:
        # 直接发送文件
        return send_file(filepath , as_attachment=True)
    except Exception as e:
        return str(e), 500

