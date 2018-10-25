from django.contrib import admin
from .models import ATM
from .models import ATMService
from .models import Accessibility


class ATMAdmin(admin.ModelAdmin):
    pass


admin.site.register(ATM, ATMAdmin)
admin.site.register(ATMService, ATMAdmin)
admin.site.register(Accessibility, ATMAdmin)
