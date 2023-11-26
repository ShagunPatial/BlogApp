from django.db import models
from user_auth.models import BgUser, TrackableMixin


# Create your models here.
class Blog(TrackableMixin):
    author = models.ForeignKey(BgUser, related_name='blogger',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    blog_reactions = models.ManyToManyField('Reaction', blank=True)

    def __str__(self):
        return self.title


class Comment(TrackableMixin):
    author = models.ForeignKey(BgUser, related_name='commentors',
                               on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    comment_reactions = models.ManyToManyField('Reaction',
                                               blank=True)

    def __str__(self):
        return self.content


class Reaction(TrackableMixin):
    LIKE = 'like'
    DISLIKE = 'dislike'

    REACTION_CHOICES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    ]

    user = models.ForeignKey(BgUser, related_name='reactor',
                                on_delete=models.CASCADE)
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES)
    blog_post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True, related_name='reactions')
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, related_name='reactions')

    def __str__(self):
        return self.reaction_type

    class Meta:
        unique_together = ('user', 'blog_post')  # Ensure a user can only react once to a blog post
