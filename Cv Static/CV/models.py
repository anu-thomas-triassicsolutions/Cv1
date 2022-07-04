from django.db import models


class Cv(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=250)

    def __str__(self):
        return self.name

