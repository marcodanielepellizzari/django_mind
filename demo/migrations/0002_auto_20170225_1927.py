# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jolly',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('domanda', models.ForeignKey(to='demo.Domande')),
                ('gara', models.ForeignKey(to='demo.Gare')),
                ('squadra', models.ForeignKey(to='demo.Squadre')),
            ],
            options={
                'permissions': (('capitano', 'Decide il Jolly'),),
            },
        ),
        migrations.AlterModelOptions(
            name='risposte',
            options={'permissions': (('studente', 'Inserisce Risposte'),)},
        ),
        migrations.AlterUniqueTogether(
            name='risposte',
            unique_together=set([('gara', 'squadra', 'domanda')]),
        ),
        migrations.AlterUniqueTogether(
            name='jolly',
            unique_together=set([('gara', 'squadra')]),
        ),
    ]
