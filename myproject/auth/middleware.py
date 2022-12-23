from django.core.cache import caches
from django.http import JsonResponse

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ignore login path
        if request.path == '/auth/login':
            response = self.get_response(request)
            return response

        auth_session_token = request.COOKIES.get('AUTH_SESSION_TOKEN') 
        if auth_session_token is None:
            return JsonResponse({"error": "error_not_logged_in"})
        
        # inject user data in request
        request.user = caches.get(auth_session_token)
        response = self.get_response(request)
        return response