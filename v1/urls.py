from django.urls import path

from v1 import views


app_name = 'v1'

urlpatterns = [
    path('test_bed/', views.TestBed.as_view()),
    path('waitlist-subscribers/', views.WaitlistSubscribersListView.as_view()),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('get_otp/', views.GetOTPView.as_view(), name='get_otp'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('user_information/', views.UserInformationView.as_view(), name='user_information'),
    path('check_user_validity/', views.CheckUserValidityView.as_view(), name='check_user_validity'),
    path('check_user_registration_conflict/', views.CheckUserRegistrationConflict.as_view(), name='check_user_registration_conflict'),
    path('learning_content/', views.LearningContentView.as_view(), name='learningcontent'),
    path('learning_content/<int:pk>/', views.LearningContentDetailView.as_view(), name='learningcontent-detail'),
    path('volunteer_opportunity/', views.VolunteerOpportunityView.as_view(), name='volunteeropportunity'),
    path('volunteer_opportunity/<int:pk>/', views.VolunteerOpportunityDetailView.as_view(), name='volunteeropportunity-detail'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('verify_forgot_password/', views.VerifyForgotPasswordEmailView.as_view(), name='verify_forgot_password'),
    path('forgot_password/', views.ForgotPasswordView.as_view(), name='forgot_password'),
]
