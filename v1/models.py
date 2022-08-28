from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import timedelta

from .querysets import OTPQueryset

User._meta.get_field('email')._unique = True


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



class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(_('Phone Number'), max_length=15, blank=True, null=True)
    AGE_CHOICES = (('Young','18 - 25'), ('Youth', '25 - 50'), ('Old', '50 - Above'))
    age = models.CharField(_('Age Range'), max_length=10, choices=AGE_CHOICES, blank=True, null=True)
    GENDER_CHOICES = (('M','Male'), ('F', 'Female'))
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    country = models.CharField(_('Country'), max_length=100)
    country_state = models.CharField(_('State'), max_length=100)
    address = models.CharField(_('Home Address'), max_length=300, blank=True, null=True)
    nationality = models.CharField(_('Nationality'), max_length=100)
    channel = models.CharField(_('How did you hear about Sparkforce'), max_length=300, blank=True, null=True)

    def __str__(self) -> str:
        return self.user.email


class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=4)
    created = models.DateTimeField(auto_created=True, auto_now_add=True)
    EXPIRES_IN = timedelta(minutes=10)
    objects = OTPQueryset.as_manager()

    def __str__(self) -> str:
        return self.user.email