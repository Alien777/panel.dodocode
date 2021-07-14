from datetime import datetime

from panel import databaseInstance as Db
from panel.model.PageModel import PageModel


class RedirectModel(Db.Model):
    __tablename__ = 'redirect'

    id = Db.Column(Db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    page_id = Db.Column(Db.Integer, Db.ForeignKey('page.id'))
    page = Db.relationship(PageModel)
    path = Db.Column(Db.String(300))
    changed = Db.Column(Db.DateTime, default=datetime.now)

    def findPageIdBy(path):
        return Db.session.query(RedirectModel.page_id).filter(RedirectModel.path == path).scalar()

    def __repr__(self):
        return '%r' % (self.path)
