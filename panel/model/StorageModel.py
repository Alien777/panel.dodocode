from panel import databaseInstance as Db


class StorageModel(Db.Model):
    __tablename__ = 'storage'

    id = Db.Column(Db.Integer, primary_key=True)
    name = Db.Column(Db.Unicode(64))
    path = Db.Column(Db.Unicode(128))
    type = Db.Column(Db.Unicode(50))
    created = Db.Column(Db.TIMESTAMP)
