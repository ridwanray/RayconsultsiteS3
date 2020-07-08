# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_productname'),
        ('cart', '0011_auto_20181112_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='itemcategory',
            field=models.ForeignKey(blank=True, null=True, to='shop.Category'),
        ),
    ]
