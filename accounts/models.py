from django.db import models

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    imageurl = models.CharField(max_length=255)
