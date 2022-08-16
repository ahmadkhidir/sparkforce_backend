from django.urls import path

from v1 import views


app_name = 'v1'

urlpatterns = [
    path('waitlist-subscribers/', views.WaitlistSubscribersListView.as_view()),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('get_otp/', views.GetOTPView.as_view(), name='get_otp'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('check_user_validity/', views.CheckUserValidityView.as_view(), name='check_user_validity'),
]
