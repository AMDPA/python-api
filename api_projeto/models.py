from django.db import models
import datetime

# Create your models here.


class Medicao(models.Model):
	uuid = models.TextField(max_length = 1000, default = "", blank = True) 
	estacao = models.TextField(max_length=256, default = "", blank = True)
	hora = models.BigIntegerField(default = 0)
	dht11_temperatura = models.FloatField(default = 0)
	dht11_umidade = models.FloatField(default = 0)
	dht11_indiceCalor = models.FloatField(default = 0)
	cjmcu101_luminosidade = models.FloatField(default = 0)
	soilmoisture_umidade = models.FloatField(default = 0)
	ccs811_co2 = models.FloatField(default = 0)
	ccs811_etvoc = models.FloatField(default = 0)
	mq8_hidrogenio =  models.FloatField(default = 0)
	mhrd_chuva = models.TextField(max_length = 1000, default = '', blank = True)
	a18b20_temperatura= models.FloatField(default = 0)
	ph4502c_ph= models.FloatField(default = 0)
	mhz19b_co2 =  models.FloatField(default = 0)
	def __str__(self):
		return f'{self.hora}'
