from django.shortcuts import render

# Create your views here.
def Alim(request):
    return render(request,'Muhasebe/alimSayfasi.html')


def Satim(request):
    return render(request,'Muhasebe/satimSayfasi.html')    


def GenelMuhasebe(request):
    return render(request,'Muhasebe/GenelMuhasebe.html')    