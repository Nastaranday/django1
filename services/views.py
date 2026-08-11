from django.shortcuts import render
from .models import Services, Price, Attribute

# Create your views here.
def services(request):
    services = Services.objects.filter(status = True)
    attributes = Attribute.objects.all
    pricing = Price.objects.filter(status = True)
    last_four_services = Services.objects.filter(status = True)[:4]
    context = {
        'last_four_services' : last_four_services,   
        'services' : services,
        'pricing' : pricing,
        'attributes' : attributes,
    }
    return render(request, 'services/services.html', context = context)

def services_detail(request):
    return render(request, 'services/service-details.html')
                  
                  