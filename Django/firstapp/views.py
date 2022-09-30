from django.http import JsonResponse

def indexPage(request):
    return JsonResponse({"message" : "Hello World!"})
