from datetime import datetime
import json
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.renderers import JSONRenderer, AdminRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_409_CONFLICT
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.views import View
from django.shortcuts import render
from v1.filters import LearningContentFilter, VolunteerOpportunityFilter
from v1.paginations import LimitOffsetPaginationWeb

from v1.permissions import IsAdminUserOrReadOnly

from .serializers import LearningContentSerializer, RegisterSerializer, AllUserInformationSerializer, VolunteerOpportunitySerializer, WaitlistSubsrcibersSerializers

from .models import OTP, LearningContent, UserInformation, VolunteerOpportunity, WaitlistSubscribers


class WaitlistSubscribersListView(ListCreateAPIView):
    queryset = WaitlistSubscribers.objects.all()
    serializer_class = WaitlistSubsrcibersSerializers
    permission_classes = [IsAdminUser]
    renderer_classes = [JSONRenderer, AdminRenderer]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(email__iexact=request.data['email']):
            return Response({
                'detail': 'User with the same email already exists.'
            },
                status=HTTP_409_CONFLICT
            )
        return super().create(request, *args, **kwargs)


class TestBed(View):
    def get(self, request):
        ctx = {
            # 'name': 'Princewill',
            'token': '1234',
            'expired': datetime.now()
        }
        return render(request, 'v1/otp.html', ctx)
        

# Remember to change to CreateAPIVIew
class RegisterView(ListCreateAPIView):
    serializer_class = RegisterSerializer
    queryset = UserInformation.objects.all()
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class GetOTPView(APIView):
    '''**Send new generated OTP to user**'''
    def post(self, request:HttpRequest):
        data = json.loads(request.body)
        email = data.get('email').lower()
        password = data.get('password')
        user = authenticate(username=email, password=password)
        if user:
            res = OTP.objects.send_otp(email)
            if res:
                return Response({'detail': 'OTP sent'}, 200)
            return Response({'detail': 'Error while sending OTP'}, 503)
        return Response({'detail': 'invalid email or password'}, 401)


class LoginView(APIView):
    def post(self, request:HttpRequest):
        data = json.loads(request.body)
        email = data.get('email').lower()
        password = data.get('password')
        otp = data.get('otp')
        user = authenticate(username=email, password=password)
        if user:
            res = OTP.objects.validate_otp(user, otp)
            if res:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'detail': {'token': token.key}}, 200)
            return Response({'detail': 'Invalid OTP'}, 417)
        return Response({'detail': 'invalid email or password'}, 401)


class CheckUserValidityView(APIView):
    def post(self, request:HttpRequest):
        data = json.loads(request.body)
        token = data.get('token')
        if not token:
            return Response({'detail': False})
        user = User.objects.filter(auth_token__key=token).first()
        return Response({'detail': True if user else False}, 200)


class CheckUserRegistrationConflict(APIView):
    def post(self, request:HttpRequest):
        data = json.loads(request.body)
        email = data.get('email').lower()
        if not email:
            return Response({'detail': False})
        user = User.objects.filter(email=email).first()
        return Response({'detail': True if user else False}, 200)


class LearningContentView(ListCreateAPIView):
    permission_classes = [ IsAuthenticated, IsAdminUserOrReadOnly]
    queryset = LearningContent.objects.all()
    serializer_class = LearningContentSerializer
    renderer_classes=[AdminRenderer, JSONRenderer]
    pagination_class = LimitOffsetPaginationWeb
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'company']
    filterset_class = LearningContentFilter


class LearningContentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [ IsAuthenticated, IsAdminUserOrReadOnly]
    queryset = LearningContent.objects.all()
    serializer_class = LearningContentSerializer
    renderer_classes=[AdminRenderer, JSONRenderer]


class VolunteerOpportunityView(ListCreateAPIView):
    permission_classes = [ IsAuthenticated, IsAdminUserOrReadOnly]
    queryset = VolunteerOpportunity.objects.all()
    serializer_class = VolunteerOpportunitySerializer
    renderer_classes=[AdminRenderer, JSONRenderer]
    pagination_class = LimitOffsetPaginationWeb
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'company']
    filterset_class = VolunteerOpportunityFilter


class VolunteerOpportunityDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [ IsAuthenticated, IsAdminUserOrReadOnly]
    queryset = VolunteerOpportunity.objects.all()
    serializer_class = VolunteerOpportunitySerializer
    renderer_classes=[AdminRenderer, JSONRenderer]


class UserInformationView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = AllUserInformationSerializer
    renderer_classes = [AdminRenderer, JSONRenderer]

    def list(self, request:HttpRequest, *args, **kwargs):
        user_id = request.user.id
        user = self.get_queryset().filter(id=user_id).first()
        ser = self.get_serializer(user)
        return Response(ser.data)
    