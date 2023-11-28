from django.shortcuts import render
from .models import Bio
from django.views.generic import DetailView


class BioDetailView(DetailView):
    model = Bio
    template_name = 'bio/bio_details.html'
    context_object_name = 'biography'


def bio_home(request):
    bios = Bio.objects.order_by('-date')
    return render(request, template_name='bio/bio_home.html', context={'bios': bios})

