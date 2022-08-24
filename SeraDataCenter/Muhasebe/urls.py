from django.urls import path
from . import views


urlpatterns = [

    path("Alim/",views.Alim,name="M_Alim"),
    path("Satim/",views.Satim,name="M_Satim"),
    path("GenelMuhasebe/",views.GenelMuhasebe,name="GenelMuhasebe"),

]
