from django.shortcuts import render

from .models import fire_service
from .forms import EmergencyForm

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')

def gallery(request):
    context = {'all_request': fire_service.objects.all()}
    return render(request, 'gallery.html', context)

def service(request):
    return render(request, 'services.html')

def gallery_single(request):
    return render(request, 'gallery-single.html')

def teams(request):
    return render(request, 'teams.html')

def all_request(request):
    context = {
        'all_request': fire_service.objects.all()
    }
    return render(request, 'gallery.html', context)

def details(request, id):
    context = {
        'photo' : fire_service.objects.get(id=id),
    }
    return render(request, 'photo-details.html', context)

def contact_view(request):
    form = EmergencyForm()
    if request.method=="POST":
        form = EmergencyForm(data=request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form':form,
    }
    return render(request, 'contact.html', context)
