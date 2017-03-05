# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_auto_20170302_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='studente',
            name='squadra',
            field=models.ForeignKey(to='demo.Squadra', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gara',
            name='stato',
            field=models.CharField(max_length=1, default='D', choices=[('D', 'Completare Domande'), ('P', 'Pronta'), ('I', 'In Corso'), ('C', 'Completata')], editable=False),
        ),
    ]
