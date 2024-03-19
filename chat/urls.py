from django.urls import path, include
from chat import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'messages', views.MessageViewSet, basename='message')
router.register(r'rooms', views.RoomViewSet, basename='room')

urlpatterns = [
    path('', include(router.urls)),
]
