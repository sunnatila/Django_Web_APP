from django.urls import path
from .views import (
    home_page_view,
    post_create_view,
    post_delete_view,
    post_edit_view,
    post_page_view,
    comment_sent,
    comment_delete_view,
    reply_sent,

)


urlpatterns = [
    # blog panel urls
    path("", home_page_view, name="home"),
    path("category/<tag>/", home_page_view, name="category"),
    path("post/create/", post_create_view, name="post_create"),
    path("post/delete/<pk>/", post_delete_view, name="post_delete"),
    path("post/edit/<pk>/", post_edit_view, name="post_edit"),
    path("post/detail/<pk>/", post_page_view, name="post_page"),

    # comment panel

    path('comment/sent/<pk>/', comment_sent, name='comment_sent'),
    path('comment/delete/<pk>/', comment_delete_view, name='comment_delete'),
    path('comment/reply/<pk>/', reply_sent, name='reply_sent'),
]
