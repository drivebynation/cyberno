from django.urls import path
from . import views

urlpatterns = [
    path("", views.stack_fill)
]