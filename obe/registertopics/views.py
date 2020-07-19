from django.shortcuts import render

# Create your views here.
from .models import Topic
from .serializers import TopicSerializer
from rest_framework import generics, filters
from django.http import HttpResponse

class TopicListCreate(generics.ListCreateAPIView):
	search_fields = ['topic','topic_subject', 'keyWords','description', 'image1', 'image2','image3', 'image4']
	filter_backends = (filters.SearchFilter,)
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer
