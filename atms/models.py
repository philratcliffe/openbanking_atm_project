from django.db import models

# An ATMService can be in many ATMs
class ATMService(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return(self.name)

# An ATM can have many ATMServices
class ATM(models.Model):
    atmid = models.CharField(max_length=32, unique=True)
    atmservices = models.ManyToManyField(ATMService)

    def __str__(self):
        return(self.atmid)




