from django.urls import path
from . import views
# url configuration
# Create your urls here. but need to import the views
urlpatterns = [
    path("january", views.index, name="index"),
]