from flask_login import UserMixin

from panel import databaseInstance as Db


class UserModel(UserMixin, Db.Model):
    __tablename__ = 'user'

    id = Db.Column(Db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    name = Db.Column(Db.String(50))
    email = Db.Column(Db.String(80), unique=True, nullable=False)
    password = Db.Column(Db.String(120), nullable=False)

    def __repr__(self):
        return '%r' % (self.name)
