from django.contrib import admin

from home.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
