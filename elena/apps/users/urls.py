
from django.urls import path, include
from rest_framework import routers

from .profile import *

router = routers.DefaultRouter()

router.register('registration', ProfileAPIView)
router.register('subject/create', SubjectAPIView)

urlpatterns = [
    path('', include(router.urls))
]
