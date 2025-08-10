from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('greet/<str:username>/', views.greet_user, name='greet_user'),
    path('greet/', views.greeting_view, name='greet'),
    path('submit/', views.submit_view, name='submit'),
    path('create/', views.person_create_view, name='person_create'),
    path('list/', views.person_list_view, name='person_list'),
    path('delete/<int:pk>/', views.person_delete_view, name='person_delete'),
]
