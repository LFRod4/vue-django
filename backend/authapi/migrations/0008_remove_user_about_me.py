# Generated by Django 2.2.7 on 2020-01-05 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapi', '0007_user_about_me'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='about_me',
        ),
    ]