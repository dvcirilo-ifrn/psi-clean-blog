from django.shortcuts import render, get_object_or_404
from .models import Postagem, Blog

def index(request):
    context = {
        "blog": Blog.objects.first(),
        "postagens": Postagem.objects.all(),
    }
    return render(request, 'blog/index.html', context)

def post(request, id_post):
    context = {
        "blog": Blog.objects.first(),
        "post": get_object_or_404(Postagem, id=id_post),
    }
    return render(request, 'blog/post.html', context)

def sobre(request):
    context = {
        "blog": Blog.objects.first(),
    }
    return render(request, 'blog/sobre.html', context)

def contato(request):
    context = {
        "blog": Blog.objects.first(),
    }
    return render(request, 'blog/contato.html', context)
