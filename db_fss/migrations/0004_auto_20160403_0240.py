# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-03 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_fss', '0003_auto_20160403_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='matiere',
        ),
        migrations.AddField(
            model_name='student',
            name='matiere',
            field=models.ManyToManyField(to='db_fss.Matiere'),
        ),
    ]
