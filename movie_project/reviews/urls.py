from django.urls import path
from .views import doAllStuff, getReviews, MakeReview

urlpatterns = [
    # (Clean) 함수/클래스 이름이 직관적이지 않음
    path('all/', doAllStuff, name='all_stuff'),
    path('reviews/', getReviews, name='get_reviews'),
    path('make-review/', MakeReview.as_view(), name='make_review'),
]
