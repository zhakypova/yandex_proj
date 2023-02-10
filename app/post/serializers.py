from django.db.models import Avg
from rest_framework import serializers
from .models import Post, Comment, Rating, PostRating


class PostSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['avg_rating', 'author']

    # def create(self, validated_data):
    #     rating = Post(avg_rating=validated_data['avg_rating'],)
    #     rating.save()


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


