import django
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save


# Create your models here.

class BlogCategory(models.Model):
    blog_category = models.CharField(max_length=80)
    blog_summary = models.CharField(max_length=100)
    category_slug = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.blog_category


class BlogSeries(models.Model):

    blog_series = models.CharField(max_length=100)
    blog_category = models.ForeignKey(BlogCategory, default=1, verbose_name='Category', on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.blog_series


class Blog(models.Model):

    blog_title = models.CharField(max_length=100)
    blog_content = models.TextField()
    blog_published = models.DateField("date post", default=django.utils.timezone.now)
    blog_series = models.ForeignKey(BlogSeries, default=1, verbose_name='Series', on_delete=models.SET_DEFAULT)
    blog_tags = models.CharField(max_length=250)
    blog_slug = models.SlugField(unique=True)

    def __str__(self):
        return self.blog_title


def pre_save_post_receiver(instance, *args, **kwarges):
    blog_slug = slugify(instance.blog_title)
    exists = Blog.objects.filter(blog_slug=blog_slug).exists()
    if exists:
        blog_slug = "%s-%s" % (blog_slug, instance.id)
    instance.blog_slug = blog_slug


pre_save.connect(pre_save_post_receiver, sender=Blog)
