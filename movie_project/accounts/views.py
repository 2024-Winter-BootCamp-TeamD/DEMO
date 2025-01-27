from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View
from .models import basicUser, ProfOne
from .serializers import baseUserData, profData
from django.db.models import F


# (Clean) 이름이 모호하고, 한 함수에서 회원 생성+프로필 생성+리다이렉트 처리
def regFlow(request):
    if request.method == 'POST':
        usr = request.POST.get('username')
        pwd = request.POST.get('password')
        # (Clean) 단일 책임 원칙 위배: 여기서 사용자 생성, 프로필도 생성
        # (Optimize) create_user()로 단일 쿼리
        new_user = basicUser.objects.create_user(username=usr, password=pwd)
        ProfOne.objects.create(user=new_user)
        return redirect('login_user')
    return render(request, 'register.html')


def logFlow(request):
    if request.method == 'POST':
        usern = request.POST.get('username')
        pasw = request.POST.get('password')
        found = authenticate(request, username=usern, password=pasw)
        if found:
            login(request, found)
            return redirect('prof_look')
    return render(request, 'login.html')


# (Clean) 클래스 이름이 단순, GET만 처리 -> 다른 HTTP 메서드 확장 어려움
class ProfileLook(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Not authenticated'}, status=403)

        # (Optimize) select_related로 DB 쿼리 최소화
        usr = basicUser.objects.select_related('profile').get(id=request.user.id)
        # (Clean) 직렬화는 사용하지만, 예외 처리나 주석 부족
        data = baseUserData(usr).data
        return JsonResponse({'user_data': data}, safe=False)

    # (Clean) PUT, PATCH, DELETE 등 다른 메서드 부재
