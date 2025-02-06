from django.urls import path
from .views import (
    home_page_view,
    post_create_view,
    post_delete_view,
    post_edit_view,
    post_page_view,

)
from django.contrib.auth.views import LoginView

urlpatterns = [
    # blog panel urls
    path("", home_page_view, name="home"),
    path("category/<tag>/", home_page_view, name="category"),
    path("post/create/", post_create_view, name="post_create"),
    path("post/delete/<pk>/", post_delete_view, name="post_delete"),
    path("post/edit/<pk>/", post_edit_view, name="post_edit"),
    path("post/detail/<pk>/", post_page_view, name="post_page"),
]
