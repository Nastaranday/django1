from django.shortcuts import render
from services.models import Services, Features
# Create your views here.

def home(request):
    last_four_services = Services.objects.filter(status = True)[:4]
    last_four_features = Features.objects.filter(status = True)[:4]
    context = {
        'last_four_services' : last_four_services,
        'last_four_features' : last_four_features,    
    }
    return render(request, 'root/index.html', context = context)

def contact_us(request):
    return render(request, 'root/contact.html')

def about(request):
    return render(request, 'root/about.html')