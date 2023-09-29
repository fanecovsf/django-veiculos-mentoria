
from django.urls import path, include

urlpatterns = [
    path('cad_veiculos/', include('app_cad_veiculos.urls'), name='veiculos'),
]
