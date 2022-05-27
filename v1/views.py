from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_409_CONFLICT

from .serializers import WaitlistSubsrcibersSerializers

from .models import WaitlistSubscribers


class WaitlistSubscribersListView(ListCreateAPIView):
    queryset = WaitlistSubscribers.objects.all()
    serializer_class = WaitlistSubsrcibersSerializers
    permission_classes = [IsAuthenticated]
    # renderer_classes = [JSONRenderer]

    def create(self, request, *args, **kwargs):
        if self.queryset.filter(email__iexact=request.data['email']):
            return Response({
                'detail': 'User with the same email already exists.'
            },
                status=HTTP_409_CONFLICT
            )
        return super().create(request, *args, **kwargs)
