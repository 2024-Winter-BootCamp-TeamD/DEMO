from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View
from .models import usrModel, profOne
from .serializers import uData, pData

def doReg(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pw = request.POST.get('password')
        newu = usrModel.objects.create_user(username=un, password=pw)
        profOne.objects.create(usr=newu)
        return redirect('log_in')
    return render(request, 'register.html')

def doLog(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pw = request.POST.get('password')
        found = authenticate(request, username=un, password=pw)
        if found:
            login(request, found)
            return redirect('prf_data')
    return render(request, 'login.html')

class ProfData(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'err': 'No auth'}, status=403)

        data = uData(request.user).data
        return JsonResponse({'user': data}, safe=False)

    # (Clean) 다른 메서드(POST, PUT) 등은 전혀 없음
# 넹