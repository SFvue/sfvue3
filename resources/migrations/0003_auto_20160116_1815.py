# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_resource_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='thumbnail',
            new_name='image_thumbnail',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='thumbnail',
            new_name='image_thumbnail',
        ),
        migrations.AddField(
            model_name='resource',
            name='video_embed',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='video_upload',
            field=models.FileField(null=True, upload_to=b'resources/%Y/%m/%d/', blank=True),
        ),
    ]
