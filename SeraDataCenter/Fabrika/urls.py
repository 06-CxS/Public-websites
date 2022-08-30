from django.urls import path
from . import views


urlpatterns = [

    path("",views.Takvim,name="Takvim")

]