# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_productname'),
        ('cart', '0008_auto_20181112_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='productnamereal',
            field=models.ForeignKey(unique=True, blank=True, null=True, to='shop.Productname'),
        ),
    ]
