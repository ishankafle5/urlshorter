
from django.http import HttpResponse
from django.shortcuts import redirect, render
import random

from url.models import Url


def indexpage(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        string = ['a', 'b', 'c', 'd', 'e', 'f']
        link = request.POST.get('link')

        suffix = ''
        for i in range(1, 10):
            a = random.choice(string)
            suffix += a
        print(suffix)
        shortlink = ''
        objectcreate = Url.objects.create(real_url=link, shorturl=suffix)

        print(suffix)
        base_url = str(request.build_absolute_uri("/"))+'link/'+suffix

        return render(request, 'result.html', {'short_link': base_url})


def shorturl(request, value):
    # value = request.GET.get('value')
    objectcheck = Url.objects.get(shorturl=value)

    return redirect(objectcheck.real_url)
