from django.shortcuts import HttpResponse

# Create your views here.
def get_privet(request):
    return HttpResponse("<h1>privet</h1>")