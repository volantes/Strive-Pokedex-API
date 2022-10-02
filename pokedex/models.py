from django.db import models


class Type(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    types = models.ManyToManyField(Type)
    is_caught = models.BooleanField(default=False)
    hp = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    special_attack = models.IntegerField(default=0)
    special_defense = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)

    def __str__(self):
        return self.name
