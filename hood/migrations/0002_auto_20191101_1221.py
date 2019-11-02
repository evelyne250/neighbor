# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-01 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True)),
                ('post', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='neighbourhood',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='hood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood_post', to='hood.NeighbourHood'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to='hood.Profile'),
        ),
    ]