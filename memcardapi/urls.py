from rest_framework.routers import DefaultRouter
from django.urls import path
from memcardapi import viewsets

router = DefaultRouter()
router.register('user', viewsets.UserViewSet, basename='user')

urlpatterns = router.urls