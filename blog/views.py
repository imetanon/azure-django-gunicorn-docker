from django.shortcuts import render

def index(request):
    from django.conf import settings
    context = { 
        'settings': settings
    }
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    return render(request, 'blog/detail.html')

