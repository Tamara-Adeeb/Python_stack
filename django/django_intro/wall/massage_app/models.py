from django.db import models
from django.db import models
import re
import bcrypt

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

class Massage(models.Model):
    massage_content = models.TextField()
    user_id = models.ForeignKey(User, related_name="massages",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment_content = models.TextField()
    massage_id = models.ForeignKey(Massage, related_name="comments",on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def creat_user(data,pw_hash):
    User.objects.create(first_name=data["fname"],last_name=data["lname"],email=data["email"],birthday=data["birthday"],password=pw_hash)

def email_check(data):
    users=User.objects.filter(email=data["email"])
    if len(users) == 0:
        return False
    if len(users) > 0:
        return True
    # user_email=users[0]
    # if user_email == None:
    #     return False
    # else:
    #     True

def check_user(data):
    users=User.objects.filter(email=data["email"])
    if len(users) == 0:
        x = 'user is not found'
        return 'user is not found'
    else:
        if bcrypt.checkpw(data['password'].encode(), users.password.encode()):
            return True
        else:
            x = 'password is wrong'
            return 'password is wrong'

def add_massage(data,user):
    Massage.objects.create(massage_content=data["massage_content"],user_id=user )

def add_comment(data,massage,user):
    Comment.objects.create(comment_content=data["comment_content"],massage_id=massage,user_id=user)

def del_massage(id):
    deleted_massage = Massage.objects.get(id=id)
    deleted_massage.delete()

def del_comment(id):
    deleted_comment = Comment.objects.get(id=id)
    deleted_comment.delete()