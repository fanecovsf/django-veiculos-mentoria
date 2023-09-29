from django.urls import path

from app_cad_veiculos.views import VeiculoAPI, VeiculoDetailsAPI

urlpatterns = [
    path('veiculos/', VeiculoAPI.as_view(), name='veiculos_all'),
    path('veiculos/<id_veiculo>', VeiculoDetailsAPI.as_view(), name='veiculos_details'),
]

