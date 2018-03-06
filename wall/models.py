from django.db import models
from django.utils import timezone

class Post(models.Model):
    post_text = models.TextField(max_length=400)
    author_name = models.CharField(max_length=40)
    pub_date = models.DateTimeField('date published')
    COLOR_CHOICES = (
        ('#eaadaa', 'Red'),
        ('#c9e2ee', 'Blue'),
        ('#fbf5c5', 'Yellow'),
        ('#bfe5ac', 'Green'),
        ('#FFE0B1', 'Orange'),
        ('#C0B4E7', 'Purple'),
        ('#FFFFFF', 'White'),
    )
    color = models.CharField(max_length=7, choices=COLOR_CHOICES, default='#FFFFFF')
    
    def __str__(self):
        return self.post_text
