# Generated by Django 3.0.5 on 2020-05-05 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloxov', '0011_auto_20200504_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postava',
            name='vyska',
            field=models.IntegerField(default=180, null=True, verbose_name='Výška'),
        ),
    ]
