# Generated by Django 5.1.1 on 2024-09-16 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_maker', '0002_rename_event_manager_event_manager_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('scheduled', 'Scheduled'), ('cancelled', 'Cancelled'), ('ended', 'Ended')], default='scheduled', max_length=10),
        ),
    ]
