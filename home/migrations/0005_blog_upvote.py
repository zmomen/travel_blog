# Generated by Django 2.0.4 on 2018-04-23 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_blog_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
    ]