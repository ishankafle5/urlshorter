
from django.shortcuts import render
import random

from .models import Url
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
        shortlink = ''
        objectcreate=Url.objects.create(real_url=link,shorturl=suffix)
        print(suffix)
        return render(request, 'result.html', {'short_link': suffix})

def shorturl(request,*args, **kwargs):
    value=''