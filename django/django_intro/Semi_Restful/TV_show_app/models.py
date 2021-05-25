from typing import Text
from django.db import models
from django.db.models.fields import DateTimeField

class showManager(models.Manager):
    def validator(self, enterd_show):
        errors = {}
        if len(enterd_show['title']) < 2:
            errors["title"] = "Book title should be at least 2 characters"
        if len(enterd_show["network"]) < 3:
            errors["network"] = "Book network should be at least 3 characters"
        if len(enterd_show["desc"]) < 10 :
            errors["description"] = "Book description should be at least 3 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = DateTimeField()
    description = models.TextField(null=True)
    objects = showManager()

def create_show(title,network,date,decs):
    Show.objects.create(title=title,network=network,release_date=date,description=decs)

def update_show(show_id,title,network ,date,decs):
    show = Show.objects.get(id=show_id)
    show.title = title
    show.network = network
    show.release_date = date
    show.description = decs
    show.save()

def delete_show(delete_id):
    delete = Show.objects.get(id=delete_id)
    delete.delete()

