from django.shortcuts import render, redirect, get_object_or_404
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
        form = PostagemModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard:posts")
        else:
            context["form"] = form
    else:
        context["form"] = PostagemModelForm()
    return render(request, "dashboard/posts_novo.html", context)

def posts_detalhar(request, id_post):
    return render(request,
                  "dashboard/posts_detalhar.html",
                  {"post": get_object_or_404(Postagem, id=id_post)}
            )

def posts_editar(request, id_post):
    context = {
        "blog": Blog.objects.first(),
        "post": get_object_or_404(Postagem, id=id_post),
    }
    if request.method == "POST":
        form = PostagemModelForm(request.POST, instance=context["post"])
        if form.is_valid():
            form.save()
            return redirect("dashboard:posts")
        else:
            context["form"] = form
    else:
        context["form"] = PostagemModelForm(instance=context["post"])
    return render(request, "dashboard/posts_editar.html", context)

def posts_remover(request, id_post):
    context = {
        "blog": Blog.objects.first(),
        "post": get_object_or_404(Postagem, id=id_post),
    }
    if request.method == "POST":
        context["post"].delete()
        return redirect("dashboard:posts")
    else:
        return render(request, "dashboard/posts_remover.html", context)