from django.http import JsonResponse

def chat_home(request):
    return JsonResponse({"message": "Chat app is working!"})
