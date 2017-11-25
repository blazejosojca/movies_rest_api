from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return "{} {}".format(self.first_name,
                              self.last_name)
