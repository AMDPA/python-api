# Generated by Django 3.2.7 on 2021-09-23 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_projeto', '0009_medicao_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicao',
            name='uuid',
            field=models.TextField(max_length=256),
        ),
    ]
