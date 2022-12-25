from django.http import JsonResponse

# Create your views here.
def event_view(request, page_id):
    return JsonResponse({
        "currentPage": page_id
    })

def event_comment(request):
    return JsonResponse({})

def event_participate(request):
    return JsonResponse({})

def event_like(request):
    return JsonResponse({})