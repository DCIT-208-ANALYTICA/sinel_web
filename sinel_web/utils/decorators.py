from django.shortcuts import redirect
from django.urls import reverse


def superuser_only(redirect_url="accounts:login"):
    """Allow only super administrator to access this view."""
    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if (request.user.is_authenticated and request.user.is_superuser):
                return function(request, *args, **kwargs)

            request.session['error_message'] = "Please login as as admin."
            referer = request.META.get('HTTP_REFERER')
            next = referer or "/"
            return redirect(reverse(redirect_url) + f"?next={next}")

        return wrapper

    return decorator
    
def staff_only(redirect_url="accounts:login"):
    """Allow only super administrator to access this view."""
    def decorator(function):
        def wrapper(request, *args, **kwargs):
            if (request.user.is_authenticated):
                return function(request, *args, **kwargs)

            request.session['error_message'] = "Please login as as admin."
            referer = request.META.get('HTTP_REFERER') or "dashboard:index"
            return redirect(reverse(redirect_url) + f"?next={referer}")

        return wrapper

    return decorator
    