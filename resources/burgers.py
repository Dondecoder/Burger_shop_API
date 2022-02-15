from flask_restful import Resource, reqparse
from models.burgers import BurgerModel


class Burger(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', 
    required = True,
    type = float,
    help = "Please enter the burger price. This field is mandatory")
    parser.add_argument('type',
    required = False,
    choices = ['turkey', 'beef', 'veggie', 'black bean', 'chicken'],    
    help = "Please enter the burger type. This field is mandatory")

    
    def get(self, name):
        burger = BurgerModel.find_by_name(name)
        if burger:
            return burger.json()
        return {'message': 'This burger item was not found'}, 404

    def post(self, name):
        if BurgerModel.find_by_name(name):
            return {'message': 'This burger item is already on the list'}
        else:
            data = Burger.parser.parse_args()
            burger = BurgerModel(name,data['price'], data['type'])
            try:
                burger.save_to_db()
            except:
                return {'message': 'An error occured inserting the item'}, 500
            return burger.json(), 201

    def put(self,name):
        data = Burger.parser.parse_args()
        burger = BurgerModel.find_by_name(name)
        if burger is None:
            try:
                burger = BurgerModel(name, **data)
            except:
                return {"message": "An error occured inserting the item"}, 500
        else:
            try:
                burger.price = data['price']
                burger.type = data['type']
                
            except:
                {"message": "An error occured updating the item"}, 500

        burger.save_to_db()

        return burger.json()
    
    def delete(self, name):
        burger = BurgerModel.find_by_name(name)
        if burger:
            burger.delete_from_db()
        return {'message': 'the burger has been deleted'}

class Allburgers(Resource):
    def get(self):
        return {'burgers': [burger.json() for burger in BurgerModel.query.all()]}