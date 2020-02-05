from django.urls import path, include
from .views import TweetAPIView, Followers, AllData, UserProfiles, DeleteFollower

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('create/', TweetAPIView.as_view(), name="tweet-create"),
    path('list/<int:author>', TweetAPIView.as_view(), name="tweet-list"),
    path('followers/<int:follower_id>', Followers.as_view(), name="followers"),
    path('follow/', Followers.as_view(), name="follow"),
    path('alldata/', AllData.as_view(), name="alldata"),
    path('userprofiles/', UserProfiles.as_view(), name="user-profiles"),
    path('delete/', DeleteFollower.as_view(), name="delete-follower")
]
