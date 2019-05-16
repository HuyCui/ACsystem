from django.db import models

# Create your models here.


class thdata(models.Model):
    temp = models.FloatField()
    hmui = models.FloatField()


class user(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=16)

    def obj_to_json(self):
        return {
            "username": self.username,
            "password": self.password
        }


class score(models.Model):
    score = models.IntegerField()
    date = models.CharField(max_length=30)

    def obj_to_json(self):
        return {
            "score": self.score,
            "date": self.date
        }