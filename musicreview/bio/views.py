from django.shortcuts import render


def bio_home(request):
    return render(request, template_name='bio/bio_home.html')
