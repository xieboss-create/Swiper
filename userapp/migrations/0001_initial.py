# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-02-03 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dating_gender', models.CharField(choices=[('male', '男性'), ('female', '女性')], default='female', max_length=10, verbose_name='匹配的性别')),
                ('dating_location', models.CharField(choices=[('北京', '北京'), ('上海', '上海'), ('深圳', '深圳'), ('成都', '成都'), ('西安', '西安'), ('武汉', '武汉'), ('沈阳', '沈阳')], default='北京', max_length=20, verbose_name='目标城市')),
                ('min_distance', models.IntegerField(default=1, verbose_name='最小查找范围')),
                ('max_distance', models.IntegerField(default=10, verbose_name='最大查找范围')),
                ('min_dating_age', models.IntegerField(default=18, verbose_name='最小交友年龄')),
                ('max_dating_age', models.IntegerField(default=50, verbose_name='最大交友年龄')),
                ('vibration', models.BooleanField(default=True, verbose_name='是否开启震动')),
                ('only_matched', models.BooleanField(default=True, verbose_name='不让未匹配的人看我的相册')),
                ('auto_play', models.BooleanField(default=True, verbose_name='自动播放视频')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenum', models.CharField(max_length=16, unique=True, verbose_name='手机号')),
                ('nickname', models.CharField(max_length=32, verbose_name='昵称')),
                ('gender', models.CharField(choices=[('male', '男性'), ('female', '女性')], default='male', max_length=10, verbose_name='性别')),
                ('birthday', models.DateField(default='1990-01-01', verbose_name='生日')),
                ('avatar', models.CharField(max_length=256, verbose_name='个人形象的URL')),
                ('location', models.CharField(choices=[('北京', '北京'), ('上海', '上海'), ('深圳', '深圳'), ('成都', '成都'), ('西安', '西安'), ('武汉', '武汉'), ('沈阳', '沈阳')], default='北京', max_length=20, verbose_name='常居地')),
            ],
        ),
    ]
