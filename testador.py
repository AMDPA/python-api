import requests

url = 'http://api-amacpa.herokuapp.com/relatorio/122/26784669957'

payload = "{\"1634168416\": {\"hora\": 1634168416, \"dht11_temperatura\": 0, \"dht11_umidade\": 0, \"dht11_indiceCalor\": 0, \"cjmcu101_luminosidade\": 0, \"soilmoisture_umidade\": 0, \"ccs811_co2\": 0, \"ccs811_etvoc\": 0, \"mq8_hidrogenio\": 0, \"mhrd_chuva\": \"\", \"a18b20_temperatura\": 0, \"ph4502c_ph\": 0, \"mhz19b_co2\": 0}}"
headers = {
  'User': 'C7ikBZwIoJTafDIWzoBzMWSeK8m1',
  'Email':'danilofritas54@gmail.com',
  'Estacao': '0',
  'Content-Type': 'application/json',
  'Cookie': 'csrftoken=EhOhOad3jYVbOEJ4C83Ry5Kfx90qE3OiclNqIGOt4XtwL25yqvhr6kiYqvMtt0Sc',
  
}
payload_list = []
payload_list.append(payload)
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
print(response.text)



#COMO POSTAR VÁRIOS EM POST_MAIOR:
# [
# {"1234":{
#         "soilmoisture_umidade": 0.0,
#         "dht11_umidade": 0.0,
#         "ccs811_etvoc": 0.0,
#         "cjmcu101_luminosidade": 0.0,
#         "mq8_hidrogenio": 0.0,
#         "dht11_temperatura": 0.0,
#         "estacao": "2",
#         "ph4502c_ph": 0.0,
#         "mhrd_chuva": "",
#         "ccs811_co2": 0.0,
#         "hora": 1234,
#         "a18b20_temperatura": 0.0,
#         "mhz19b_co2": 0.0,
#         "dht11_indiceCalor": 0.0,
#         "uuid": "bbb"
#     }},
# {"12345":{
#         "soilmoisture_umidade": 0.0,
#         "dht11_umidade": 0.0,
#         "ccs811_etvoc": 0.0,
#         "cjmcu101_luminosidade": 0.0,
#         "mq8_hidrogenio": 0.0,
#         "dht11_temperatura": 0.0,
#         "estacao": "2",
#         "ph4502c_ph": 0.0,
#         "mhrd_chuva": "",
#         "ccs811_co2": 0.0,
#         "hora": 12345,
#         "a18b20_temperatura": 0.0,
#         "mhz19b_co2": 0.0,
#         "dht11_indiceCalor": 0.0,
#         "uuid": "bbb"
#     }},
# {"123456":{
#         "soilmoisture_umidade": 0.0,
#         "dht11_umidade": 0.0,
#         "ccs811_etvoc": 0.0,
#         "cjmcu101_luminosidade": 0.0,
#         "mq8_hidrogenio": 0.0,
#         "dht11_temperatura": 0.0,
#         "estacao": "2",
#         "ph4502c_ph": 0.0,
#         "mhrd_chuva": "",
#         "ccs811_co2": 0.0,
#         "hora": 123456,
#         "a18b20_temperatura": 0.0,
#         "mhz19b_co2": 0.0,
#         "dht11_indiceCalor": 0.0,
#         "uuid": "bbb"
#     }},
# {"1234567":{
#         "soilmoisture_umidade": 0.0,
#         "dht11_umidade": 0.0,
#         "ccs811_etvoc": 0.0,
#         "cjmcu101_luminosidade": 0.0,
#         "mq8_hidrogenio": 0.0,
#         "dht11_temperatura": 0.0,
#         "estacao": "2",
#         "ph4502c_ph": 0.0,
#         "mhrd_chuva": "",
#         "ccs811_co2": 0.0,
#         "hora": 1234567,
#         "a18b20_temperatura": 0.0,
#         "mhz19b_co2": 0.0,
#         "dht11_indiceCalor": 0.0,
#         "uuid": "bbb"
#     }},
# {"12345678":{
#         "soilmoisture_umidade": 0.0,
#         "dht11_umidade": 0.0,
#         "ccs811_etvoc": 0.0,
#         "cjmcu101_luminosidade": 0.0,
#         "mq8_hidrogenio": 0.0,
#         "dht11_temperatura": 0.0,
#         "estacao": "2",
#         "ph4502c_ph": 0.0,
#         "mhrd_chuva": "",
#         "ccs811_co2": 0.0,
#         "hora": 12345678,
#         "a18b20_temperatura": 0.0,
#         "mhz19b_co2": 0.0,
#         "dht11_indiceCalor": 0.0,
#         "uuid": "bbb"
#     }},
# {"123456789":{
#         "soilmoisture_umidade": 0.0,
#         "dht11_umidade": 0.0,
#         "ccs811_etvoc": 0.0,
#         "cjmcu101_luminosidade": 0.0,
#         "mq8_hidrogenio": 0.0,
#         "dht11_temperatura": 0.0,
#         "estacao": "2",
#         "ph4502c_ph": 0.0,
#         "mhrd_chuva": "",
#         "ccs811_co2": 0.0,
#         "hora": 123456789,
#         "a18b20_temperatura": 0.0,
#         "mhz19b_co2": 0.0,
#         "dht11_indiceCalor": 0.0,
#         "uuid": "bbb"
#     }}
# ]