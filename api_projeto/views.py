from api_projeto.models import Medicao
from api_projeto.serializer import MedicaoSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import datetime
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, storage

from .generate import create_pdf

cred = credentials.Certificate('firebase_json_config/amacpa-ifes-firebase-adminsdk-je7ue-d98bbac888.json')
firebase_admin.initialize_app(cred, {'storageBucket': "amacpa-ifes.appspot.com"})
db = firestore.client()

# Funções criadas por Danilo

def get_interval_data(usuario,data_inicio, data_fim):
	dados = get_all_from_firebase()

	dados_table = []
	dados_table2 = []
	dados_table3 = []
	dados_table4 = []

	for i in dados:
		if i.get("uuid") == usuario and i.get("hora") >= int(data_inicio) and i.get("hora")<=int(data_fim):
			dados_table.append([milis_to_data(i.get("hora")), milis_to_hora(i.get("hora")),i.get("cjmcu101_luminosidade"),i.get("mq8_hidrogenio"), i.get("a18b20_temperatura")])
			dados_table2.append([ milis_to_data(i.get("hora")), milis_to_hora(i.get("hora")),i.get("dht11_temperatura"), i.get("dht11_umidade"), i.get("dht11_indiceCalor")])
			dados_table3.append([milis_to_data(i.get("hora")), milis_to_hora(i.get("hora")),i.get("soilmoisture_umidade"),i.get("ccs811_co2"),i.get("ccs811_etvoc")])
			dados_table4.append([milis_to_data(i.get("hora")), milis_to_hora(i.get("hora")),i.get("mhrd_chuva"),i.get("ph4502c_ph"),i.get("mhz19b_co2") ])
	return [dados_table, dados_table2, dados_table3, dados_table4]


def milis_to_data(tempo_milis):
	date = datetime.datetime.fromtimestamp(int(tempo_milis))
	data = date.strftime('%Y-%m-%d')
	return str(data)

def milis_to_hora(tempo_milis):
	date = datetime.datetime.fromtimestamp(int(tempo_milis))			
	hora = date.strftime('%H:%M:%S')
	return str(hora)
   
def get_all_from_firebase():
	database = firestore.client()
	dados = []
	col = database.collections()
	for c in col:
		subcolec = c.document(u"Dados").collections()
		for dado in subcolec:
			for d in dado.stream():
				dados.append(d.to_dict()) 
	return dados

def get_data_to_relatorio(usuario, hora_inicial, hora_final):
	database = firestore.client()
	dados = []
	doc_ref = database.collection(f'{usuario}')
	query_ref = doc_ref.where(u"Dados", u"<=", f'{milis_to_data(hora_final)}')
	query_ref = query_ref.where(u"Dados", u">=", f'{milis_to_data(hora_inicial)}').stream()
	for d in query_ref:
		dados.append(d.get().to_dict())

	return dados

	
@api_view(["GET"])
def relatorios(request, data_inicio, data_fim):
	usuario_id = request.headers.get("User")
	
	create_pdf(request.headers.get("Email"), hora_inicial=f'{milis_to_data(data_inicio)} às {milis_to_hora(data_inicio)}', hora_final=f'{milis_to_data(data_fim)} às {milis_to_hora(data_fim)}', tb = get_interval_data(usuario_id, data_inicio, data_fim))
	
	try:
		fileNameUp = f"{usuario_id}/{milis_to_data(data_inicio)}_{str(milis_to_hora(data_inicio)).replace(':','-')}/{milis_to_data(data_fim)}_{str(milis_to_hora(data_fim)).replace(':','-')}/relatorio.pdf"
		fileName = f"arquivos_storage/relatorio.pdf"
		bucket = storage.bucket()
		blob = bucket.blob(fileNameUp)
		blob.upload_from_filename(fileName)
		# Opt : if you want to make public access from the URL
		blob.make_public()
		os.remove(f"arquivos_storage/relatorio.pdf")
		return Response(blob.public_url)

	except Exception:
		return Response(f"Falha no upload do arquivo")


@api_view(["GET", "POST"])
def medicoes(request):
	dados = dict(request.data)
	print("DADOS", dados)
	for i in dados:
		print(i)

	if request.method == 'GET':
		dados_do_firebase = get_all_from_firebase()
		return Response(dados_do_firebase)

	elif request.method == 'POST':
		chave = list(dados)[0]
		dados = dados[chave]
		dados["uuid"] = request.headers.get("User")
		dados["estacao"] = request.headers.get("Estacao")
		serializer = MedicaoSerializer(data = dados)
		if serializer.is_valid():
			hora = milis_to_hora(serializer.data.get("hora"))
			data = milis_to_data(serializer.data.get("hora"))

			doc_ref = db.collection(f'{dict(serializer.data).get("uuid")}').document(f'Dados').collection(f'{data}').document(f'{hora}')
			doc_ref.set(dict(serializer.data), merge= True)

			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def posta_muitos(request):

	dados = request.data
	print("DADOS",dados)
	if request.method == 'GET':
		dados_do_firebase = get_all_from_firebase()
		return Response(dados_do_firebase)

	elif request.method == 'POST':
		dados2 =[]
		for i in list(dados):
			chave = list(dict(i))[0]
			i = dict(i)[chave]
			i["uuid"] = request.headers.get('User')
			i["estacao"] = request.headers.get('Estacao')
			dados2.append(i)
		
		serializer = MedicaoSerializer(data = dados2, many = True)

		if serializer.is_valid():

			for serializer2 in serializer.data:
				data = milis_to_data(serializer2.get("hora"))
				hora = milis_to_hora(serializer2.get("hora"))
				doc_ref = db.collection(f'{serializer2.get("uuid")}').document(f'Dados').collection(f'{data}').document(f'{hora}')
				doc_ref.set(serializer2)

			return Response("Registros postados com sucesso", status = status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
