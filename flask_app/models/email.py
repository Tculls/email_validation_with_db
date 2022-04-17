from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    db = "email_validation"
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# this saves the email object into our database
    @classmethod
    def save(cls,data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(cls.db).query_db(query,data)

# this will get all the emails from our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails"
        results= connectToMySQL(cls.db).query_db(query)
        emails=[]
        for row in results:
            emails.append(cls(row))
        return emails

# this method will destroy an email from the database
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

# thhis static method will veryify if a email is unique and if the email has valid conventions


    @staticmethod
    def is_valid(email):
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL(Email.db).query_db(query, email)
        if len(results) >= 1:
            flash("Email address is taken.")
            is_valid = False
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid Email adress")
            is_valid = False
        return is_valid
