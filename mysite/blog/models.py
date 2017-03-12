from django.db import models

# Model for the blog applications


class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=35)
    comment_date = models.DateTimeField('date published')
    comment_body = models.TextField()



