# Generated by Django 4.1.7 on 2023-04-16 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0002_alter_competition_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]