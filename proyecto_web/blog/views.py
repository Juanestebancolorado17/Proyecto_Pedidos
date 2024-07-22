from django.shortcuts import render
from blog.models import Post, Categoria

def blog(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts, 'categorias': categorias})


def table(request):
    poster = Post.objects.all()
    return render(request, 'table.html', {'posts': poster})


def filtrar_por_categoria(request, categoria):
    posts = Post.objects.filter(categorias__nombre=categoria)
    categorias = Categoria.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts, 'categorias': categorias})



