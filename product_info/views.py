import re
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


from .models import Contact

def index(request):
    return render(request, 'index.html')

def dev_info(request):
    return render(request, 'dev_info.html')

def about(request):
    return render(request, 'about.html')

def order(request):
    return render(request,'order.html')


def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        comments = request.POST.get('comments')
        contact.name=name
        contact.email=email
        contact.comments = comments
        contact.save()
        return HttpResponse('<h1>Thanks for Contract with us</h1>')
    return render(request, 'contact.html')
def showdata(request):
    data = Contact.objects.all()
    print(data)
    return render(request, 'showdata.html', {'Contact': data})

def orderdata(request):
    data = order.object.all()
    print(data)
    return render(request, 'orderdata.html', {'order': data})