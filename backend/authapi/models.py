from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'
    about_me = models.CharField(
        max_length=500, default='You have not set your About Me')

    def get_username(self):
        return self.username


class Tweet(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tweets")
    tweet_text = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tweet_text


class Follower(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True,  related_name="follower")
    follower_id = models.IntegerField()
    followed_id = models.IntegerField()


class AllData(models.Model):
    profile_id = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tweet_text = models.CharField(max_length=200)

    def __str__(self):
        return self.profile_id
