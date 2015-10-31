from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Blog_Entry(models.Model):
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField(default=timezone.now)
    approved=models.BooleanField(default=False)
    visited_date=models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True)

    @models.permalink
    def get_absolute_url(self):
        return 'blog:post', (self.slug,)

    def update(self):
        self.visited_date=datetime.datetime.now()
        self.save()


    def __str__(self):              # __unicode__ on Python 2
        return self.headline
