from django.urls import path
from AppCoder import views


urlpatterns = [
    path (" ", views.inicio),
    path('cliente', views.cliente, name="Cliente"),
    path('CanalDe_Negocio', views.canalDe_Negocio),
    path('Persona_aCargo', views.persona_aCargo),
    path('Cliente_conDeuda', views.cliente_conDeuda),

    ]

