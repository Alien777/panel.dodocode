from flask import url_for
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from werkzeug.utils import redirect

from panel import panelAdminInstance as Pa, databaseInstance as Db
from panel.model.RedirectModel import RedirectModel


class RedirectView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))

    column_list = ['page', 'path']


Pa.add_view(RedirectView(RedirectModel, Db.session, "Redirecty"))
