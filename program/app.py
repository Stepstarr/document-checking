from flask import Flask, Response, send_from_directory
from algorithm.baseclass import BaseClass
import win32com.client as win32
import time
import pythoncom
from flask_cors import CORS

from format_config import reference_format
from flask import Flask
from service.upload import upload_bp
from service.download import download_bp
from service.check_docx import check_bp
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)
app.register_blueprint(upload_bp)
app.register_blueprint(download_bp)
app.register_blueprint(check_bp)

@app.route('/')
def helloworld():

    return 'helloworld'


if __name__ == '__main__':
    app.run(debug=True)
