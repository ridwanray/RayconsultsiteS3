# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180908_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productname',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('titleitemname', models.CharField(max_length=120, null=True)),
            ],
        ),
    ]
