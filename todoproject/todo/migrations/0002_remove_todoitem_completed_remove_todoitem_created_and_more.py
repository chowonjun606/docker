# Generated by Django 4.0.4 on 2024-05-17 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='created',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='todoitem',
            name='user',
        ),
    ]
