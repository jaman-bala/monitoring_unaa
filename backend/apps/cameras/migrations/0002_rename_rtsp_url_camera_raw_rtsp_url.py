# Generated by Django 4.2.7 on 2023-11-29 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cameras', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='camera',
            old_name='rtsp_url',
            new_name='raw_rtsp_url',
        ),
    ]
