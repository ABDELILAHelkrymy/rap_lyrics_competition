# Generated by Django 4.1.7 on 2023-04-17 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0005_competitionentry'),
        ('home', '0016_alter_recommandations_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommandations',
            name='competition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommendations_com', to='competition.competitionentry'),
        ),
    ]
