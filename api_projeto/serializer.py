from rest_framework import serializers
from api_projeto.models import Medicao

class MedicaoSerializer(serializers.ModelSerializer):
 	class Meta:
 		model = Medicao
 		fields = ["uuid","estacao","hora","dht11_temperatura","dht11_umidade","dht11_indiceCalor","cjmcu101_luminosidade","soilmoisture_umidade","ccs811_co2","ccs811_etvoc","mq8_hidrogenio","mhrd_chuva","a18b20_temperatura","ph4502c_ph","mhz19b_co2"]

