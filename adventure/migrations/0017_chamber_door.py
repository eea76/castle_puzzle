# Generated by Django 3.0.6 on 2020-05-27 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0016_auto_20200527_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamber',
            name='door',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adventure.Door'),
        ),
    ]
