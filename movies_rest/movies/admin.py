from django.contrib import admin
from .models import Movie, Role


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['role']
