# middleware.py

from django.shortcuts import redirect
from django.urls import reverse


class CheckLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is not logged in and trying to access a protected feature
        if not request.user.is_authenticated and request.path == '//':
            return redirect(reverse('login'))  # Redirect to login page

        response = self.get_response(request)
        return response