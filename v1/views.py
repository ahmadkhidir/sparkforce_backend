from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import AdminRenderer, JSONRenderer

from .serializers import WaitlistSubsrcibersSerializers

from .models import WaitlistSubscribers


class WaitlistSubscribersListView(ListCreateAPIView):
    queryset = WaitlistSubscribers.objects.all()
    serializer_class = WaitlistSubsrcibersSerializers
    permission_classes = [IsAuthenticated]
    renderer_classes = [AdminRenderer]
