from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}} # esto es para hacer un campo de contraseña para q solo sea escritura

    def create(self, validated_data): #crear basicamente un usuario y caldidar los datos que no se repitan
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user
# validar los datos de los usurios creados
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
# para presentar los detalles del usuario
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']