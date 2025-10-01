from django.contrib import admin

from .models import Postagem, Blog

admin.site.register(Postagem)
admin.site.register(Blog)