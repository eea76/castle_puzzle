# Generated by Django 3.0.6 on 2020-05-27 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0011_answer_ultimate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer',
            new_name='Child',
        ),
        migrations.RenameModel(
            old_name='Prompt',
            new_name='Parent',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='preceding_answer',
            new_name='last_child',
        ),
    ]