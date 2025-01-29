from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import get_user_model
from .models import Lk, Bmk, Fw
from .serializers import LkSer, BmkSer, FwSer


User = get_user_model()

def doLk(request):
    if request.method == 'POST':
        uid = request.POST.get('usr')
        ctp = request.POST.get('ctype')
        oid = request.POST.get('oid')
        usr_obj = get_object_or_404(User, id=uid)
        newlk = Lk.objects.create(usr=usr_obj, ctype=ctp, oid=oid)
        data = LkSer(newlk).data
        return JsonResponse({'lk': data}, status=201)
    return JsonResponse({'err': 'Only POST'}, status=400)

def doBmk(request):
    if request.method == 'POST':
        uid = request.POST.get('usr')
        link = request.POST.get('link')
        note = request.POST.get('note', '')
        usr_obj = get_object_or_404(User, id=uid)
        bm = Bmk.objects.create(usr=usr_obj, link=link, nt=note)
        data = BmkSer(bm).data
        return JsonResponse({'bmk': data}, status=201)
    return JsonResponse({'err': 'Only POST'}, status=400)

class FwView(View):
    def get(self, request):
        uid = request.GET.get('uid')
        if uid:
            fw_list = Fw.objects.filter(fr_id=uid)
        else:
            fw_list = Fw.objects.all()
        data = FwSer(fw_list, many=True).data
        return JsonResponse({'fw': data}, safe=False)

    def post(self, request):
        frid = request.POST.get('fr')
        toid = request.POST.get('to')
        fr_obj = get_object_or_404(User, id=frid)
        to_obj = get_object_or_404(User, id=toid)
        fw_obj = Fw.objects.create(fr=fr_obj, to=to_obj)
        return JsonResponse({'fw_id': fw_obj.id}, status=201)
