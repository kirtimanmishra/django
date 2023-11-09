from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import MyApp

# Create your views here.


def helloRender(request):
    return render(request, "hello.html", {"today": "sunday"})


def hello(request, time_of_day=None):
    if time_of_day is None:
        response = "Hello!"
    else:
        response = f"Hello at {time_of_day}!"
    return HttpResponse(response)


def default(request):
    text = f"welcome to myapp default page"
    return HttpResponse(text)


def article(request, article_id):
    response = f"Article id at {article_id}!"
    return HttpResponse(response)


def default(request):
    response = "this is my app default page"
    return HttpResponse(response)


def post_myapp(request, name, type, phonenumber):
    myApp = MyApp(name=name, type=type, phonenumber=phonenumber)
    myApp.save()
    response = f"{myApp} is saved"
    return HttpResponse(response)


def get_myapp(request):
    type = request.GET.get("type")
    myApp = MyApp.objects.filter(type=type)
    return HttpResponse(f"get my app {myApp}")
