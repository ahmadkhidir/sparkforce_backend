from django.db import models
from django.utils import timezone
from django.core.mail import send_mail, EmailMultiAlternatives
from email.mime.image import MIMEImage
from django.template.loader import render_to_string
from django.contrib.auth.models import User
import random
from django.templatetags.static import static

from .templates import OTP_TEMPLATE, OTP_TEMPLATE_HEADER

now = timezone.now()


class OTPQueryset(models.QuerySet):
    def check_otp(self, user, token, type) -> bool:
        otp = self.filter(user=user, type=type).first()
        token = str(token)
        if not otp:
            return False
        _token = otp.token
        valid = _token == token
        not_expire = now - otp.created < self.model.EXPIRES_IN
        if valid and not_expire:
            return True
        return False
    
    def validate_otp(self, user, token, type) -> bool:
        otp = self.filter(user=user, type=type).first()
        token = str(token)
        if not otp:
            return False
        _token = otp.token
        valid = _token == token
        not_expire = now - otp.created < self.model.EXPIRES_IN
        if valid and not_expire:
            otp.delete()
            return True
        return False

    def send_otp(self, email, type) -> bool:
        token = str(random.randint(1000, 9999))
        try:
            user = User.objects.filter(email=email).first()
            otp_user = self.filter(user=user, type=type).first()
            if otp_user:
                otp_user.delete()
            self.create(user=user, token=token, type=type)
            ctx = {
                'name': user.first_name,
                'token': token,
                'expired': str(self.model.EXPIRES_IN).split(':')[1],
                'type': type
            }
            send_mail(
            subject=OTP_TEMPLATE_HEADER,
            message=OTP_TEMPLATE.format(token=token, expires=self.model.EXPIRES_IN),
            recipient_list=[email],
            from_email=None,
            html_message=render_to_string('v1/otp.html', ctx)
            )
        except Exception as e:
            otp_user = self.filter(user=user, type=type).first()
            if otp_user:
                otp_user.delete()
            return False
        return True
