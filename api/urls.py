from rest_framework import routers
from .viewset import *
from django.urls import path,include
router = routers.DefaultRouter()
router.register('student', StudentViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
