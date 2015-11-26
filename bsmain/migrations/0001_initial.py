# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mbean',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('m_b_name', models.CharField(max_length=50)),
                ('m_b_unitprice', models.DecimalField(max_digits=8, decimal_places=1)),
                ('m_b_weight', models.DecimalField(max_digits=8, decimal_places=1)),
                ('m_b_minimum', models.DecimalField(max_digits=8, decimal_places=1)),
                ('m_b_e_date', models.DateTimeField()),
                ('m_b_d_date', models.DateTimeField()),
                ('m_b_c_date', models.DateTimeField(auto_now_add=True)),
                ('m_b_deleted', models.BooleanField(default=False)),
                ('m_b_remark', models.CharField(max_length=300, blank=True)),
                ('m_p_phone', models.CharField(max_length=10)),
                ('m_p_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('o_b_set', models.DecimalField(max_digits=5, decimal_places=1)),
                ('o_b_remark', models.CharField(max_length=300, blank=True)),
                ('o_p_phone', models.CharField(max_length=10)),
                ('o_p_address', models.CharField(max_length=100)),
                ('o_b_c_date', models.DateTimeField(auto_now_add=True)),
                ('o_b_deleted', models.BooleanField(default=False)),
                ('o_m_b', models.ForeignKey(to='bsmain.Mbean')),
                ('o_p_name', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
