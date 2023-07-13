from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from courses.api.serializers import CourseSerializer
from courses.models import Course

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, 
            methods=['post'],
            authentication_classes=[BasicAuthentication,],
            permission_classes=[IsAuthenticated,])
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({
            'enrolled': True
        })