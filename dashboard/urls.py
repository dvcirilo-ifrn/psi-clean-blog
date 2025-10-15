from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('posts/novo/', views.posts_novo, name='posts_novo'),
    path('posts/<int:id_post>/detalhar/', views.posts_detalhar, name='posts_detalhar'),
    path('posts/<int:id_post>/editar/', views.posts_editar, name='posts_editar'),
    path('posts/<int:id_post>/remover/', views.posts_remover, name='posts_remover'),
]