from rest_framework import serializers

from blogapp.models import BlogCategory, BlogSeries, Blog


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'


class BlogSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSeries
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
