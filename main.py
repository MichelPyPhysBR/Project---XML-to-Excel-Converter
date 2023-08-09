import xmltodict # faz a leitura xml e transforma para dicionário
import os  # manusear arquivos
import pandas as pd

def pegar_infor(arquivo):
    print(f"Pegou as informações {arquivo}")
    with open(f'nfs/{arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        print(dic_arquivo)


lista_arquivos = os.listdir("nfs")

for arquivo in lista_arquivos:
    pegar_infor(arquivo)

