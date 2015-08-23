from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=200)



class Tag(models.Model):
    name = models.CharField(max_length=200)



class TagClient(models.Model):
    signal = models.IntegerField()
