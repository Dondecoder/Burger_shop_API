from flask_restful import Resource, reqparse
import sqlite3

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
        burger = self.find_by_name(name)
        if burger:
            return burger
        return {'message': 'This burger item was not found'}, 404

    def find_by_name(self,name):
        connection = sqlite3.connect('burgers.db')
        cursor = connection.cursor()

        query = "SELECT * FROM burgers WHERE name=?"
        result = cursor.execute(query, (f"{name} burger",))
        row = result.fetchone()

        connection.close()

        if row:
            return {"burger": {'name': row[0], 'price': row[1], 'type': row[2]}}

    def post(self, name):
        if self.find_by_name(name): 
            return {'message': 'This burger item is already on the list'}
        else:
            data = Burger.parser.parse_args()
            burger = {'name':f"{name} burger", 'price':data['price'], 'type': f"{data['type']} burger"}
            try:
                self.insert(burger)
            except:
                return {'message': 'An error occured inserting the item'}, 500
            return burger, 201

    def insert(self, burger):
        connection = sqlite3.connect('burgers.db')
        cursor = connection.cursor()

        query = "INSERT INTO burgers VALUES (?,?,?)"
        cursor.execute(query, (burger['name'], burger['price'], burger['type']))
        connection.commit()
        connection.close()

    def put(self,name):
        data = Burger.parser.parse_args()
        burger = self.find_by_name(name)
        updated_burger = {'name':f"{name} burger", 'price':data['price'], 'type': f"{data['type']} burger"}
        if burger is None:
            try:
                self.insert(updated_burger)
            except:
                return {"message": "An error occured inserting the item"}, 500
        else:
            try:
                self.update(updated_burger)
            except:
                {"message": "An error occured updating the item"}, 500
        return updated_burger
    
    def update(self, burger):
        connection = sqlite3.connect('burgers.db')
        cursor = connection.cursor()

        query = "UPDATE burgers SET price= ?, type =? WHERE name=?"
        cursor.execute(query, (burger['price'], burger['type'], burger['name']))
        connection.commit()
        connection.close()

            
    def delete(self, name):
        connection = sqlite3.connect('burgers.db')
        cursor = connection.cursor()

        query = "DELETE FROM burgers WHERE name=?"
        cursor.execute(query, (f"{name} burger",))
        connection.commit()
        connection.close()

        return {'message': 'the burger has been deleted'}

class Allburgers(Resource):
    def get(self):
        connection = sqlite3.connect('burgers.db')
        cursor = connection.cursor()

        query = "SELECT * FROM burgers"
        burgers = cursor.execute(query)
        row = burgers.fetchall()
        connection.commit()
        connection.close()
        if row:
            return {'burgers': row}  
        return {None}