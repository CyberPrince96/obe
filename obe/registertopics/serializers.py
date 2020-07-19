from rest_framework import serializers
from .models import Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id','topic', 'author_name', 'topic_subject', 'keyWords','description', 'last_modified', 'image1', 'image2','image3', 'image4')