from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    return render(request,template_name)


def details(request):
    template_name = 'details.html'
    return render ( request, template_name )

def details2(request):
    template_name = 'radisson.html'
    return render ( request, template_name )