# pages/urls.py
from django.urls import path
from . import views # new

urlpatterns = [
    path('', views.verbs_view, name='verbs_view'),
    path('select_verbs/', views.select_verbs_view, name='select_verbs_view'),
    path('select_tenses/', views.select_tenses_view, name='select_tenses_view'),
    path('select_POVs/', views.select_POVs_view, name='select_POVs_view'),
    path('practice/', views.practice_view, name='practice_view'),
]