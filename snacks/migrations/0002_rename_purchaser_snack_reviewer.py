# Generated by Django 4.1.5 on 2023-01-25 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snack',
            old_name='purchaser',
            new_name='reviewer',
        ),
    ]
