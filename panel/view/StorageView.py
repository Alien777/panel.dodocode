import os
import random
import magic
from flask import url_for, redirect
from flask_admin import form
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from markupsafe import Markup
from datetime import datetime, timezone

from panel import panelAdminInstance as Pa, databaseInstance as Db
from panel.model.StorageModel import StorageModel


def _list_thumbnail(view, context, model, name):
    if not model.path:
        return ''

    url = url_for('static', filename=os.path.join(model.path))

    if 'image' in model.type:
        return Markup(
            '<img id="%s" src="%s" width="100"> '
            '<button onclick="CopyToClipboard(\'%s\');return false;">Kopiuj url</a>' % (
                model.path, url, model.path))

    if 'audio' in model.type:
        return Markup(
            '<audio controls="controls"><source id="%s" src="%s" type="%s" /></audio>'
            '<button onclick="CopyToClipboard(\'%s\');return false;">Kopiuj url</a>' % (
                model.path, url, model.type, model.path))

    if 'video' in model.type:
        return Markup(
            '<video controls="controls"><source  id="%s" src="%s" width="320" height="240" type="%s" /></video>'
            '<button onclick="CopyToClipboard(\'%s\');return false;">Kopiuj url</a>' % (
                model.path, url, model.type, model.path))


def _change_path_data(form):
    try:
        storage_file = form.file.data

        if storage_file is not None:
            path = '%s.%s' % (random.getrandbits(128), storage_file.filename.split('.')[-1])
            storage_file.save(
                os.path.join("/home/adam/Desktop/p/msrol/files/", path)
            )
            form.path.data = path
            form.name.data = form.name.data or storage_file.filename

            del form.file

    except Exception as ex:
        pass

    return form


class StorageView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

    column_formatters = {
        'path': _list_thumbnail
    }
    column_list = ('name', 'path', 'type', 'created')
    form_excluded_columns = ('created', 'type')
    form_extra_fields = {
        'file': form.FileUploadField('file')
    }
    form_edit_rules = ['name', 'file', 'title', 'metatitle', 'metadescription', 'body']
    can_edit = False

    def create_form(self, obj=None):
        return _change_path_data(
            super(StorageView, self).create_form(obj)
        )

    def on_model_delete(self, model):
        os.remove(os.path.join("/home/adam/Desktop/p/msrol/files/", model.path))

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.created = datetime.now(timezone.utc)
            model.type = magic.from_file(os.path.join("/home/adam/Desktop/p/msrol/files/", form.path.data), mime=True)

    list_template = 'page/list.html'


Pa.add_view(StorageView(StorageModel, Db.session, "Pliki"))
