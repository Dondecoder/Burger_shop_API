from flask import Flask,app


burgers = []

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///burgers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Dondecoder'
api = Api(app)


jwt = JWT(app,authenticate, identity)

    
api.add_resource(Burger, '/burger/<string:name>')
api.add_resource(Allburgers, '/allburgers')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug= True)

