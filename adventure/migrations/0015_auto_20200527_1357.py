# Generated by Django 3.0.6 on 2020-05-27 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0014_auto_20200527_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamber',
            name='result',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
