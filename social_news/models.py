from django.db import models
from django.contrib.auth.models import User
    
class Entry(models.Model):
    title = models.CharField(max_length = 200)
    link = models.URLField(max_length = 200)
    post_date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.title

    @property
    def num_votes(self):
        return Vote.objects.filter(entry=self).count()

class Vote(models.Model):
    entry = models.ForeignKey(Entry, null=True)
    voter = models.ForeignKey(User, null=True)
    
