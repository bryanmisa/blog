from django.db import models
from django.utils import timezone   
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):

    # enum type, suggested to use enum classes for text choices
    class Status(models.TextChoices):
        DRAFT = 'DF', 'DRAFT'
        PUBLISHED = 'PB', 'PUBLISHED'

    title = models.CharField(max_length=250) 
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                                # models.CASCADE will delete all related post
                                # when the user is deleted.
                                on_delete=models.CASCADE,
                                # allows us to access related objects from a user
                                # by using the user.blog_posts notation
                                related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, 
                              choices=Status.choices,
                              default=Status.DRAFT)

    class Meta:
        
        # sort in reverse chronological order in descending order
        ordering = ['-publish'] 
        indexes = [
            # define database indexes on model Post, in descending order
            models.Index(fields=['publish']) 
        ]

    def __str__(self):
        return self.title

