from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='show_topics_index' ),
]