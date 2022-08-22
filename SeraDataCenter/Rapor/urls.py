from django.urls import path
from . import views


urlpatterns = [

    path("",views.ReportHome,name="RaporAnaSayfa"),
    path("GunlukMuhasebe",views.MuhasebeGunluk,name="GunlukMuhasebe"),

    path("week/",views.test,name="WeekReports")


]