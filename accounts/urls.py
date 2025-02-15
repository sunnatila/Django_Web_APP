from django.contrib.auth.views import LoginView
from django.urls import path
from .views import (
    profile_view,
    profile_edit_view,
    user_register_view,
    logout_view,
    profile_delete_view
)

urlpatterns = [
    path('edit/', profile_edit_view, name="profile_edit"),
    path('delete/', profile_delete_view, name="profile_delete"),

    path('', profile_view, name="profile"),
    path('<username>/', profile_view, name="userprofile"),
    path("accounts/signup/", user_register_view, name="sign_up"),
    path("accounts/logout/", logout_view, name="log_out"),
    path("accounts/login/", LoginView.as_view(), name="login"),
]
