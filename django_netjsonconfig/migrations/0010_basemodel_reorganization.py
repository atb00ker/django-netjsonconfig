# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 14:52

import collections
import jsonfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0009_openvpn_data_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='template',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='vpn',
            name='config',
            field=jsonfield.fields.JSONField(default=dict, dump_kwargs={'ensure_ascii': False, 'indent': 4}, help_text='configuration in NetJSON DeviceConfiguration format', load_kwargs={'object_pairs_hook': collections.OrderedDict}, verbose_name='configuration'),
        ),
    ]
