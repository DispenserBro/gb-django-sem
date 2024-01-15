from django.urls import path

import app_1.views as views


urlpatterns = [
    path('', views.index, name='index'),
    path('coin/', views.coin_flip, name='coin'),
    path('c/', views.coin_stat, name='coin_stat'),
    path('r/', views.random_number, name='random'),
]