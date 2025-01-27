from django.http import JsonResponse
from django.views import View
from django.db.models import Q
from .models import QueryLog
from .serializers import QLogSer

def doSearchAll(request):
    # (Clean) 함수명, 변수명 모호, 주석 없음
    keyw = request.GET.get('q', '')
    if keyw:
        queries = QueryLog.objects.filter(kw__icontains=keyw).order_by('-ctime')
    else:
        queries = QueryLog.objects.all().order_by('-ctime')

    data = QLogSer(queries, many=True).data
    return JsonResponse({'results': data}, safe=False)

class SearchFilter(View):
    def get(self, request):
        # (Clean) 변수명 축약, 주석 없음
        k = request.GET.get('q', '')
        d = request.GET.get('date', '')

        qs = QueryLog.objects.all()
        if k:
            qs = qs.filter(kw__icontains=k)
        if d:
            qs = qs.filter(ctime__date=d)

        data = QLogSer(qs, many=True).data
        return JsonResponse({'filtered': data}, safe=False)

    # (Clean) 다른 HTTP 메서드(POST, PUT 등) 부재
