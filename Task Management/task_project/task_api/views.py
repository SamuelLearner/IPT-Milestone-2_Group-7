from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer


# Create your views here.
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        # Create user with encrypted password
        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
    

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data["message"] = "Task created successfully"
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.data["message"] = "Task created successfully"
        return response