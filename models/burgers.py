from db import db

class BurgerModel(db.Model):
    __tablename__ = 'burgers'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40))
    price = db.Column(db.Float())
    type = db.Column(db.String(40))   
        
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

    def json(self):
        return {"name": self.name, "price": self.price, "type": self.type}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    