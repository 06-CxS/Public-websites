from django.shortcuts import render


def Uretimindex(request):
    return render(request,"Uretim/Uretindex.html")


def UretimBolumleri(request):
    return render(request,"Uretim/Bolumler.html")


def SiparisTakip(request):
    return render(request,"Uretim/SiparisTakip.html")
    
