# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_auto_20170228_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gara',
            name='inizio_previsto',
        ),
        migrations.AddField(
            model_name='gara',
            name='stato',
            field=models.CharField(editable=False, choices=[('D', 'Completare Domande'), ('P', 'Pronta'), ('I', 'In Corso'), ('C', 'Completata')], default='I', max_length=1),
        ),
    ]
