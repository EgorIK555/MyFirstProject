from django.db import models
class Enemy(models.Model):
     name = models.CharField(max_length=10)
     damage = models.IntegerField()
     speed = models.IntegerField()
     health = models.IntegerField()
     avatar = models.ImageField(blank=True)

