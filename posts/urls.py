from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.write, name='write'),
    path('Top/', views.Top, name='Top'),
]