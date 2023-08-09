import xmltodict # faz a leitura xml e transforma para dicionário
import os  # manusear arquivos
import pandas as pd
import json

def pegar_infor(arquivo):
    print(f"Pegou as informações {arquivo}")
    with open(f'nfs/{arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        print(json.dumps(dic_arquivo, index=4)) # melhorar a visualização dos arquivos, onde index dará 4 espaços entre os prints


lista_arquivos = os.listdir("nfs")

for arquivo in lista_arquivos:
    pegar_infor(arquivo)

