# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entry', '0002_auto_20151028_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_entry',
            name='snippet',
            field=models.CharField(max_length=500, default=' ', verbose_name=' summary '),
        ),
        migrations.AddField(
            model_name='blog_entry',
            name='writer',
            field=models.ForeignKey(verbose_name=' author ', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog_entry',
            name='approved',
            field=models.BooleanField(verbose_name=' approved by maintainer', default=False),
        ),
        migrations.AlterField(
            model_name='blog_entry',
            name='body_text',
            field=models.TextField(verbose_name=' content '),
        ),
        migrations.AlterField(
            model_name='blog_entry',
            name='headline',
            field=models.CharField(db_index=True, max_length=150, verbose_name=' title '),
        ),
        migrations.AlterField(
            model_name='blog_entry',
            name='pub_date',
            field=models.DateField(verbose_name=' creation time ', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog_entry',
            name='visited_date',
            field=models.DateTimeField(verbose_name='tracking for deactiavation', auto_now_add=True),
        ),
    ]
