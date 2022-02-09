from flask import Flask,app
from flask_restful import  Api
# from flask_jwt import JWT, jwt_required
# from authentication import authenticate,identity
from burgers import Burger,Allburgers


app = Flask(__name__)
app.secret_key = 'Dondecoder'
api = Api(app)


# jwt = JWT(app,authenticate, identity)



    
api.add_resource(Burger, '/burger/<string:name>')
api.add_resource(Allburgers, '/allburgers')

app.run(port=5000, debug= True)


