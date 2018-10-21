from django.db import models


# An ATM can have many ATMServices
class ATM(models.Model):
    atmid = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.atmid




