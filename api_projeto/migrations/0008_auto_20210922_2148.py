# Generated by Django 3.2.7 on 2021-09-23 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_projeto', '0007_auto_20210922_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicao',
            name='temperatura',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='medicao',
            name='umidade',
            field=models.FloatField(),
        ),
    ]
