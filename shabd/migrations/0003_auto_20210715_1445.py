# Generated by Django 3.2.5 on 2021-07-15 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shabd', '0002_auto_20210713_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='famous_ghazals',
            name='shayari',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ghazals_home',
            name='shayari',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='new_ghazals',
            name='shayari',
            field=models.TextField(blank=True, null=True),
        ),
    ]