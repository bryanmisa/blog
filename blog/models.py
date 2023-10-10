from django.db import models
from django.utils import timezone   

# Create your models here.

class Post(models.Mode):
    title = models.CharField(max_lenght=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        
        # sort in reverse chronological order in descending order
        ordering = ['-publish'] 
        indexes = [
            # define database indexes on model Post, in descending order
            models.Index(fields=['publish']) 
        ]

    def __str__(self):
        return self.title

