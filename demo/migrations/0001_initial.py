# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domande',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('num', models.SmallIntegerField(verbose_name='Numero')),
                ('risp', models.SmallIntegerField(verbose_name='Risposta corretta')),
            ],
        ),
        migrations.CreateModel(
            name='Gare',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('titolo', models.CharField(unique=True, max_length=30, verbose_name='Titolo')),
                ('tipo', models.CharField(choices=[('M', 'Math'), ('F', 'Fisica')], max_length=1)),
                ('num_domande', models.SmallIntegerField()),
                ('inizio_previsto', models.DateTimeField(blank=True, null=True)),
                ('inizio', models.DateTimeField(blank=True, null=True)),
                ('durata', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Risposte',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('risposta', models.SmallIntegerField(verbose_name='Risposta Inserita')),
                ('domanda', models.ForeignKey(to='demo.Domande')),
                ('gara', models.ForeignKey(to='demo.Gare')),
            ],
        ),
        migrations.CreateModel(
            name='Squadre',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=30)),
                ('des_squadra', models.TextField(blank=True, null=True, verbose_name='DescrizioneSquadra')),
                ('gare', models.ManyToManyField(to='demo.Gare')),
            ],
        ),
        migrations.AddField(
            model_name='risposte',
            name='squadra',
            field=models.ForeignKey(to='demo.Squadre'),
        ),
        migrations.AddField(
            model_name='domande',
            name='gara',
            field=models.ForeignKey(to='demo.Gare'),
        ),
    ]
