from django.shortcuts import render
from .models import Services

# Create your views here.
def services(request):
    services = Services.objects.filter(status = True)
    context = {
        'services' : services,
    }
    return render(request, 'services/services.html', context = context)

def services_detail(request):
    return render(request, 'services/service-details.html')
                  
                  