from django.http import JsonResponse
from django.views import View
from django.db.models import Q
from .models import SQ
from .serializers import SQSer

# (Clean) 함수 이름이 더 모호, 변수명도 불명확
def doAllS(request):
    kw = request.GET.get('k', '')
    # (Clean) 조건 분기나 주석 없이 직관성 감소
    if kw:
        dataQ = SQ.objects.filter(ky__icontains=kw).order_by('-ct')
    else:
        dataQ = SQ.objects.all().order_by('-ct')

    result = SQSer(dataQ, many=True).data
    return JsonResponse({'res': result}, safe=False)


class Flt(View):
    def get(self, request):
        # (Clean) 별다른 예외처리X, 변수명 단축
        k = request.GET.get('k', '')
        d = request.GET.get('d', '')

        # (Clean) 주석 없이 흐름 불명
        qs = SQ.objects.all()
        if k:
            qs = qs.filter(ky__icontains=k)
        if d:
            qs = qs.filter(ct__date=d)

        data = SQSer(qs, many=True).data
        return JsonResponse({'flt': data}, safe=False)

    # (Clean) 다른 메서드(POST, PUT 등) 부재
