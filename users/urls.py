from django.urls import path

from . import views

app_name = "users"


urlpatterns = [
    # login paths
    path("login/", views.login_view, name="login_function"), # view function
    path("api/v1/users/login/", views.LoginView.as_view(), name="login_api"), # api
    
    # sign up paths
    path("signup/", views.signup_view, name="signup_function"), # view function
    path("api/v1/users/signup/", views.SignUpView.as_view(), name="signup_api"), # api
    
    # log out paths
    path("logout/", views.logout_view, name="logout_view"),
    path("api/v1/users/logout/", views.LogOutView.as_view(), name="logout_api"), # api
    
    # view profile
    path("profile/", views.profile_view, name="profile_function"), # view function
    path("api/v1/users/profile/", views.ProfileView.as_view(), name="profile_api"), # api
    
    # 
]
