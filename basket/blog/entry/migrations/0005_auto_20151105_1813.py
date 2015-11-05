# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0004_auto_20151105_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_entry',
            name='visited_date',
            field=models.DateTimeField(verbose_name='tracking for deactiavation', default=django.utils.timezone.now),
        ),
    ]
