from django.shortcuts import render


def ReportHome(request):
    return render(request,'Raporlar/DayReport.html')


def test(request):
    return render(request,'Raporlar/WeekReports.html')

def MuhasebeGunluk(request):
    return render(request,"Raporlar/MuhasebeDays.html")
