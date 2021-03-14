from django.urls import path

from . import views

app_name = 'Commandes'
urlpatterns = [
    path('', views.index3, name='index3')
]