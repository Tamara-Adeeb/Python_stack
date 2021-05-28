from django.db import models
from django.http import request
import re
import bcrypt

class   (models.Manager):
    def registration_validater(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData["fname"]) and len(postData["lname"]) < 2:
            errors["first_name"] = "The name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):          
            errors['email'] = "Invalid email address!"
        if postData["password"] != postData["cpw"] and len(postData["password"]) <8:
            errors["password"] = "unvalid password"
        return errors
    # def login_validaterv(self,login_data):
    #     pass


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = loginManager()



def register(data,password):
    Users.objects.create(first_name=data["first_name"],last_name=data["last_name"],email=data["email"],password=password) 

def check_user(data):
    users=Users.objects.filter(email=data["email"])
    user=users[0]
    if bcrypt.checkpw(data['password'].encode(), user.password.encode()):
        return True
    if user == None:
        return False
    return False