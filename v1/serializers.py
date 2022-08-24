from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserInformation, WaitlistSubscribers


class WaitlistSubsrcibersSerializers(serializers.ModelSerializer):
    class Meta:
        model = WaitlistSubscribers
        fields = '__all__'


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=255)
    password = serializers.CharField(max_length=20, write_only=True)
    username = serializers.CharField(read_only=True,max_length=255)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)


class RegisterSerializer(serializers.Serializer):
    user = UserSerializer(required=True)
    phone = serializers.CharField(max_length=15, required=False)
    GENDER_CHOICES = (('M','Male'), ('F', 'Female'))
    gender = serializers.ChoiceField(GENDER_CHOICES, required=False)
    AGE_CHOICES = (('Young','18 - 25'), ('Youth', '25 - 50'), ('Old', '50 - Above'))
    age = serializers.ChoiceField(AGE_CHOICES, required=False)
    country = serializers.CharField(max_length=100)
    country_state = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=300, required=False)
    nationality = serializers.CharField(max_length=100)
    channel = serializers.CharField(max_length=300, required=False)

    def create(self, validated_data):
        _user = validated_data.get('user')
        user = User.objects.create_user(
            username=_user.get('email').lower(),
            email=_user.get('email').lower(),
            password=_user.get('password'),
            first_name=_user.get('first_name'),
            last_name=_user.get('last_name'),
        )
        information = UserInformation.objects.create(
            user=user,
            phone=validated_data.get('phone'),
            age=validated_data.get('age'),
            gender=validated_data.get('gender'),
            country=validated_data.get('country'),
            country_state=validated_data.get('country_state'),
            address=validated_data.get('address'),
            nationality=validated_data.get('nationality'),
            channel=validated_data.get('channel'),
        )
        return information