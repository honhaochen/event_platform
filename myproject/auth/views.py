from django.http import JsonResponse
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from .models import AuthTab
from django.contrib.auth.hashers import make_password,  check_password
from json import loads
import uuid

def login(request):
    request_data = loads(request.body)
    email = request_data['email']
    password = request_data['password']
    
    # check user
    user = None
    try:
        user = AuthTab.objects.get(email=email)
    except ObjectDoesNotExist:
        return JsonResponse({
                "error": "error_no_user"
            })
    
    # check password
    if not check_password(password, user.password):
        return JsonResponse({
                "error": "error_wrong_password"
            })

    # handle session cookies
    response = JsonResponse({
        "message": "sucess"
    })

    session_id = uuid.uuid4() # this is insecure
    response.set_cookie("AUTH_SESSION_TOKEN", session_id, 60*60*3) # 3 hours expiry time
    cache.set(session_id, {
        "user_id": user.id
    }, 60*60*3) # 3 hours expiry time
    return response
    

def register(request):
    request_data = loads(request.body)
    username = request_data['name']
    email = request_data['email']
    password = request_data['password']
    if username is None or email is None or password is None:
        return JsonResponse({
            "error": "error_fields_empty"
        })

    if AuthTab.objects.filter(email=email).exists():
        return JsonResponse({
            "error": "error_user_exists"
        })

    user = AuthTab(name=username, email=email, password=make_password(password), is_admin=0)
    user.save()
    return JsonResponse({
        "message": "sucess"
    })