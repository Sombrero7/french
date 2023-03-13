# pages/urls.py
from django.urls import path
from . import views # new

urlpatterns = [
    path('', views.opposites, name='home'),
    path('ds/', views.selection, name="data_selection")
]