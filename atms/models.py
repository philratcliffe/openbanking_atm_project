from django.db import models


class ATMManager(models.Manager):

    def delete_all(self):
        return self.all().delete()


class ATMServiceManager(models.Manager):

    def delete_all(self):
        return self.all().delete()


class ATMService(models.Model):
    name = models.CharField(max_length=33, unique=True)

    objects = ATMServiceManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class ATM(models.Model):
    atmid = models.CharField(max_length=32, unique=True)
    atm_services = models.ManyToManyField(ATMService)

    objects = ATMManager()

    def __str__(self):
        return self.atmid

    class Meta:
        ordering = ('atmid',)




