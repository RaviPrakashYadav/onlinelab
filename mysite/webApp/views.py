from django.shortcuts import render


# Create your views here.
# def index(request):
#     return HttpResponse("<h2>hey!</h2>")


def index(request):
    return render(request, "webapp/home.html")


def contact(request):
    return render(request, "webapp/basic.html", {'content': ['You can email me at :', 'raviprakashlts@gmail.com']})
