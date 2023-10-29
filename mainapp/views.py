from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')

def specialists(request):
    return render(request, 'mainapp/specialists.html')

def contacts(request):
    return render(request, 'mainapp/contact.html')