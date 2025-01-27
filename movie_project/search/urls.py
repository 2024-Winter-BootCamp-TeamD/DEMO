from django.urls import path
from .views import doSearchAll, SearchFilter

urlpatterns = [
    path('all/', doSearchAll, name='search_all'),
    path('filter/', SearchFilter.as_view(), name='filter_search'),
]
