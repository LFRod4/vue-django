from django.urls import path, include
from .views import restricted, TweetAPIView, AllTweets

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('restricted/', restricted),
    path('create/', TweetAPIView.as_view(), name="tweet-create"),
    path('list/<int:author>', AllTweets.as_view(), name="tweet-list")
]
