from django.shortcuts import render

# Create your views here.
def SevkTarih(request):
    return render(request,'Sevkiyat/SevkTarih.html')


def SevkDurum(request):
    return render(request,'Sevkiyat/SevkDurum.html')    


def GenelSevkiyat(request):
    return render(request,'Sevkiyat/GenelSevkiyat.html')    