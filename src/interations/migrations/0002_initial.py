# Generated by Django 4.1.9 on 2023-09-05 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('microblogs', '0001_initial'),
        ('interations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='view',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='microblogs.microblogpost'),
        ),
    ]
