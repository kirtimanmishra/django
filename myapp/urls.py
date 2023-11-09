from django.contrib import admin
from django.urls import path, re_path
from myapp.views import *

urlpatterns = [
    path("hello/", hello, name="my-view"),
    path("hello/<str:time_of_day>/", hello, name="my-time-of-day"),
    path("hello-render/", helloRender),
    path("article/<int:article_id>/", article, name="article_id"),
    path("<str:name>/<str:type>/<int:phonenumber>", post_myapp),
    path("", get_myapp),
    # path("", default),
]
