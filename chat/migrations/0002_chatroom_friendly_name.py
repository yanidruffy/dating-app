# Generated by Django 5.1.6 on 2025-02-17 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
