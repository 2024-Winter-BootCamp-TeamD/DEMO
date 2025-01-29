from django.urls import path
from .views import doAllS, Flt


urlpatterns = [
    path('all/', doAllS, name='search_all'),
    path('flt/', Flt.as_view(), name='filter_data'),
]
