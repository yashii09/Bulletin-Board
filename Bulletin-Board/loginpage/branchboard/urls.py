from django.urls import path, include
from . import views

app_name = 'branchboard'
urlpatterns = [
	path('student', views.student),
	path('teacher', views.teacher),
	path('teacher/upload', views.upload),
	# path('dashboard/', include('dashboard.urls')),
	path('student/<branch>/dashboard/', include('dashboard.urls')),
	path('teacher/<branch>/dashboard/', include('dashboard.urls')),
]