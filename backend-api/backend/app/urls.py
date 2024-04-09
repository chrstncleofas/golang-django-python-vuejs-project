from app import views
from django.conf.urls import url

urlpatterns = [
    # Frontend API
    url(r'^students$',views.studentsApi),
    url(r'^students/([0-9]+)$',views.studentsApi),
]
