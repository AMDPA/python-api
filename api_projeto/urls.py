from django.urls import path
from .views import medicoes, posta_muitos, relatorios

urlpatterns = [
	path("",medicoes),
	path('post_maior/', posta_muitos),
	path('relatorio/<str:data_inicio>/<str:data_fim>', relatorios),


]