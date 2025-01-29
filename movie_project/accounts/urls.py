from django.urls import path
from .views import doReg, doLog, ProfData


urlpatterns = [
    path('reg/', doReg, name='reg_usr'),
    path('log/', doLog, name='log_in'),
    path('prof/', ProfData.as_view(), name='prf_data'),
]
