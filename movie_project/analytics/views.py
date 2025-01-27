from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.db.models import Sum
from .models import AnalyticsRec
from .serializers import RecDataSerializer


def getAnaAll(request):
    # (Clean) 함수명 모호, 주석 불충분
    recs = AnalyticsRec.objects.all().order_by('-created')
    data = RecDataSerializer(recs, many=True).data
    return JsonResponse({'analytics': data}, safe=False)


class AggView(View):
    # (Clean) 클래스 이름과 메서드가 구체적이지 않음
    def get(self, request):
        t = request.GET.get('type', None)
        if t:
            total_value = AnalyticsRec.objects.filter(dtype=t).aggregate(Sum('val'))
        else:
            total_value = AnalyticsRec.objects.aggregate(Sum('val'))

        return JsonResponse({
            'data_type': t or 'all',
            'total_value': total_value['val__sum'] or 0
        })
