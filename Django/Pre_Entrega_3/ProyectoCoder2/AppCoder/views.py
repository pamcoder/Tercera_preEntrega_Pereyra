from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Cliente

# Create your views here.
def cliente(self):
    cliente = Cliente(nombre="Pamela", apellido="Pereyra")
    cliente.save()

    documentoDeTexto= f'---->Cliente: {cliente.nombre} Apellido: {cliente.apellido}'

    return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cliente(request):
    return render(request, "AppCoder/cliente.html")

def canalDe_Negocio(request):
    return render(request, "AppCoder/canalDe_Negocio.html")

def persona_aCargo(request):
    return render(request, "AppCoder/persona_aCargo.html")

def cliente_conDeuda(request):
    return render(request, "AppCoder/cliente_conDeuda.html")
