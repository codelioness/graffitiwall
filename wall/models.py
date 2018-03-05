from django.db import models
from django.utils import timezone

class Post(models.Model):
    post_text = models.TextField(max_length=400)
    author_name = models.CharField(max_length=40)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.post_text
