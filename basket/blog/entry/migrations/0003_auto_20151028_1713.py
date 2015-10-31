# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_auto_20151028_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_entry',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blog_entry',
            name='body_text',
            field=models.TextField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='blog_entry',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
