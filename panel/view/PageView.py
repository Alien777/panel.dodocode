from datetime import datetime, timezone

from flask import url_for
from flask_admin.contrib.sqla import ModelView
from flask_ckeditor import CKEditorField
from flask_login import current_user
from werkzeug.utils import redirect

from panel import panelAdminInstance as Pa, databaseInstance as Db
from panel.model.PageModel import PageModel


class PageView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

    column_searchable_list = ['title']
    column_list = ['title', 'created', 'updated']
    column_filters = ['created', 'updated']
    column_editable_list = ['created', 'updated']
    form_create_rules = ['title', 'metatitle', 'metadescription', 'body']
    form_edit_rules = ['created', 'updated', 'title', 'metatitle', 'metadescription', 'body']
    form_overrides = dict(body=CKEditorField)

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.created = datetime.now(timezone.utc)
        else:
            model.updated = datetime.now(timezone.utc)

    def on_form_prefill(self, form, id):
        form.created.render_kw = {'readonly': True}
        form.updated.render_kw = {'readonly': True}

    create_template = 'page/edit.html'
    edit_template = 'page/edit.html'


Pa.add_view(PageView(PageModel, Db.session, "Strony"))
