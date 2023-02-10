from django.db.models import Avg
from rest_framework import serializers
from .models import Post, Comment, Rating, PostRating


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['avg_rating', 'author']




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['post', 'author']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ['author', 'post']


class PostRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostRating
        fields = '__all__'
        read_only_fields = ['author', 'post']
