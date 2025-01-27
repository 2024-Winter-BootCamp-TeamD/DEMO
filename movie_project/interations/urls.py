from django.urls import path
from .views import doLike, doBookmark, FollowView

urlpatterns = [
    # (Clean) 함수/클래스 이름이 모호
    path('like/', doLike, name='like_content'),
    path('bookmark/', doBookmark, name='bookmark_content'),
    path('follow/', FollowView.as_view(), name='follow_user'),
]
