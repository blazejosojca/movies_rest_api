from django.contrib import admin
from .models import Person, Movie, Role


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'description',
                    'director',
                    'actors',
                    'year',
                    'ranking']


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['movie',
                    'person',
                    'role']
