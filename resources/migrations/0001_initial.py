# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(default=b'', max_length=255, blank=True)),
                ('url', models.URLField(unique=True)),
                ('help_text', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(default=b'', null=True, blank=True)),
                ('level', models.CharField(default=b'introductory', max_length=30, verbose_name=b'Level of depth', blank=True, choices=[(b'introductory', b'introductory'), (b'intermediate', b'intermediate'), (b'in-depth', b'in-depth')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('show', models.BooleanField(default=True)),
                ('rating_votes', models.PositiveIntegerField(default=0, editable=False, blank=True)),
                ('rating_score', models.IntegerField(default=0, editable=False, blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
                ('slug', models.SlugField(max_length=255)),
                ('help_text', models.CharField(max_length=255, null=True, blank=True)),
                ('color', models.CharField(default=b'purple', unique=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
                ('slug', models.SlugField(max_length=255)),
                ('help_text', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('thumbnail', models.ImageField(null=True, upload_to=b'topics/%Y/%m/%d/', blank=True)),
                ('official_website', models.URLField(null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='resource',
            name='resource_type',
            field=models.ForeignKey(default=2, to='resources.ResourceType'),
        ),
        migrations.AddField(
            model_name='resource',
            name='topics',
            field=models.ManyToManyField(to='resources.Topic'),
        ),
        migrations.AddField(
            model_name='featuredresource',
            name='resource',
            field=models.ForeignKey(to='resources.Resource'),
        ),
        migrations.AddField(
            model_name='featuredresource',
            name='resource_type',
            field=models.ForeignKey(to='resources.ResourceType'),
        ),
        migrations.AddField(
            model_name='featuredresource',
            name='topic',
            field=models.ForeignKey(to='resources.Topic'),
        ),
        migrations.AlterUniqueTogether(
            name='featuredresource',
            unique_together=set([('topic', 'resource_type')]),
        ),
    ]
