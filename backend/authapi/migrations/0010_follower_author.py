# Generated by Django 2.2.7 on 2020-01-06 04:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapi', '0009_user_about_me'),
    ]

    operations = [
        migrations.AddField(
            model_name='follower',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
