from django.http import HttpResponse

# Create your views here.

# https://docs.djangoproject.com/en/2.1/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/',
#     domain=None, secure=None, httponly=False, samesite=None)
def cookie(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get('zap', None)
    resp = HttpResponse('In a view - the zap cookie value is '+str(oldval))
    if oldval :
        resp.set_cookie('zap', int(oldval)+1) # No expired date = until browser close
    else :
        resp.set_cookie('zap', 42) # No expired date = until browser close
        resp.set_cookie('dj4e_cookie', '4b025079', max_age=1000)
    return resp


def sessfun(request) :
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    return HttpResponse('view count='+str(num_visits))