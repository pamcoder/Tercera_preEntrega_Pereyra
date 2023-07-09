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
    return HttpResponse('Vista Inicio')

def canalDe_Negocio(request):
    return HttpResponse('Vista CanalDe_Negocio')

def persona_aCargo(request):
    return HttpResponse('Vista Persona_aCargo')

def cliente_conDeuda(request):
    return HttpResponse('vista Cliente_conDeuda')
