from django.urls import path
from .views import upload_file, list_files

urlpatterns = [
    path("upload/", upload_file),
    path("list/", list_files),
]
