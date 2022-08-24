from django.urls import path
from . import views


urlpatterns = [

    path("SevkiyatPlan/",views.SevkTarih,name="SevkTarih"),
    path("SevkiyatDurumu/",views.SevkDurum,name="SevkDurum"),
    path("GenelSevkiyat/",views.GenelSevkiyat,name="GenelSevkiyat"),

]