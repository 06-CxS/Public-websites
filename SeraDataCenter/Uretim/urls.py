from django.urls import path
from . import views


urlpatterns = [

    path("Takvim/",views.Uretimindex,name="UretimHome"),
    path("Bolumler/",views.UretimBolumleri,name="Bolumler"),

]