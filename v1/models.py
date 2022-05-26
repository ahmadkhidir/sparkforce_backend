from django.db import models


class WaitlistSubscribers(models.Model):
    fullname = models.CharField(max_length=300, blank=False, null=False)
    country = models.CharField(max_length=200, blank=False, null=False)
    phone = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=400, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    field_of_interest = models.CharField(
        max_length=500, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Waitlist subscribers's"
