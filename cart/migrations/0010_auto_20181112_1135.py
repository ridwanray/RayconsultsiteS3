# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_cartitem_productnamereal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='productnamereal',
            field=models.ForeignKey(blank=True, null=True, to='shop.Productname'),
        ),
    ]
