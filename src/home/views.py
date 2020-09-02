import random
import string

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import ShortUrl
from .forms import CreateShortURLForm


def index(request):
    form = CreateShortURLForm()
    urls = ShortUrl.objects.all().order_by('-id')

    if request.method == 'POST':
        form = CreateShortURLForm(request.POST)
        if form.is_valid():
            shorty = form.save(commit=False)
            shorty.slug = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
            shorty.save()
            return HttpResponseRedirect('/new_url/{}'.format(shorty.slug))

    context = {
        'form': form,
        'urls': urls
    }

    return render(request, 'base.html', context)

def new_url(request, slug):
    context = {
        'shorty': ShortUrl.objects.get(slug=slug)
    }

    return render(request, 'new_url.html', context)

def url_redirect(request, slug):
    shorty = ShortUrl.objects.get(slug=slug)
    url = shorty.original

    return redirect(url)