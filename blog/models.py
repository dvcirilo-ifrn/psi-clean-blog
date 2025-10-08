from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    titulo_blog = models.CharField(max_length=100)
    subtitulo_blog = models.CharField(max_length=100)
    bg_blog = models.ImageField(upload_to="blog/bg/", blank=True)
    titulo_sobre = models.CharField(max_length=100)
    subtitulo_sobre = models.CharField(max_length=100)
    bg_sobre = models.ImageField(upload_to="blog/bg/", blank=True)
    conteudo_sobre = models.TextField()
    titulo_contato = models.CharField(max_length=100)
    subtitulo_contato = models.CharField(max_length=100)
    bg_contato = models.ImageField(upload_to="blog/bg/", blank=True)

    def __str__(self):
        return self.titulo_blog

class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    bg_image = models.ImageField(upload_to="postagens/",
                                 blank=True, 
                                 verbose_name="Imagem de fundo"
                                 )
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Postagens"

    def __str__(self):
        return self.titulo
    
    @property
    def informacoes(self):
        return f"Postado por {self.autor} em {self.criado_em}."
