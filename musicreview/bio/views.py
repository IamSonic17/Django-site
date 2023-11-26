from django.shortcuts import render
from .models import Bio


def bio_home(request):
    bios = Bio.objects.order_by('date')
    return render(request, template_name='bio/bio_home.html', context={'bios': bios})

