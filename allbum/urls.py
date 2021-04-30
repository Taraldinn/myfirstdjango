from django.urls import path, include
from . import views

app_name = 'allbum'

urlpatterns =[
    path('', views.allbum, name='allbum')
]

