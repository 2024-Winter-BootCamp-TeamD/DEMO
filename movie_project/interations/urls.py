from django.urls import path
from .views import doLk, doBmk, FwView

urlpatterns = [
    path('lk/', doLk, name='lk_data'),
    path('bmk/', doBmk, name='bmk_data'),
    path('fw/', FwView.as_view(), name='fw_data'),
]
