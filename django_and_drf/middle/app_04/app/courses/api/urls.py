from django.urls import path, include
from rest_framework import routers
from courses.api import views, viewsets

app_name = 'courses'

router = routers.DefaultRouter()
router.register('courses', viewsets.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('subjects/', views.SubjectListView.as_view(), 
                        name='subject_list'),
    path('subjects/<pk>/', views.SubjectDetailView.as_view(), 
                        name='subject_detail'),
    path('courses/<pk>/enroll/', views.CourseEnrollView.as_view(),
                        name='course_enroll'),

]