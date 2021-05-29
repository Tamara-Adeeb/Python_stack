from django.db import models
from django.db.models.fields import CharField
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def Registration_validator(self,postData):
        errors = {}
        # years_ago = (datetime.datetime.now() - relativedelta(years=13)).strftime("%Y%m%d")
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
    def login_validator(self,postData):
        errors = {}
        user_email = User.objects.filter(email=postData["email"])
        if len(user_email) == 0:
            errors['unvalid-email'] = "IThis email is not exist"
        else:
            if not bcrypt.checkpw(postData['password'].encode(), user_email[0].password.encode()):
                errors['password'] = "Wrong password"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updates_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User,related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User,related_name="liked_books")
    created_at = models.DateTimeField(auto_now=True)
    updates_at = models.DateTimeField(auto_now_add=True)

def creat_user(data,pw_hash):
    User.objects.create(first_name=data["fname"],last_name=data["lname"],email=data["email"],password=pw_hash)

def create_fav_book(data,id):
    user = User.objects.get(id=id)
    fav_book = Book.objects.create(title=data["title"], desc=data["desc"],uploaded_by=user)
    fav_book.users_who_like.add(user)

def update_book_desc(data,id):
    book = Book.objects.get(id=id)
    print(book,"-"*50)
    book.desc = data["updated_desc"]
    book.save()

def delete_allBook(id):
    book = Book.objects.get(id=id)
    book.delete()

def un_favorit(id,uid):
    book = Book.objects.get(id=id)
    user = User.objects.get(id=uid)
    user.liked_books.remove(book)

def user_fav_book(id,uid):
    book = Book.objects.get(id=id)
    user = User.objects.get(id=uid)
    user.liked_books.add(book)


def email_check(data):
    users=User.objects.filter(email=data["email"])
    if len(users) == 0:
        return False
    if len(users) > 0:
        return True
    

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
