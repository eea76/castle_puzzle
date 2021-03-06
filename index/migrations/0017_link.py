# Generated by Django 3.0.6 on 2020-05-23 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_paintingperroom_href'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=1000, null=True)),
                ('href', models.CharField(blank=True, max_length=1000, null=True)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Room')),
            ],
        ),
    ]
