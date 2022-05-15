from django.urls import path

from .views import WaitlistSubscribersListView


urlpatterns = [
    path('waitlist-subscribers/', WaitlistSubscribersListView.as_view())
]
