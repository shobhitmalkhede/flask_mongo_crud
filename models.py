from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash


mongo = PyMongo()

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
   
    def save(self):
        hashed_password = generate_password_hash(self.password)
        user_data = {
            'name': self.name,
            'email': self.email,
            'password': hashed_password
        }
     
        mongo.db.users.insert_one(user_data)

   
    @staticmethod
    def find_by_id(user_id):
        user = mongo.db.users.find_one({'_id': user_id})
        return user


    @staticmethod
    def find_by_email(email):
        user = mongo.db.users.find_one({'email': email})
        return user

  
    def update(self, user_id):
        hashed_password = generate_password_hash(self.password)
        updated_data = {
            'name': self.name,
            'email': self.email,
            'password': hashed_password
        }
        mongo.db.users.update_one({'_id': user_id}, {'$set': updated_data})


    @staticmethod
    def delete(user_id):
        mongo.db.users.delete_one({'_id': user_id})

  
    def check_password(self, password):
        return check_password_hash(self.password, password)
