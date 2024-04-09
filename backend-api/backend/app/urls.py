from . import views
from django.urls import path

urlpatterns = [
    path('students/', views.get_all_students, name='get_all_students'),
    path('students/<int:student_id>/', views.get_student, name='get_student'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/<int:student_id>/update/', views.update_student, name='update_student'),
    path('students/<int:student_id>/delete/', views.delete_student, name='delete_student'),
]
