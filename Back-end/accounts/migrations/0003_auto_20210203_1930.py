# Generated by Django 3.1.6 on 2021-02-03 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='last_activty',
            new_name='last_activity',
        ),
    ]
