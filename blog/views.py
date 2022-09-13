from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'dogbot',
        'title' : 'blogpost 1',
        'content' : 'bush did 7/11',
        'date_posted' : 'September 12th, 2022'
    },
    {
        'author' : 'nutbot',
        'title' : 'blogpost 2',
        'content' : 'obama did 4/20',
        'date_posted': 'September 13th, 2022'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

