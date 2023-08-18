
from django.urls import path, re_path, include
from . import views as list_views 
from . import routers

urlpatterns = [
    re_path('$', list_views.home, name='home'),
    path('lists/', include(routers)),
]