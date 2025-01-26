from django.urls import path
from .views import searchAll, FilterSearchView

urlpatterns = [
    # (Clean) 함수/클래스 이름이 직관적이지 않음
    path('all/', searchAll, name='search_all'),
    path('filter/', FilterSearchView.as_view(), name='filter_search'),
]
