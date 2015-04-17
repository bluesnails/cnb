# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0002_auto_20150417_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_choice',
            field=models.ForeignKey(to='pro.choice'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='question',
            name='ques_text',
            field=models.TextField(max_length=1024),
        ),
    ]
