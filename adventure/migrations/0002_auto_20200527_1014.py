# Generated by Django 3.0.6 on 2020-05-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='count',
            field=models.CharField(blank=True, default='0', max_length=1000, null=True),
        ),
    ]