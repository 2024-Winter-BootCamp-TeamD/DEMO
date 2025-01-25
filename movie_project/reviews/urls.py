from django.urls import path
from .views import doAllStuff, getReviews, MakeReview

# (Clean 측면) 함수/클래스 이름이 직관적이지 않음
# (Optimize 측면) URL 패턴은 최소화하여 라우팅 오버헤드를 줄임
urlpatterns = [
    path('all/', doAllStuff, name='all_stuff'),
    path('reviews/', getReviews, name='get_reviews'),
    path('make-review/', MakeReview.as_view(), name='make_review'),
]