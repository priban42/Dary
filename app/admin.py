from django.contrib import admin
from app.models import Dar

@admin.register(Dar)
class DarAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
