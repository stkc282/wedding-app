from django.urls import path
from . import views

urlpatterns = [
    path('', views.top_page, name='top_page'),
    path('detail/', views.detail, name='detail'),
    path('input_page/', views.input_page, name='input_page'),
    path('send_page/', views.send_page, name='send_page'),
]