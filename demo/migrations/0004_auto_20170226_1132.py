# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20170226_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risposte',
            name='studente',
            field=models.ForeignKey(to='demo.Studenti'),
        ),
    ]
