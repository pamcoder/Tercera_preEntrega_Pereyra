import datetime
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Django-Coder")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :)")

def diaDeHoy(request):
    dia = datetime.datetime.now()
    documentodeTexto = f"Hoy es día: <br> {dia}"
    return HttpResponse(documentodeTexto)

def miNombreEs(self, nombre):
    documentodeTexto = f"Mi nombre es: <br><br> {nombre}"
    return HttpResponse(documentodeTexto)

def probandoTemplate(self):
    miHtml = open("C:/Users/pamp/OneDrive - Chevron/Desktop/Python/Django/Pythonproyecto2/Proyecto2/Proyecto2/plantillas/template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()

    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

    
