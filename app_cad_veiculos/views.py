from django.shortcuts import render
from .models import Veiculo

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app_cad_veiculos.services import VeiculoServices
from app_cad_veiculos.serializers import VeiculoSerializer


class VeiculoAPI(APIView):


    def get(self, request):
        veiculos = VeiculoServices.query_all()
        serializer = VeiculoSerializer(veiculos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = VeiculoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VeiculoDetailsAPI(APIView):


    def get(self, request, id_veiculo):
        veiculo = VeiculoServices.get(id_veiculo)

        if veiculo:
            serializer = VeiculoSerializer(veiculo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'erro':'veiculo nao existe'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, id_veiculo):
        veiculo = VeiculoServices.get(id_veiculo)

        if veiculo:
            veiculo.delete()
            return Response(data={'delete':'veiculo deletado'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data={'erro':'veiculo nao existe'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, id_veiculo):
        data = request.data
        veiculo = VeiculoServices.get(id_veiculo)

        if veiculo:
            serializer = VeiculoSerializer(instance=veiculo, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'erro':'veiculo nao existe'}, status=status.HTTP_404_NOT_FOUND) 
        