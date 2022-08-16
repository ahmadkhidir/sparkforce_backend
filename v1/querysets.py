from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import User
import random

from .templates import OTP_TEMPLATE, OTP_TEMPLATE_HEADER

now = timezone.now()

class OTPQueryset(models.QuerySet):
    def validate_otp(self, user, token) -> bool:
        otp = self.filter(user=user).first()
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
    
    def send_otp(self, email):
        print('the email',email)
        token = str(random.randint(1000, 9999))
        try:  
            user = User.objects.filter(email=email).first()
            print('current',user)
            otp_user = self.filter(user=user).first()
            if otp_user:
                otp_user.delete()
                print('I delete', user)
            self.create(user=user, token=token)
            send_mail(
            subject=OTP_TEMPLATE_HEADER, 
            message=OTP_TEMPLATE.format(token=token, expires=self.model.EXPIRES_IN),
            recipient_list=[email],
            from_email=None
            )
        except Exception as e:
            print(e)
            otp_user = self.filter(user=user).first()
            if otp_user:
                otp_user.delete()
            return False
        return True
