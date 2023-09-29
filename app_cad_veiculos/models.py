from django.db import models

class Veiculo(models.Model):


    id_veiculo=models.AutoField(primary_key=True)
    modelo=models.CharField(max_length=100, blank=False, null=False)
    ano=models.IntegerField(blank=False, null=False)
    cor=models.CharField(max_length=100, blank=False, null=False)

    def __str__(self) -> str:
        return self.id_veiculo


