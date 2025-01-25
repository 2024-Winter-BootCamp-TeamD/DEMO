from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View
from .models import CustomUser, UserProfile
from .serializers import UserDataSerializer, UserProfileSerializer
from django.db.models import F


# (Clean) 한 함수 안에 회원가입 로직, 즉시 로그인, 오류 처리 등이 혼재
# (Optimize) DB 연산을 최소화하기 위해 get_or_create 등 고려
def do_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = CustomUser.objects.create_user(username=username, password=password)
        # (Optimize) create_user()로 단일 쿼리 처리
        UserProfile.objects.create(user=user)
        return redirect('login_user')
    return render(request, 'register.html')


def do_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # (Optimize) 페이지 리다이렉트 단순화
            return redirect('profile_data')
    return render(request, 'login.html')


# (Clean) 클래스 이름은 직관적이지만, GET만 처리하며 다른 메서드는 확장 어려울 수 있음
# (Optimize) select_related('profile')로 DB 호출 최적화
class ProfileDataView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Not authenticated'}, status=403)

        user = CustomUser.objects.select_related('profile').get(id=request.user.id)
        # (Optimize) Serializer 사용
        data = UserDataSerializer(user).data
        return JsonResponse({'user': data}, safe=False)

    # (Clean) PUT, PATCH, POST 등 다른 메서드 명시적 구현 없이, 수정 기능 등 부재
    # (Optimize) 여기에 코드를 추가한다면 DB 연산 고려 필요

