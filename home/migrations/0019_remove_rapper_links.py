# Generated by Django 4.1.7 on 2023-04-19 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_rapper_social_github_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rapper',
            name='links',
        ),
    ]
