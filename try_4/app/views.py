from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Advertisement
from .forms import AdvForm

def index(request):
    advertisements=Advertisement.objects.all()
    context={'advertisements' : advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form=AdvForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement=form.save(commit=False)
            new_advertisement.user=request.user
            new_advertisement.save()
            url=reverse('main-page')
            return redirect(url)
    else:
        form=AdvForm()
    context={'form' : form}
    return render(request, 'advertisement-post.html', context)

# Create your views here.
