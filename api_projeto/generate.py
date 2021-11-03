
import os
def create_pdf(email_usuario, hora_inicial, hora_final, tb):
	tb1 = tb[0]
	tb2 = tb[1]
	tb3 = tb[2]
	tb4 = tb[3]
	#nao mudar
	head = '<!DOCTYPE html><html lang="pt-br"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Relatorio Personalizado</title><link rel="stylesheet" href="css/normalize.css"><link rel="stylesheet" href="css/style.css"><link rel="stylesheet" href="css/p.css"><script src="js/modernizr.min.js"></script></head>'

	#nao mudar
	body1 = '<body> <div class="divC"> <img class="imgC" src="img/logo.svg" alt="logo SoloTech"> <h4>SoloTech <br><i>Análise Simplificada</i></h4> </div> <h2 class="title1">Resumo de medições por período</h2>'

	#Adicionar data e  horas iniciais
	usuario = f'<p class="title1">Requerente: {email_usuario}</p>'
	data = f'<p class="title1">De {hora_inicial} / Até {hora_final}</p>'

	#nao mudar
	tableh = '<table class="tg"> <thead> <tr> <th class="tg-1wig">DATA</th> <th class="tg-1wig">HORA</th> <th class="tg-1wig">LUMINOSIDADE</th> <th class="tg-1wig">HIDROGENIO</th> <th class="tg-1wig">TEMPERATURA SOLO</th> </tr> </thead> <tbody>'

	#colocar num for e preencher com as informações da tabela
	table1 = ''
	for i in tb1:
		tableb = f'<tr> <td class="tg-baqh">{i[0]}</td> <td class="tg-baqh">{i[1]}</td> <td class="tg-baqh">{i[2]}%</td> <td class="tg-baqh">{i[3]}ppm</td> <td class="tg-baqh">{i[4]}ºC</td> </tr>'
		table1+= tableb
	#nao mudar
	tablef = '</tbody> </table>'

	tt = '<br>'
	#---------------------------------TABLE 2
	#nao mudar
	tableh2 = '<table class="tg"> <thead> <tr> <th class="tg-1wig">DATA</th> <th class="tg-1wig">HORA</th> <th class="tg-1wig">TEMPERATURA AMBIENTE</th> <th class="tg-1wig">UMIDADE AMBIENTE</th> <th class="tg-1wig"> ÍNDICE DE CALOR AMBIENTE</th> </tr> </thead> <tbody>'

	#colocar num for e preencher com as informações da tabela
	table2 = ''
	for i in tb2:
		tableb = f'<tr> <td class="tg-baqh">{i[0]}</td> <td class="tg-baqh">{i[1]}</td> <td class="tg-baqh">{i[2]}%</td> <td class="tg-baqh">{i[3]}ppm</td> <td class="tg-baqh">{i[4]}ºC</td> </tr>'
		table2+= tableb
	#nao mudar
	tablef = '</tbody> </table>'

	tt = '<br>'
	#-------------------------------TABLE 3
	#nao mudar
	tableh3 = '<table class="tg"> <thead> <tr> <th class="tg-1wig">DATA</th> <th class="tg-1wig">HORA</th> <th class="tg-1wig">UMIDADE SOLO</th> <th class="tg-1wig">CO2 CCS811</th> <th class="tg-1wig">ETVOC</th> </tr> </thead> <tbody>'

	#colocar num for e preencher com as informações da tabela
	table3 = ''
	for i in tb3:
		tableb = f'<tr> <td class="tg-baqh">{i[0]}</td> <td class="tg-baqh">{i[1]}</td> <td class="tg-baqh">{i[2]}%</td> <td class="tg-baqh">{i[3]}ppm</td> <td class="tg-baqh">{i[4]}ºC</td> </tr>'
		table3+= tableb
	#nao mudar
	tablef = '</tbody> </table>'

	tt = '<br>'
	#----------------------------TABLE 4
	#nao mudar
	tableh4 = '<table class="tg"> <thead> <tr> <th class="tg-1wig">DATA</th> <th class="tg-1wig">HORA</th> <th class="tg-1wig">CHUVA</th> <th class="tg-1wig">PH SOLO</th> <th class="tg-1wig">CO2 MHZ19B</th> </tr> </thead> <tbody>'

	#colocar num for e preencher com as informações da tabela
	table4 = ''
	for i in tb4:
		tableb = f'<tr> <td class="tg-baqh">{i[0]}</td> <td class="tg-baqh">{i[1]}</td> <td class="tg-baqh">{i[2]}%</td> <td class="tg-baqh">{i[3]}ppm</td> <td class="tg-baqh">{i[4]}ºC</td> </tr>'
		table4+= tableb
	#nao mudar
	tablef = '</tbody> </table>'

	tt = '<br>'
	#repetir tableh, tableb, tablef para novas tabelas. Mudando seus atributos.
	#ao fim de uma tabela adicionar tt

	#nao mudar
	bodyf = '</body> </html>'
	tb1 = tableh + table1 + tablef + tt
	tb2 = tableh2 + table2 + tablef + tt
	tb3 = tableh3 + table3 + tablef + tt
	tb4 = tableh4 + table4 + tablef + tt
	finalData = head + body1 + usuario + data + tb1 + tb2 + tb3 + tb4
	f = open("pdf_amdpa/data.html", "w", encoding='UTF-8')
	f.write(finalData)
	f.close()
	
	os.system('php pdf_amdpa/generate.php')

	# o programa cria um arquivo data.html e 
	# executa o script generate.php que cria um arquivo relatorio.pdf
	# na raiz do projeto.
