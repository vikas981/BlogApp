from django.contrib import admin
from django.db import models
from .models import Blog, BlogCategory, BlogSeries
from tinymce.widgets import TinyMCE


class BlogAdmin(admin.ModelAdmin):
    fields = [
        'user_name',
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


class BlogSeriesAdmin(admin.ModelAdmin):
    fields = [
        'blog_series',
        'blog_category',
        'series_summary'

    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


class BlogCategoryAdmin(admin.ModelAdmin):
    fields = [
        'blog_category',
        'blog_summary',
        'category_slug'

    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(BlogCategory,BlogCategoryAdmin)
admin.site.register(BlogSeries,BlogSeriesAdmin)
admin.site.register(Blog, BlogAdmin)
