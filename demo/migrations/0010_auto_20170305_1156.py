# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0009_auto_20170305_1120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studente',
            options={'verbose_name_plural': 'Studenti'},
        ),
        migrations.AlterField(
            model_name='gara',
            name='durata',
            field=models.DurationField(default=datetime.timedelta(0, 7200)),
        ),
        migrations.AlterField(
            model_name='gara',
            name='stato',
            field=models.CharField(max_length=1, editable=False, default='D', choices=[('D', 'Definire domande'), ('P', 'Pronta'), ('I', 'In Corso'), ('C', 'Completata')]),
        ),
    ]
