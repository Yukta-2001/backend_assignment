from django.urls import path
from .views import google_auth, google_callback

urlpatterns = [
    path("login/", google_auth),
    path("callback/", google_callback),
]
