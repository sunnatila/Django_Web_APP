from django.urls import path
from .views import home_page_view, post_create_view

urlpatterns = [
    path("", home_page_view, name="home"),
    path("post/create", post_create_view, name="post_create"),
]
