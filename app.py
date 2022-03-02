from flask import Flask,app
from flask_restful import  Api
# from flask_jwt import JWT, jwt_required
# from authentication import authenticate,identity
from resources.burgers import Burger,Allburgers
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///burgers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True 
app.secret_key = 'Dondecoder'
api = Api(app)


# jwt = JWT(app,authenticate, identity)

@app.before_first_request
def create_tables():
    db.create_all()
    
api.add_resource(Burger, '/burger/<string:name>')
api.add_resource(Allburgers, '/allburgers')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug= True)


