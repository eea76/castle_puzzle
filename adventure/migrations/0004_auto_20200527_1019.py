# Generated by Django 3.0.6 on 2020-05-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0003_auto_20200527_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
