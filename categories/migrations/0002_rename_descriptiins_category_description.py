# Generated by Django 5.1.3 on 2024-11-12 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='descriptiins',
            new_name='description',
        ),
    ]
