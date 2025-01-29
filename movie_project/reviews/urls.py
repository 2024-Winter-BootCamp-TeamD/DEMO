from django.urls import path
from .views import doAll, getRvs, mkRv


urlpatterns = [
    path('all/', doAll, name='all_data'),
    path('rvs/', getRvs, name='get_rvs'),
    path('mk/', mkRv.as_view(), name='make_rv'),
]
