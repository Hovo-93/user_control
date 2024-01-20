from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializers import UserModelSerializer, UserDetailSerializer
from django.core.validators import EmailValidator
from django.http import JsonResponse


class UserCreate(generics.CreateAPIView):
    """
    Создание User
    """
    serializer_class = UserModelSerializer

    def post(self, request, *args, **kwargs):

        try:
            EmailValidator(request.data['email'])
        except ValidationError:
            return JsonResponse({'error': 'Invalid Email'}, status=400)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserList(generics.ListAPIView):
    """
        Список всех User
    """
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserDetail(generics.RetrieveAPIView):
    """
        Детальная информация User
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserDelete(generics.DestroyAPIView):
    """
     Удаление
    """
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return JsonResponse({'deleted': f'{instance.email}'}, status=204)


