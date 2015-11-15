# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsontest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailySteps',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=8)),
                ('steps', models.IntegerField(default=0)),
            ],
        ),
    ]
