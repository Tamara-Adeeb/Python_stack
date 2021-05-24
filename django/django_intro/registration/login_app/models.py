from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def register(username,password):
    Users.objects.create(name=username,password=password)

def check_user(name,passed):
    user=Users.objects.filter(name=name)
    if user == None:
        return False
    if user[0].password == passed:
        return True
    return False