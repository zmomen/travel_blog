# Generated by Django 2.0.4 on 2018-04-18 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180415_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='title', max_length=200),
            preserve_default=False,
        ),
    ]