from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from app_conference.models import LogoModel, ConferenceModel
from app_conference.serializers import LogoSerializer, ConferenceSerializer


# Create your views here.
class LogoViewSet(ModelViewSet):
    queryset = LogoModel.objects.all()
    serializer_class = LogoSerializer


class ConferenceViewSet(ModelViewSet):
    queryset = ConferenceModel.objects.all()
    serializer_class = ConferenceSerializer