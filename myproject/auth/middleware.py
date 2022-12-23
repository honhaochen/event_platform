from django.core.cache import cache
from django.http import JsonResponse

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ignore auth path
        if 'api/auth/' in request.path:
            response = self.get_response(request)
            return response

        auth_session_token = request.COOKIES.get('AUTH_SESSION_TOKEN') 
        if auth_session_token is None:
            return JsonResponse({"error": "error_not_logged_in"})
        
        # inject user data in request
        request.user = cache.get(auth_session_token)
        if request.user is None:
            return JsonResponse({"error": "error_not_logged_in"})

        response = self.get_response(request)
        return response