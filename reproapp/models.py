from django.db import models

class MyModel(models.Model):
    myfield = models.CharField(max_length=10)

