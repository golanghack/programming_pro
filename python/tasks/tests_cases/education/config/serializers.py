from rest_framework import serializers
from app.models import Lesson, Content, Product

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name_of_lesson',
                    'video',
                    'duration',
                    'visited', 
                    'current_time',]

class LessonsListSerializer(serializers.ModelSerializer):
    