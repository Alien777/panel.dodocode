from flask_admin.menu import MenuLink
from flask_login import current_user

from panel import panelAdminInstance as Pa


class LogoutMenuLink(MenuLink):
    def is_accessible(self):
        return current_user.is_authenticated


class GoToHome(MenuLink):
    def is_accessible(self):
        return current_user.is_authenticated


Pa.add_link(GoToHome(name='Wróć', category='', url="/"))
Pa.add_link(LogoutMenuLink(name='Logout', category='', url="/logout"))
