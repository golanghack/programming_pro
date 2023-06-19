from django.contrib import admin
from django.urls import path, include
from core.routers import router, urlpatterns as simplerouter

urlpatterns = [
    #path("admin/", admin.site.urls),
]
urlpatterns += simplerouter