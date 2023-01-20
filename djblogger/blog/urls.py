from django.urls import path
from djblogger.blog import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name = 'homepage'),
    path('<slug:post>/',views.post_single,name ='post_single')
]
