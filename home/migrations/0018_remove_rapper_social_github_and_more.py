# Generated by Django 4.1.7 on 2023-04-19 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_recommandations_competition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rapper',
            name='social_github',
        ),
        migrations.RemoveField(
            model_name='rapper',
            name='social_linkedin',
        ),
    ]
