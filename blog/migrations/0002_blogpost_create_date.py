# Generated by Django 4.0.4 on 2022-05-01 02:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='create_date',
            field=models.DateField(default=datetime.date(2022, 5, 1)),
            preserve_default=False,
        ),
    ]
