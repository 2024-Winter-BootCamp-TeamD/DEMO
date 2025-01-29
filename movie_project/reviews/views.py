from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.db.models import Avg, Count
from .models import Mv, Rv
from .serializers import MvData, RvData


def doAll(request):
    movies = Mv.objects.prefetch_related('rvs').annotate(
        avg_s=Avg('rvs__sc'),
        total_r=Count('rvs')
    ).order_by('-avg_s')

    data = MvData(movies, many=True).data
    return JsonResponse({'mv_list': data}, safe=False)

def getRvs(request):
    mid = request.GET.get('m', None)
    if mid:
        qs = Rv.objects.select_related('mv').filter(mv_id=mid)
    else:
        qs = Rv.objects.select_related('mv').all()

    ser = RvData(qs, many=True)
    return JsonResponse({'rvs': ser.data}, safe=False)

class mkRv(View):
    def post(self, request):
        m_id = request.POST.get('mv_id')
        ctt = request.POST.get('cont')
        s_val = request.POST.get('sc', 0)

        mv_obj = get_object_or_404(Mv, pk=m_id)
        new_rv = Rv.objects.create(mv=mv_obj, cont=ctt, sc=s_val)
        return JsonResponse({'rv_id': new_rv.id})
