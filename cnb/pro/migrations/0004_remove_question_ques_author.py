# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0003_auto_20150417_0456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='ques_author',
        ),
    ]
