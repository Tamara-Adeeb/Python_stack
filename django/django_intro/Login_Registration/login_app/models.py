from django.db import models
from django.db.models.fields import CharField
from django.db import models
import re

class UserManager(models.Manager):
    def Registration_validator(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData["fname"]) < 2:
            errors["fname"] = "User first name should be at least 2 characters"
        if len(postData["lname"]) < 2:
            errors["fname"] = "User last name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):          
            errors['unvalid-email'] = "Invalid email address!"
        if  len(postData["password"]) < 8:
            errors["lenpassword"] = "User password should be at least 8 characters"
        if  postData["password"] != postData["cpw"] :
            errors["password"] = "password does not match"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

def creat_user(data,pw_hash):
    User.objects.create(first_name=data["fname"],last_name=data["lname"],email=data["email"],birthday=data["birthday"],password=pw_hash)

def email_check(data):
    users=User.objects.filter(email=data["email"])
    user_email=users[0]
    if user_email == None:
        return False
    else:
        True

def check_user(data):
    users=User.objects.filter(email=data["email"])
    user=users[0]
    if bcrypt.checkpw(data['password'].encode(), user.password.encode()):
        return True
    if user == None:
        return False
    return False