# Generated by Django 3.0.6 on 2020-05-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20200522_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='first_title_timestamp',
            field=models.DateTimeField(blank=True, db_index=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='attempt',
            name='second_title_timestamp',
            field=models.DateTimeField(blank=True, db_index=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='attempt',
            name='third_title_timestamp',
            field=models.DateTimeField(blank=True, db_index=True, default=None, null=True),
        ),
    ]