from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Photo
from .serializers import PhotoSerializer

class PhotoListView(ListAPIView):
    queryset = Photo.objects.filter(archived=False)
    serializer_class = PhotoSerializer
