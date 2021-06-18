from panel import databaseInstance as Db


class PageModel(Db.Model):
    __tablename__ = 'page'

    id = Db.Column(Db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    title = Db.Column(Db.Text(70), unique=True, nullable=False)
    metatitle = Db.Column(Db.Text(70))
    metadescription = Db.Column(Db.Text(120))
    body = Db.Column(Db.Text())
    created = Db.Column(Db.TIMESTAMP)
    updated = Db.Column(Db.TIMESTAMP)

    def __repr__(self):
        return '%r' % (self.title)
