from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_timetable, name='exam_timetable'),
    path('history/', views.exam_history, name='exam_history'),
]