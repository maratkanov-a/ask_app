# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask_app', '0002_answer_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ans_author',
            field=models.ForeignKey(to='ask_app.User'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text_author',
            field=models.ForeignKey(to='ask_app.User'),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
