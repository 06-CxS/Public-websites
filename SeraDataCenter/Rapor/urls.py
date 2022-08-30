from django.urls import path
from . import views


urlpatterns = [

    path("Uretim/",views.ReportHome,name="RaporAnaSayfa"),
    path("Muhasebe/",views.MuhasebeGunluk,name="GunlukMuhasebe"),
    path("Proje/",views.ProjeRaporlar,name="Proje"),
    path("Fabrika/",views.Fabrika,name="Fabrika"),
    path("Haftalık/",views.test,name="WeekReports"),
    
    #*****************************************************

    path("Muhasebe/Gunluk",views.MuhasebeGunlukRapor,name="M_GunlukRapor"),
    path("Muhasebe/Haftalık",views.MuhasebeHaftalıkRapor,name="M_HaftalıkRapor"),
    path("Muhasebe/Aylık",views.MuhasebeAylikRapor,name="M_AylıkRapor"),
  

  
    path("Uretim/Gunluk",views.UretimGunlukRapor,name="U_GunlukRapor"),
    path("Uretim/Haftalık",views.UretimHaftalıkRapor,name="U_HaftalıkRapor"),
    path("Uretim/Aylık",views.UretimAylikRapor,name="U_AylıkRapor"),


]