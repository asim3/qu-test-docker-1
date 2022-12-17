# Generated by Django 3.2 on 2022-12-17 11:26

from django.db import migrations


def my_custom_data(apps, schema_editor):
    # We can't import the model directly. We use the historical version.
    User = apps.get_model('auth', 'User')
    User.objects.create_superuser("admin", password="admin")


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile_is_email_verified'),
    ]

    operations = [
        migrations.RunPython(my_custom_data),
    ]