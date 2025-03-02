from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def upload_file(request):
    return Response({"message": "File uploaded successfully"})

@api_view(["GET"])
def list_files(request):
    return Response({"files": ["file1.pdf", "file2.docx"]})
