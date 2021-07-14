# main.py
import json

from flask import Blueprint, send_file
import json
from panel.model.PageModel import PageModel
from panel.model.RedirectModel import RedirectModel

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


@main.route('/api/blog/<path>')
def return_files_tut2(path):
    result = PageModel.getPageBy(RedirectModel.findPageIdBy(path))

    print(result.__dict__)
    print(json.dumps(result.__dict__))

    return 'aaa'
