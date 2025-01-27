from django.urls import path
from .views import getAnaAll, AggView

urlpatterns = [
    path('all/', getAnaAll, name='all_data'),
    path('agg/', AggView.as_view(), name='agg_data'),
]
