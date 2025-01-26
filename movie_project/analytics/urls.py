from django.urls import path
from .views import getAllAnalytics, AggregatedDataView

urlpatterns = [
    # (Clean) 함수 이름이 모호 (getAllAnalytics)
    path('all/', getAllAnalytics, name='all_analytics'),
    path('aggregated/', AggregatedDataView.as_view(), name='aggregated_data'),
]
