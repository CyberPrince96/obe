from django.urls import path
from . import views

urlpatterns = [
    path('topic/', views.TopicListCreate.as_view() ),
    path('topic/images/<str:imgname>', views.renderImg ),
]