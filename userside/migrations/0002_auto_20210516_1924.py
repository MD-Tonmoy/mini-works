# Generated by Django 3.0.14 on 2021-05-16 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='email',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
    ]