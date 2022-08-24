from django.shortcuts import render


def Uretimindex(request):
    return render(request,"Uretim/Uretindex.html")


def UretimBolumleri(request):
    return render(request,"Uretim/Bolumler.html")

