from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#def hello_world(request):
#    return HttpResponse("안녕하세요!")

def hello_world(request):
    if request == 'POST':
        return render(request, "accountapp/hello_world.html",
                      context={'text':'POST METHOD'})
    else:
        return render(request, "accountapp/hello_world.html",
                      context={'text':'GET METHOD'})