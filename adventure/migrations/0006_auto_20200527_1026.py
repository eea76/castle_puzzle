# Generated by Django 3.0.6 on 2020-05-27 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0005_auto_20200527_1024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='description',
            new_name='text',
        ),
    ]