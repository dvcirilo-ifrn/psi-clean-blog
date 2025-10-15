from django.shortcuts import render, redirect
from blog.models import Blog, Postagem
from blog.forms import PostagemModelForm 

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

def posts_novo(request):
    context = {
        "blog": Blog.objects.first(),
    }
    if request.method == "POST":
        print("ajaj")
        return redirect("dashboard:posts")
    else:
        context["form"] = PostagemModelForm()
    return render(request, "dashboard/posts_novo.html", context)





def posts_detalhar(request, id_post):
    pass

def posts_editar(request, id_post):
    pass

def posts_remover(request, id_post):
    pass

