from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
	path('student', views.student),
	path('teacher', views.teacher),
]