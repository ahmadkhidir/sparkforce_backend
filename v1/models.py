from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from datetime import timedelta
from django.utils import timezone

from v1.utils import courses_image_path, hash_words, opportunities_image_path, validate_rate

from .querysets import OTPQueryset

User._meta.get_field('email')._unique = True

now = timezone.now()

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=4)
    created = models.DateTimeField(auto_created=True, auto_now_add=True)
    type = models.CharField(max_length=50)
    EXPIRES_IN = timedelta(minutes=10)
    objects = OTPQueryset.as_manager()

    def __str__(self) -> str:
        return f"{self.user.email} | {self.type}"


class LearningContent(models.Model):
    icon = models.ImageField(_('Content icon'), upload_to=courses_image_path, blank=True, null=True)
    underlay = models.ImageField(_('Background Image'), upload_to=courses_image_path, blank=True, null=True)
    title = models.CharField(_('Title'), max_length=200)
    company = models.CharField(_('Company'), max_length=200)
    platform = models.CharField(_('Platform'), max_length=200)
    time_posted = models.DateTimeField(_('Time posted'), auto_now=True)
    cost = models.PositiveIntegerField(_('Cost in dollar'), default=0)
    TYPE_OPTION = [('remote', 'remote')]
    type = models.CharField(_('Employment type'), choices=TYPE_OPTION, max_length=200)
    visitors = models.ManyToManyField(User)
    period_start = models.DateTimeField(_('Starting Period'), default='django.utils.timezone.now')
    period_end = models.DateTimeField(_('Ending Period'))
    author = models.CharField(_("Author Name"), max_length=200, null=True, blank=True)
    about = models.TextField(_('About course'), blank=True, null=True, help_text="This field use markdown")
    experience = models.TextField(_('What you will learn'), blank=True, null=True, help_text="This field use markdown")
    skills = models.TextField(_('Skills you will gain'), blank=True, null=True, help_text="This field use markdown")
    # author = Not yet decided

    @property
    def total_rates(self):
        return self.rating_set.all().aggregate(Sum('rate'))['rate__sum'] or 0


class Rating(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    learning_content = models.ForeignKey(LearningContent, models.CASCADE)
    rate = models.PositiveIntegerField(_('Number of rating'), default=1, validators=[validate_rate])

    def __str__(self) -> str:
        return f"{self.user.email} ({self.rate} star)"


class VolunteerOpportunity(models.Model):
    icon = models.ImageField(_('Content icon'), upload_to=opportunities_image_path, blank=True, null=True)
    underlay = models.ImageField(_('Background Image'), upload_to=opportunities_image_path, blank=True, null=True)
    title = models.CharField(_('Title'), max_length=200)
    company = models.CharField(_('Company'), max_length=200)
    address = models.CharField(_('Address'), max_length=500)
    time_posted = models.DateTimeField(_('Time posted'), auto_now=True)
    point = models.PositiveIntegerField(_('Point'), default=0)
    TYPE_OPTION = [('remote', 'remote')]
    type = models.CharField(_('Employment type'), choices=TYPE_OPTION, max_length=200)
    visitors = models.ManyToManyField(User)
    period_start = models.DateTimeField(_('Starting Period'), default='django.utils.timezone.now')
    period_end = models.DateTimeField(_('Ending Period'))
    author = models.CharField(_("Author Name"), max_length=200, null=True, blank=True)
    about = models.TextField(_('About course'), blank=True, null=True, help_text="This field use markdown")
    # experience = models.TextField(_('What you will learn'), blank=True, null=True, help_text="This field use markdown")
    # skills = models.TextField(_('Skills you will gain'), blank=True, null=True, help_text="This field use markdown")
    # author = Not yet decided
