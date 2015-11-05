# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0003_auto_20151105_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_entry',
            name='visited_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='tracking for deactiavation'),
        ),
        migrations.AlterField(
            model_name='blog_entry',
            name='writer',
            field=models.ForeignKey(verbose_name=' author ', default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
