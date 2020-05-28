# Generated by Django 3.0.6 on 2020-05-27 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0013_auto_20200527_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chamber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField(blank=True, null=True)),
                ('count', models.CharField(blank=True, default='0', max_length=1000, null=True)),
                ('door', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adventure.Door')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('count', models.CharField(blank=True, default='0', max_length=1000, null=True)),
                ('belonging_chamber', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='belonging_chamber', to='adventure.Chamber')),
                ('next_chamber', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adventure.Chamber')),
            ],
        ),
        migrations.RemoveField(
            model_name='parent',
            name='door',
        ),
        migrations.RemoveField(
            model_name='result',
            name='last_child',
        ),
        migrations.DeleteModel(
            name='Child',
        ),
        migrations.DeleteModel(
            name='Parent',
        ),
        migrations.AddField(
            model_name='result',
            name='last_option',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adventure.Option'),
        ),
    ]
