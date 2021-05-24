from django.db import models
from django.db.models.fields import TimeField

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

class Authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    Books = models.ManyToManyField(Books,related_name="author")
    notes = models.TextField(null=True)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

def add_book(book_title,book_desc):
    Books.objects.create(title=book_title,desc=book_desc)

def add_author(firstName,lastName,notes):
    Authors.objects.create(first_name=firstName,last_name=lastName,notes=notes)

def create_book(this_authour,Bo):
    added_book = Books.objects.get(id=Bo)
    this_authour.Books.add(added_book)

def create_auth(this_Book,Ba):
    added_auth = Authors.objects.get(id=Ba)
    this_Book.author.add(added_auth)
