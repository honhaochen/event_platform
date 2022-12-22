from django.http import JsonResponse

# Create your views here.
def index(request):
    data = {}
    return JsonResponse(data)