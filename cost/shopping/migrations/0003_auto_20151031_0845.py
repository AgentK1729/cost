# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20151010_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='count',
            field=models.IntegerField(default=0, max_length=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='metric',
            field=models.CharField(default=b'items', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='useritem',
            name='count',
            field=models.IntegerField(default=0, max_length=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='useritem',
            name='metric',
            field=models.CharField(default=b'items', max_length=10),
            preserve_default=True,
        ),
    ]
