# Generated by Django 2.2.7 on 2019-12-20 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapi', '0005_alldata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alldata',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='alldata',
            name='followed_id',
        ),
        migrations.RemoveField(
            model_name='alldata',
            name='username',
        ),
    ]
