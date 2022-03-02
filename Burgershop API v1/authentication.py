from customer import Customer

customers = [
    Customer(3,'John','shark')
]


username_mapping = {c.username: c for c in customers}

user_id_mapping = {c.id: c for c in customers}


def authenticate(username, password):
    customer = username_mapping.get(username, None)
    if customer and customer.password == password:
        return customer
    return {'message': 'Information is invalid'}, 404

def identity(payload):
    user_id = payload["identity"]
    return user_id_mapping(user_id, None)