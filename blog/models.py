from django.db import models
from login_system.models import User
from django.urls import reverse 
from datetime import datetime, date


STATUS = (
    (0,"Hidden"),
    (1,"Publish")
)

class Post(models.Model):
    question = models.CharField(max_length= 255)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    answer = models.TextField(blank= True)
    post_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.question + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.post.question, self.name ) 
        