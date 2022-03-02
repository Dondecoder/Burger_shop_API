from flask import Flask,app
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from authentication import authenticate,identity

burgers = []

app = Flask(__name__)
app.secret_key = 'Dondecoder'
api = Api(app)


jwt = JWT(app,authenticate, identity)


class Burger(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', 
    required = True,
    type = float,
    help = "Please enter the burger price. This field is mandatory")
    parser.add_argument('type',
    required = False,
    choices = ['turkey', 'beef', 'veggie', 'black bean'],    
    help = "Please enter the burger type. This field is mandatory")

    @jwt_required()
    def get(self, name):
        burger = next(filter(lambda x: x['name']== f"{name} burger", burgers), None)
        return {'burger':burger}

    def post(self, name):
        if next(filter(lambda x: x['name']== f"{name} burger", burgers), None): 
            return {'message': 'This burger item is already on the list'}
        else:
            data = Burger.parser.parse_args()
            burger = {'name':f"{name} burger", 'price':data['price'], 'type': f"{data['type']} burger"}
            burgers.append(burger)
            return burgers

    def put(self,name):
        data = Burger.parser.parse_args()
        burger = next(filter(lambda x: x['name']== f"{name} burger", burgers), None)
        if burger is None:
            burger = {'name':f"{name} burger", 'price':data['price'], 'type': f"{data['type']} burger"}
            burgers.append(burger)
        else:
            burger.update({'price':data['price']})
        
        return burgers
            
    def delete(self, name):
        global burgers
        burgers = list(filter(lambda x: x['name']!= f"{name} burger", burgers))
        return {'message': 'the burger has been deleted'}

class Allburgers(Resource):
    def get(self):
        return {'burgers': burgers}
    
api.add_resource(Burger, '/burger/<string:name>')
api.add_resource(Allburgers, '/allburgers')

app.run(port=5000, debug= True)

