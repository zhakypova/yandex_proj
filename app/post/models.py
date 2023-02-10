from django.db import models
from django.db.models import Avg, Count

from account.models import Author


class Post(models.Model):
    text = models.TextField()
    date_public = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    avg_rating = models.FloatField(default=0.0)

    def get_rating(self):
        scores = PostRating.objects.filter(post=self) \
            .aggregate(avg=Avg('rating'))
        self.avg_rating = scores.get('avg')
        # for i in scores:
        #     self.avg_rating[i['rating']] = i['avg']
        return self.avg_rating


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_comment = models.CharField(max_length=25)
    text = models.TextField()
    date_public = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.author_comment


class Rating(models.Model):
    RATE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )

    score = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return f'{self.score}'


class PostRating(models.Model):
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f' post # {self.post} - score: {self.rating.score}'
