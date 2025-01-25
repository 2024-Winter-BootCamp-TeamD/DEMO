from django.http import JsonResponse
from django.views import View
from django.db.models import Q
from .models import SearchQuery
from .serializers import SearchQuerySerializer


# (Clean) 함수 이름이 모호, docstring이나 주석 없음
# (Optimize) DB 접근 최소화, 필요한 검색만 수행
def searchAll(request):
    keyword = request.GET.get('q', '')
    # (Optimize) 키워드가 있으면 필터, 없으면 전체
    if keyword:
        queries = SearchQuery.objects.filter(keyword__icontains=keyword).order_by('-created_at')
    else:
        queries = SearchQuery.objects.all().order_by('-created_at')

    data = SearchQuerySerializer(queries, many=True).data
    return JsonResponse({'results': data}, safe=False)


# (Clean) 클래스 이름이 의도는 드러내지만, post/get 등 확장성 모호
# (Optimize) 필터링 시 Q 객체 사용 -> 조건 간소화
class FilterSearchView(View):
    def get(self, request):
        kw = request.GET.get('q', '')
        date_str = request.GET.get('date', '')

        qs = SearchQuery.objects.all()

        if kw:
            qs = qs.filter(keyword__icontains=kw)
        if date_str:
            qs = qs.filter(created_at__date=date_str)

        # (Optimize) 필요한 데이터만 직렬화
        data = SearchQuerySerializer(qs, many=True).data
        return JsonResponse({'filtered': data}, safe=False)
