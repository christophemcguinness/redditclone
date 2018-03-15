from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    url = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votes_total = models.IntegerField(default=0)


    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')