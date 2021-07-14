# init.py

from flask import Flask, redirect
from flask_admin import Admin, AdminIndexView, expose
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

databaseInstance = SQLAlchemy()
panelAdminInstance = Admin(template_mode='bootstrap4')
ckeditor = CKEditor()


class DashboardView(AdminIndexView):

    def is_visible(self):
        # This view won't appear in the menu structure
        return False

    @expose('/')
    def index(self):
        return redirect("/admin/pagemodel")


def create_app():
    global panelAdminInstance
    global ckeditor
    global databaseInstance
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/dodocode"
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['CKEDITOR_ENABLE_CODESNIPPET'] = True
    app.config['CKEDITOR_SERVE_LOCAL'] = False
    app.config['CKEDITOR_PKG_TYPE'] = 'full-all'
    app.config['CKEDITOR_CODE_THEME'] = 'docco'
    databaseInstance.init_app(app)
    ckeditor.init_app(app)

    panelAdminInstance.init_app(app, index_view=DashboardView())

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from panel.model.UserModel import UserModel

    from panel.view.PageView import PageView
    from panel.view.RedirectView import RedirectView
    from panel.view.StorageView import StorageView
    from panel.view.AdminView import LogoutMenuLink
    from panel.view.AdminView import GoToHome

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return UserModel.query.get(int(user_id))

    # blueprint for non-auth parts of app
    from .Endpoints import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .AuthEndpoint import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
