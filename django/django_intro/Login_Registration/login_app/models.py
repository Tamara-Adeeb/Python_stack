from django.db import models
from django.db.models.fields import CharField
from django.db import models
import re
import bcrypt
import datetime
from datetime import datetime
# from dateutil.relativedelta import relativedelta

class UserManager(models.Manager):
    def Registration_validator(self,postData):
        errors = {}
        today = datetime.now().strftime("%Y%m%d")
        # user_birthday =  datetime.strptime(postData["birthday"], '%Y-%m-%d')
        # years13 = abs((today-user_birthday).days)
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData["fname"]) < 2:
            errors["fname"] = "User first name should be at least 2 characters"
        if len(postData["lname"]) < 2:
            errors["fname"] = "User last name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):          
            errors['unvalid-email'] = "Invalid email address!"
        if postData["birthday"].replace("-","") > today:
            errors['unvalid-birthday'] = "Invalid birthday"
        # if years13 < 4745:
        #     errors["birthday"] = "You should be older than 13 years to register in this website"
        if  len(postData["password"]) < 8:
            errors["lenpassword"] = "User password should be at least 8 characters"
        if  postData["password"] != postData["cpw"] :
            errors["password"] = "password does not match"
        return errors
    def login_validator(self,postData):
        errors = {}
        user_email = User.objects.filter(email=postData["email"])
        if len(user_email) == 0:
            errors['unvalid-email'] = "This email is not exist"
        else:
            if not bcrypt.checkpw(postData['password'].encode(), user_email[0].password.encode()):
                errors['password'] = "Wrong password"
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
    if len(users) == 0:
        return False
    if len(users) > 0:
        return True
    

# def check_user(data):
#     users=User.objects.filter(email=data["email"])
#     if len(users) == 0:
#         x = 'user is not found'
#         return 'user is not found'
#     else:
#         if bcrypt.checkpw(data['password'].encode(), users.password.encode()):
#             return True
#         else:
#             x = 'password is wrong'
#             return 'password is wrong'