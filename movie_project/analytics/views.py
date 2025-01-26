from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.db.models import Sum
from .models import AnalyticsRecord
from .serializers import AnalyticsDataSerializer


# (Clean) 함수 이름이 모호, 단일 책임 분리 미흡
# (Optimize) 쿼리 한 번에 전부 로드하여 오버헤드 감소
def getAllAnalytics(request):
    records = AnalyticsRecord.objects.all().order_by('-created_at')
    serializer = AnalyticsDataSerializer(records, many=True)
    return JsonResponse({'analytics': serializer.data}, safe=False)


# (Clean) 클래스 이름이 어느 정도 직관적이지만, GET만 지원
# (Optimize) DB aggregate로 데이터를 한 번에 계산
class AggregatedDataView(View):
    def get(self, request):
        data_type = request.GET.get('type', None)
        if data_type:
            total_value = AnalyticsRecord.objects.filter(data_type=data_type).aggregate(Sum('value'))
        else:
            total_value = AnalyticsRecord.objects.aggregate(Sum('value'))

        # (Optimize) 한 번의 쿼리로 sum을 계산
        return JsonResponse({
            'data_type': data_type or 'all',
            'total_value': total_value['value__sum'] or 0
        })
