from django.contrib import admin

from django.urls import path
from .import views


from django.http import HttpResponse



urlpatterns = [
    path("login/", views.loginPage,name="login"),
    path("logout/", views.logoutuse,name="logout"),
    path("register/",views.registerPage,name='register'),
    path("admin/", admin.site.urls),
    path("create-room/", views.createroom, name="create-room"),  # Specific route first
    path("update-room/<int:pk>/", views.updateroom, name="update-room"),
    path("profile/<str:username>/", views.userProfile, name="user-profile"),
    path("delete-room/<int:pk>/", views.deleteroom, name="delete-room"),
    path("delete-message/<int:pk>/", views.deletemessage, name="delete-message"),
    path("room/<int:pk>/", views.room, name="room"),  # Use int if Room ID is an integer
    path("", views.home, name="home"),  # Home route last
    path("update-user/",views.updateUser,name="update-user"),
    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
]
