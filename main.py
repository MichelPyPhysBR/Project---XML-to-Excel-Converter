import xmltodict  # faz a leitura xml e transforma para dicionário
import os  # manusear arquivos
import pandas as pd


def pegar_infor(arquivo):
    print(f"Pegou as informações {arquivo}")
    with open(f'nfs/{arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)

        if "NFe" in dic_arquivo:
            infor_nf = dic_arquivo["NFe"]["infNFe"]
        else:
            infor_nf = dic_arquivo["nfeProc"]["NFe"]["infNFe"]
        numero_nota = infor_nf["@Id"]
        empresa_emissora = infor_nf["emit"]["xNome"]
        nome_cliente = infor_nf["dest"]["xNome"]
        endereco = infor_nf["dest"]["enderDest"]
        if "vol" in dic_arquivo:
            peso = infor_nf["transp"]["vol"]["pesoB"]
        else:
            peso = "Não informado!"
        print(numero_nota, empresa_emissora, nome_cliente, endereco, peso, sep="\n")


lista_arquivos = os.listdir("nfs")

for arquivo in lista_arquivos:
    pegar_infor(arquivo)
    # break



