from django.contrib import admin
from .models import ATM
from .models import ATMService

class ATMAdmin(admin.ModelAdmin):
    pass

class ATMServices(admin.ModelAdmin):
    pass

admin.site.register(ATM)
admin.site.register(ATMService)
