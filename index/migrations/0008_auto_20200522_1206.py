# Generated by Django 3.0.6 on 2020-05-22 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20200522_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attempt',
            old_name='timestamp',
            new_name='submission_timestamp',
        ),
    ]