from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
from .views import TaskViewSet, CategoryViewSet


router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    # Include the router's URLS
    path('', include(router.urls)),

    # User registration URL
    path('register/', views.register, name='register')
]

