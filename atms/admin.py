from django.contrib import admin
from .models import ATM

class ATMAdmin(admin.ModelAdmin):
    pass

admin.site.register(ATM)
