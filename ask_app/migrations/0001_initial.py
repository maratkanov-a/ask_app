# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('answer_text', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(verbose_name='Дата ответа')),
                ('flag_of_true', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('label', models.CharField(max_length=20, default='Первый вопрос')),
                ('text', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(verbose_name='Дата вопроса')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=10)),
                ('reg_date', models.DateTimeField(verbose_name='Дата регистрации')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='text_author',
            field=models.ForeignKey(to='ask_app.Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='ans_author',
            field=models.ForeignKey(to='ask_app.Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='which_question',
            field=models.ForeignKey(to='ask_app.Question'),
            preserve_default=True,
        ),
    ]
