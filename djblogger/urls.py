from django.contrib import admin
from django.urls import path,include
from djblogger.blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('djblogger.blog.urls')),
]
