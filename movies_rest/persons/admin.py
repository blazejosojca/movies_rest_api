from django.contrib import admin
from persons.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']

# Register your models here.
