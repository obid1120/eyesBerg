from rest_framework.serializers import ModelSerializer

from .models import LogoModel, ConferenceModel


class LogoSerializer(ModelSerializer):
    class Meta:
        model = LogoModel
        fields = '__all__'


class ConferenceSerializer(ModelSerializer):
    class Meta:
        model = ConferenceModel
        fields = '__all__'