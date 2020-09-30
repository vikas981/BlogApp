from django.contrib import admin
from django.db import models
from .models import Blog, BlogCategory, BlogSeries
from tinymce.widgets import TinyMCE


class BlogAdmin(admin.ModelAdmin):
    fields = [
        'blog_title',
        'blog_content',
        'blog_published',
        'blog_slug',
        'blog_tags',
        'blog_series'
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(BlogCategory)
admin.site.register(BlogSeries)
admin.site.register(Blog, BlogAdmin)
