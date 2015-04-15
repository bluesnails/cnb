# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('answer_id', models.AutoField(serialize=False, primary_key=True)),
                ('answer_text', models.TextField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain', models.CharField(max_length=32)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='choice',
            fields=[
                ('choice_id', models.AutoField(serialize=False, primary_key=True)),
                ('choice_text', models.CharField(max_length=256)),
                ('choice_ans', models.BooleanField(default=False)),
                ('choice_tags', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('ques_id', models.AutoField(serialize=False, primary_key=True)),
                ('ques_text', models.TextField(max_length=1024)),
                ('ques_created', models.DateField(auto_now_add=True)),
                ('ques_dscore', models.IntegerField()),
                ('ques_bloom', models.CharField(max_length=3, choices=[(b'KNO', b'Knowledge'), (b'COM', b'Comprehension'), (b'APP', b'Application')])),
                ('ques_subject', models.CharField(max_length=3, choices=[(b'ECO', b'Economics'), (b'HIS', b'History'), (b'GEO', b'Geography'), (b'CLR', b'Culture and Arts'), (b'ENV', b'Environment and Ecology'), (b'SCI', b'Science and Technology'), (b'CRN', b'Current Affairs')])),
                ('ques_type', models.CharField(max_length=1, choices=[(b'0', b'Matching'), (b'1', b'Single Choice Correct'), (b'2', b'Two Choices Correct'), (b'3', b'Three Choices Correct'), (b'4', b'Four Choices Correct')])),
                ('ques_flags', models.CharField(max_length=16)),
                ('ques_author', models.ForeignKey(to='pro.author')),
            ],
        ),
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('quiz_id', models.AutoField(serialize=False, primary_key=True)),
                ('quiz_title', models.CharField(max_length=32)),
                ('quiz_doc', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='tagcon',
            fields=[
                ('tagcon_id', models.AutoField(serialize=False, primary_key=True)),
                ('tagcon_ques', models.ForeignKey(to='pro.question')),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('tags_id', models.AutoField(serialize=False, primary_key=True)),
                ('tags_text', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='tagcon',
            name='tagcon_tags',
            field=models.ForeignKey(to='pro.tags'),
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_ques',
            field=models.ForeignKey(to='pro.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_ques',
            field=models.ForeignKey(to='pro.question'),
        ),
    ]
