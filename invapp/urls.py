from django.urls import path
from . import views

urlpatterns = [
    path('', views.top_page, name='top_page'),
    path('detail/', views.detail, name='detail'),
    path('input/', views.input, name='input'),
    path('send/', views.send, name='send'),
]