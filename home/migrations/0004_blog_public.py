# Generated by Django 2.0.4 on 2018-04-19 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180418_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
