# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 21:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='stops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='images', width_field='width_field')),
                ('content', models.TextField(blank=True)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='tour',
            name='duration',
        ),
        migrations.AddField(
            model_name='tour',
            name='progress',
            field=models.TextField(default='0%'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tour',
            name='capacity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='cityname',
            field=models.CharField(blank=True, default='your city', max_length=120),
        ),
        migrations.AlterField(
            model_name='tour',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='country',
            field=models.CharField(blank=True, default='your country', max_length=120),
        ),
        migrations.AlterField(
            model_name='tour',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='slug',
            field=models.CharField(blank=True, default='', max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='state',
            field=models.CharField(blank=True, default='your state', max_length=120),
        ),
        migrations.AlterField(
            model_name='tour',
            name='title',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_intensity',
            field=models.CharField(blank=True, choices=[('sandals', 'Sandals'), ('regular shoes', 'Regular shoes'), ('gym shoes', 'Gym Shoes'), ('hiking shoes', 'Hiking shoes')], default='sandals', max_length=20),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_theme',
            field=models.CharField(blank=True, choices=[('art', 'Art'), ('activity', 'Activity'), ('historic', 'Historic'), ('generic', 'General')], default='generic', max_length=10),
        ),
        migrations.AddField(
            model_name='stops',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.Tour'),
        ),
    ]
