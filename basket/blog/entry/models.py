from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.
class Blog_Entry(models.Model):
    headline = models.CharField(' title ' , max_length = 150 , db_index = True )
    snippet = models.CharField ( ' summary ' , max_length = 500 , default = ' ' )
    body_text = models.TextField(' content ' ,)
    pub_date = models.DateField(' creation time ' , auto_now_add = True )
    approved=models.BooleanField(' approved by maintainer',default=False)
    visited_date=models.DateTimeField('tracking for deactiavation',default=timezone.now)
    slug = models.SlugField(unique=True)
    writer = models.ForeignKey (User, verbose_name = ' author ')


    @models.permalink
    def get_absolute_url(self):
        return 'blog:post', (self.slug,)

    def update(self):
        self.visited_date=datetime.datetime.now()
        self.save()

    def  Save ( self , user, * args , ** kwargs ):
        self .snippet =  self .snippet or  self .content [: 140 ]
        self.writer= User.objects.get(username=user)
        super (Blog_Entry, self ) .save ( * args, ** kwargs)


    def __str__(self):              # __unicode__ on Python 2
        return self.headline
