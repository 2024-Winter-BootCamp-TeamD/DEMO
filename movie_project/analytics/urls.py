from django.urls import path
from .views import getAAll, agView


urlpatterns = [
    path('all/', getAAll, name='an_all'),
    path('ag/', agView.as_view(), name='ag_data'),
]
