from app import views
from django.urls import path

urlpatterns = [
    path('students/', views.studentApi, name='get_students'),
    path('students/<int:student_id>/', views.studentApi, name='get_update_delete_student'),
    path('students/create/', views.studentApi, name='create_student'),
]
