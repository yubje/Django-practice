from django.shortcuts import render, redirect, get_object_or_404

from .models import Review
from .forms import ReviewForm


def review_list(request):
    reviews = Review.objects.order_by('-pk')
    context = {'reviews':reviews}
    return render(request, 'community/review_list.html', context)

def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('community:review_list')
    else:
        form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, 'community/form.html', context)

def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    context = {
        'review': review,
    }
    return render(request, 'community/review_detail.html', context)