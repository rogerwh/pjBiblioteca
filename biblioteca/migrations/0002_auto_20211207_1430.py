# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='libro',
            name='fecha_publicacion',
            field=models.DateField(null=True, blank=True),
        ),
    ]
