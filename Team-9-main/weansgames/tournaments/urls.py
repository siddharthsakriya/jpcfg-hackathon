
from tournaments import views
from django.urls import path

app_name = "tournaments"

urlpatterns = [
    path('', views.index,name="home"),
    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path('logout/', views.auth_logout, name="logout"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('child/manage/', views.add_child, name="add_child"),
    path('create-event/', views.create_event, name="create"),
    path('manage-event/<int:id>', views.manage_event, name="manage"),
    path('child/remove/', views.remove_child, name="remove_child"),
    path('game/add/', views.add_game, name="add_game"),
    path('genre/add/', views.add_genre, name="add_genre"),
    path('browse/', views.browse, name="browse"),
    path('leaderboard/',views.leaderboard,name="leaderboard")
]
