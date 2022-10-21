from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is the soft life. This is my first django app")