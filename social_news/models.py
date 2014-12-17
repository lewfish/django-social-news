import datetime

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

    #scoring function from
    #http://amix.dk/blog/post/19574
    def compute_score(self, gravity=1.8):
        age_delta = datetime.datetime.utcnow() - self.post_date.replace(tzinfo=None)
        hour_age = age_delta.days * 24 + age_delta.seconds // 3600
        return (self.num_votes - 1) / pow((hour_age + 2), gravity)

class Vote(models.Model):
    entry = models.ForeignKey(Entry, null=True)
    voter = models.ForeignKey(User, null=True)
    
