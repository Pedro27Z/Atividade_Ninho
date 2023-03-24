import requests


def consulta_cnpj(cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":cnpj,"plugin":"RF"}
    response = requests.request("GET",url,params=querystring)

    resp = response.json()
    nome = resp['nome']
    logradouro = resp['logradouro']
    numero = resp['numero']
    complemento = resp['complemento']
    bairro = resp['bairro']
    municipio = resp['municipio']
    uf = resp['uf']
    cep = resp['cep']
    telefone = resp['telefone']
    email = resp['email']

    return (nome, logradouro, numero, complemento, bairro, municipio, uf, cep, telefone, email)

