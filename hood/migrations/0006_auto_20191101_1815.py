# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-01 15:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0005_auto_20191101_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='neighbourhood',
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='health_tell',
            field=models.IntegerField(null=True, blank=True,),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='police_number',
            field=models.IntegerField(null=True, blank=True,),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='user',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='neighbor', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]