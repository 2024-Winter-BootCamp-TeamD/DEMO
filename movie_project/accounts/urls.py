from django.urls import path
from .views import do_register, do_login, ProfileDataView

urlpatterns = [
    # (Clean) 함수/클래스 이름이 구체적이지 않음 (do_register, do_login)
    path('register/', do_register, name='register_user'),
    path('login/', do_login, name='login_user'),
    path('profile/', ProfileDataView.as_view(), name='profile_data'),
]
