from .models import User

from rest_framework.serializers import ModelSerializer


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )


class UserDetailSerializer(ModelSerializer):
    """
        Детальная информация
    """

    class Meta:
        model = User
        fields = '__all__'
