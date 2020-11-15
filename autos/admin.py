from django.contrib import admin
from .models import Auto, Comment, Alquiler

# Register your models here.

class AutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'marca', 'modelo', 'ano']

admin.site.register(Auto, AutoAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'auto', 'user']

admin.site.register(Comment, CommentAdmin)

class AlquilerAdmin(admin.ModelAdmin):
    list_display = ['id', 'auto', 'user']

admin.site.register(Alquiler, AlquilerAdmin)