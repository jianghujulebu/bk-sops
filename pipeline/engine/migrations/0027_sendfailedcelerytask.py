# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-07-01 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("engine", "0026_auto_20200610_1442"),
    ]

    operations = [
        migrations.CreateModel(
            name="SendFailedCeleryTask",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=1024, verbose_name="任务名")),
                ("kwargs", models.TextField(verbose_name="任务参数")),
                (
                    "type",
                    models.IntegerField(
                        choices=[
                            (0, "empty"),
                            (1, "process"),
                            (2, "node"),
                            (3, "schedule"),
                        ],
                        verbose_name="任务类型",
                    ),
                ),
                ("extra_kwargs", models.TextField(verbose_name="额外参数")),
                ("exec_trace", models.TextField(verbose_name="错误信息")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
            ],
        ),
    ]
