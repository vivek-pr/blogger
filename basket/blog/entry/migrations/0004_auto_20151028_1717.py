# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0003_auto_20151028_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_entry',
            name='body_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog_entry',
            name='visited_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
