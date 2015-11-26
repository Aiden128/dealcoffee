# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bsmain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mbean',
            name='m_b_shipping_fee',
            field=models.DecimalField(default=0, max_digits=8, decimal_places=1),
        ),
    ]
