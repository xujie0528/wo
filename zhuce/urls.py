from django.urls import re_path
from zhuce import views
urlpatterns = [
    re_path(r'^zhuce/$', views.func)
]