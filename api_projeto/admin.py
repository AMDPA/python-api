from django.contrib import admin
from api_projeto.models import Medicao

class Medicoes(admin.ModelAdmin):
	list_display = ["uuid","hora","dht11_temperatura","dht11_umidade","dht11_indiceCalor","cjmcu101_luminosidade","soilmoisture_umidade","ccs811_co2","ccs811_etvoc","mq8_hidrogenio","mhrd_chuva","a18b20_temperatura","ph4502c_ph","mhz19b_co2"]
	list_display_links = ["uuid","hora"]
	search_fields = ["uuid","hora",]
# Register your models here.


admin.site.register(Medicao, Medicoes)