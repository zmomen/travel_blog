# Generated by Django 2.0.4 on 2018-04-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20180425_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
