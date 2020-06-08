from django.http import HttpResponse


def index(request):
    return HttpResponse("User login page")

# Create your views here.
