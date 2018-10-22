from django.db import models


class ATMManager(models.Manager):

    def delete_all(self):
        return self.all().delete()


# An ATM can have many ATMServices
class ATM(models.Model):
    atmid = models.CharField(max_length=32, unique=True)

    objects = ATMManager()

    def __str__(self):
        return self.atmid




