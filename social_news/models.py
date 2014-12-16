from django.db import models
    
class Entry(models.Model):
    title = models.CharField(max_length = 200)
    link = models.URLField(max_length = 200)
    post_date = models.DateTimeField(auto_now_add = True)
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
