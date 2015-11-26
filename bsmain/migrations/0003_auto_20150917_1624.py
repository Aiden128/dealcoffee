# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bsmain', '0002_mbean_m_b_shipping_fee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('s_success', models.DecimalField(max_digits=8, decimal_places=1)),
                ('s_fail', models.DecimalField(max_digits=8, decimal_places=1)),
                ('s_comment', models.CharField(max_length=300, blank=True)),
                ('s_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='mbean',
            old_name='m_p_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='o_p_name',
            new_name='user',
        ),
    ]
