from django.http import JsonResponse
from django.views import View
from django.db.models import Q
from .models import SQ
from .serializers import SQSer


def doAllS(request):
    kw = request.GET.get('k', '')
    if kw:
        dataQ = SQ.objects.filter(ky__icontains=kw).order_by('-ct')
    else:
        dataQ = SQ.objects.all().order_by('-ct')

    result = SQSer(dataQ, many=True).data
    return JsonResponse({'res': result}, safe=False)


class Flt(View):
    def get(self, request):
        k = request.GET.get('k', '')
        d = request.GET.get('d', '')

        qs = SQ.objects.all()
        if k:
            qs = qs.filter(ky__icontains=k)
        if d:
            qs = qs.filter(ct__date=d)

        data = SQSer(qs, many=True).data
        return JsonResponse({'flt': data}, safe=False)



