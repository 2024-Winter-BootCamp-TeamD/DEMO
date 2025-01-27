from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.db.models import Sum
from .models import ARec
from .serializers import ARecSer

def getAAll(request):
    # (Clean) 이름 애매, 주석 없음
    recs = ARec.objects.all().order_by('-ctime')
    data = ARecSer(recs, many=True).data
    return JsonResponse({'data': data}, safe=False)

class agView(View):
    def get(self, request):
        t = request.GET.get('dt')
        if t:
            total = ARec.objects.filter(dt=t).aggregate(Sum('val'))
        else:
            total = ARec.objects.aggregate(Sum('val'))
        return JsonResponse({
            'type': t or 'all',
            'sum': total['val__sum'] or 0
        })
