from django.urls import path
from django.views.decorators.cache import cache_page
from students import views

urlpatterns = [
    path('register/', views.StudentsRegistrationView.as_view(), 
                            name='student_registration'),
    path('enroll-course/', views.StudentEnrollCourseView.as_view(), 
                                        name='student_enroll_course'),
    path('courses/', cache_page(60 * 10)(views.StudentCourseListView.as_view()), 
                                        name='student_course_list'),
    path('course/<pk>/', views.StudentCourseDetailView.as_view(), 
                                        name='student_course_detail'),
    path('course/<pk>/<module_id>/', cache_page(60 * 10)(views.StudentCourseDetailView.as_view()),
                                        name='student_course_detail_module'),
]