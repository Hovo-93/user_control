from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UserList.as_view(), name='users-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('users/create/', views.UserCreate.as_view(), name='user-create'),
    path('delete/<int:pk>/', views.UserDelete.as_view(), name='user-delete'),
]