from django.urls import path
from .views import AutoDetail

urlpatterns = [
    path('<slug:slug>', AutoDetail.as_view(), name='autos_detail')
]