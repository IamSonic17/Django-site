from django.shortcuts import render
from .models import Reviews
from django.views.generic import DetailView


class ReviewsDetailView(DetailView):
    model = Reviews
    template_name = 'review/review_details.html'
    context_object_name = 'rev'


def reviews_home(request):
    rev = Reviews.objects.order_by('-date')
    return render(request, template_name='reviews/reviews_home.html', context={'rev': rev})

