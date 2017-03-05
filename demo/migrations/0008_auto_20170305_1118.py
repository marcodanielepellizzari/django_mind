# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_auto_20170305_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gara',
            name='squadre',
            field=models.ManyToManyField(to='demo.Squadra', null=True),
        ),
    ]
