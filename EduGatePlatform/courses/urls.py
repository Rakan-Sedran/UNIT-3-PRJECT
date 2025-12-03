from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("assign-subject/", views.assign_subject_to_class, name="assign_subject"),
    path("enroll-students/", views.enroll_students_in_class, name="enroll_students"),
]
