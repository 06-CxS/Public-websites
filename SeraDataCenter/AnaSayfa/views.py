from django.shortcuts import render
import pyodbc as deneme



def Home(request):

    server = 'localhost' 
    database = 'master' 
    username = 'omer' 
    password = 'Net123' 
    cnxn = deneme.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)



    cursor = cnxn.cursor()
   
    result = cursor.execute('SELECT * FROM il')
    data = result.fetchall();


    return render(request,'AnaSayfa/index.html',{"tanim":data})
