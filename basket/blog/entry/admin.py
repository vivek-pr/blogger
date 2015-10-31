from django.contrib import admin
from entry.models import Blog_Entry
from django.contrib.auth.models import User

def make_published(modeladmin, request, queryset):
    queryset.update(approved=True)
make_published.short_description = "Mark selected stories as published"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['headline', 'approved']
    ordering = ['headline']
    actions = [make_published]

class UserAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','password']


admin.site.register(Blog_Entry, ArticleAdmin)
