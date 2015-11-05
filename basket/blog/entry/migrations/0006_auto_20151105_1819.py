# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0005_auto_20151105_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_entry',
            name='writer',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name=' author '),
        ),
    ]
