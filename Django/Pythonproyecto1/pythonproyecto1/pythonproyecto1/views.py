import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def saludo(request):
    return HttpResponse("Hola Django-Coder")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :)")

def diaDeHoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto =f"Hoy es día: <br> {dia}"
    return HttpResponse(documentoDeTexto)

def miNombreEs(self,nombre):
    documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"
    return HttpResponse(documentoDeTexto)

def probando_template(self):
    nom = "Pame"
    ap = "Pereyra"

    listaDeNotas = [2,4,6,8,10]

    diccionario = {"nombre": nom, "apellido": ap, "hoy": datetime.datetime.now, "notas": listaDeNotas}

    #miHtml = open("C:/Users/pamp/OneDrive - Chevron/Desktop/Python/Django/Pythonproyecto1/pythonproyecto1/pythonproyecto1/plantillas/template1.html")
    
   #plantilla = Template(miHtml.read())

    #miHtml.close()

    #miContexto = Context(diccionario)

    #documento = plantilla.render(miContexto)

    plantilla = loader.get_template("template1.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

