# Generated by Django 3.1.7 on 2021-03-28 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='created_on',
            new_name='date',
        ),
    ]
