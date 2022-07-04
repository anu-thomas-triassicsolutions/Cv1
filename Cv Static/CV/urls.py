from django.urls import path
from .import views

urlpatterns = [
    path('', views.cv, name='cv'),
    path('add/', views.add, name='add'),
]
