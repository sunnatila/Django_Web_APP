from django.urls import path
from .views import *


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
    path('comment/reply/delete/<pk>/', reply_delete_view, name='reply_delete'),

    # like panel

    path('post/like/<pk>/', like_post_view, name='post_like'),
    path('comment/reply/like/<pk>/', like_reply_view, name='reply_like'),
    path('comment/like/<pk>/', like_comment_view, name='comment_like'),
]
