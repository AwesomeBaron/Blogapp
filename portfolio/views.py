from django.shortcuts import render

#from django.http import HttpResponse


#def index(request):
   # return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    template = 'portfolio/home.html'
    context = {}
    return render(request, template, context)
