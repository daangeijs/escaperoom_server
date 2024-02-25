from django.http import HttpResponse

def clear_session(request):
    request.session.flush()  # This will delete the current session data and cookie.
    return HttpResponse("Session cleared!")
