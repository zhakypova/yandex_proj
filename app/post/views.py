import os

import telebot
from rest_framework import generics, views
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from . import tasks
from .models import Post, Comment, PostRating, Rating
from .permissions import IsAuthorPermission
from .serializers import PostSerializer, CommentSerializer, RatingSerializer



class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        post = serializer.save(author=self.request.user.author)
        tasks.send_message.delay(f'Ваш пост: {post.id} успешно добавлен')


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorPermission | IsAdminUser]


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(
            post_id=self.kwargs.get('post_id'),
            author=self.request.user.author
        )


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser, ]

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs.get('post_id'))


class RatingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class RatingRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthorPermission, ]


class PostRatingCreateAPI(views.APIView):
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs.get('post_id'))
        rating = Rating.objects.get(score=kwargs.get('score'))
        post_rating = PostRating.objects.create(
            rating=rating,
            post=post,
            author=request.user.author
        )
        return Response({'message': 'Score added'}, status=201)




