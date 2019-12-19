from django.urls import path, include
from .views import TweetAPIView, AllTweets, Followers, AllData

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('create/', TweetAPIView.as_view(), name="tweet-create"),
    path('list/<int:author>', AllTweets.as_view(), name="tweet-list"),
    path('followers/', Followers.as_view(), name="followers"),
    path('alldata/', AllData.as_view(), name="alldata")
]
