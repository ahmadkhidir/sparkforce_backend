from rest_framework import serializers

from .models import WaitlistSubscribers


class WaitlistSubsrcibersSerializers(serializers.ModelSerializer):
    class Meta:
        model = WaitlistSubscribers
        fields = '__all__'
