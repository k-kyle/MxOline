# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-04 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20180502_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='teater',
            name='age',
            field=models.IntegerField(default=25, verbose_name='\u6559\u5e08\u5e74\u9f84'),
        ),
    ]
