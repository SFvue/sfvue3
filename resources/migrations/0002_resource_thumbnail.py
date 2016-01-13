# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=b'resources/%Y/%m/%d/', blank=True),
        ),
    ]
