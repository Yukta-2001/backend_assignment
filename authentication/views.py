from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
import google.oauth2.credentials
import google_auth_oauthlib.flow

CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ["openid", "https://www.googleapis.com/auth/userinfo.email"]

@api_view(["GET"])
def google_auth(request):
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES
    )
    flow.redirect_uri = "http://localhost:8000/auth/callback"
    authorization_url, state = flow.authorization_url()
    return Response({"auth_url": authorization_url})

@api_view(["GET"])
def google_callback(request):
    return Response({"message": "Google authentication successful"})
