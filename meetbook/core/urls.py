from django.urls import path, include
# custom imports
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]