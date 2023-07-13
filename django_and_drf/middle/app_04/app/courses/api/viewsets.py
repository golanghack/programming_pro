from rest_framework import viewsets
from courses.api.serializers import CourseSerializer
from courses.models import Course

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer