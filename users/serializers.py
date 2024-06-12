from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True, validators=[validate_password])
    # phone = serializers.CharField()

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'phone', 'password', 'password_confirm', 'gender', 'affiliation')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'first_name', 'last_name', 'email', 'date_joined', 'last_login')
        read_only_fields = ('date_joined', 'last_login')
