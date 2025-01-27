from django.urls import path
from .views import regFlow, logFlow, ProfileLook

urlpatterns = [
    # (Clean) 경로 이름과 뷰 이름이 일치하지 않아 혼란
    path('register/', regFlow, name='register_user'),
    path('login/', logFlow, name='login_user'),
    path('profile/', ProfileLook.as_view(), name='prof_look'),
]
