from django.shortcuts import render


def ReportHome(request):
    return render(request,'Raporlar/DayReport.html')


def test(request):
    return render(request,'Raporlar/WeekReports.html')



def MuhasebeGunluk(request):
    return render(request,"Raporlar/MuhasebeDays.html")

def ProjeRaporlar(request):
    return render (request,"Raporlar/ProjeRapor.html")


def Fabrika(request):
    return render(request,"Raporlar/FabrikaRapor.html")


#************************URETİM **********************************

def UretimGunlukRapor(request):
    return render(request,"Raporlar/Uretim/U_gun.html")

def UretimHaftalıkRapor(request):
    return render(request,"Raporlar/Uretim/U_hafta.html")

def UretimAylikRapor(request):
    return render(request,"Raporlar/Uretim/U_Ay.html")


#**********************MUHASEBE **********************************


def MuhasebeGunlukRapor(request):
    return render(request,"Raporlar/Muhasebe/M_gun.html")

def MuhasebeHaftalıkRapor(request):
    return render(request,"Raporlar/Muhasebe/M_hafta.html")

def MuhasebeAylikRapor(request):
    return render(request,"Raporlar/Muhasebe/M_Ay.html")
