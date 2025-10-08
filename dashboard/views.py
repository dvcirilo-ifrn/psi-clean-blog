from django.shortcuts import render
from blog.models import Blog, Postagem

def index(request):
    context = {
        "blog": Blog.objects.first(),
    }
    return render(request, "dashboard/index.html", context)

def posts(request):
    context = {
        "blog": Blog.objects.first(),
        "posts": Postagem.objects.all(),
    }
    return render(request, "dashboard/posts.html", context)

def criar_post(request):
    pass

def visualizar_post(request, id_post):
    pass

def editar_post(request, id_post):
    pass

def remover_post(request, id_post):
    pass

