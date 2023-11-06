from django.http import HttpResponse
from django.shortcuts import render

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
