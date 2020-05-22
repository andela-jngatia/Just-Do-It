# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-14 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bucketlist', '0003_auto_20160310_1934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bucketlist',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AlterModelOptions(
            name='bucketlistitem',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AlterField(
            model_name='bucketlistitem',
            name='bucketlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='bucketlist.Bucketlist'),
        ),
    ]
