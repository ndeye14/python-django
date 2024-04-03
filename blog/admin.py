from django.contrib import admin
# imporation de notre modele post
from .models import Post
# enregistre notre model
admin.site.register(Post)