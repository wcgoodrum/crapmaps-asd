# Generated by Django 4.2.6 on 2023-11-04 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crap_maps', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='approved_status',
            field=models.BooleanField(default=False),
        ),
    ]
