from app_cad_veiculos.models import Veiculo


class VeiculoServices:


    @staticmethod
    def get(id_veiculo):
        try:
            veiculo = Veiculo.objects.get(id_veiculo=id_veiculo)
            return veiculo
        except:
            return None
        
    @staticmethod
    def query_all():
        veiculos = Veiculo.objects.all()
        return veiculos
