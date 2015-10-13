# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pickuplocation',
            name='geolocation',
        ),
        migrations.AlterField(
            model_name='pickuplocation',
            name='address',
            field=models.CharField(max_length=300),
        ),
    ]
