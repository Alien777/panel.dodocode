# main.py
from flask import Blueprint, send_file

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return "Hop"


@main.route('/static/<id>')
def return_files_tut(id):
    try:
        return send_file('/home/adam/Desktop/p/msrol/files/' + id, attachment_filename='python.jpg')
    except Exception as e:
        return str(e)
