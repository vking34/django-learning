from django.contrib import admin
from .models import Board, Post, Topic

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    # fields = ['description', ]

    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Description', {'fields' : ['description']}),
    ]
    list_display = ('name', 'description')
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Board, BoardAdmin)