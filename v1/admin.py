from django.contrib import admin

from v1 import models

# Register your models here.

admin.site.register(models.WaitlistSubscribers)
admin.site.register(models.UserInformation)
admin.site.register(models.OTP)
