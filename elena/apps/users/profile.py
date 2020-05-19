from django.db.models import Count
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import Subjects, UserProfile
from .serializers import ProfileSerializers, SubjectSerializers


class ProfileAPIView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializers
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save()


class SubjectAPIView(ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializers
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save()
