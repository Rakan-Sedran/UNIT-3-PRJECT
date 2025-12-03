from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path("create-class/", views.create_class, name="create_class"),
    path("add-announcement/", views.add_announcement, name="add_announcement"),
]
