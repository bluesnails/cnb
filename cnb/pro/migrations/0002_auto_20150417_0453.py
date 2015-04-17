# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_ans',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_choice',
            field=models.ForeignKey(to='pro.choice'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_tags',
            field=models.CharField(default=datetime.date(2015, 4, 17), max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='domain',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='question',
            name='ques_bloom',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='question',
            name='ques_subject',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='question',
            name='ques_text',
            field=models.TextField(default=b'What is the answer to life universe and everything', max_length=1024),
        ),
        migrations.AlterField(
            model_name='question',
            name='ques_type',
            field=models.CharField(max_length=1),
        ),
    ]
