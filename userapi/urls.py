"""userapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info, Contact, License
from rest_framework.permissions import AllowAny
schema_view = get_schema_view(
    Info(
        title='Users_Control',
        default_version='1.0',
        description='full documentation api',
        contact=Contact(email='ogannes@mail.ru'),
        license=License(name='MIT')
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    path('swagger/', schema_view.with_ui()),

]