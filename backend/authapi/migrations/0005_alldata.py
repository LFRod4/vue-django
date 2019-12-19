# Generated by Django 2.2.7 on 2019-12-18 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapi', '0004_follower'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=100)),
                ('tweet_text', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField()),
                ('followed_id', models.IntegerField()),
            ],
        ),
    ]
