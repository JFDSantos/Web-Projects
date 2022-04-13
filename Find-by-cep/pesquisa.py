from types import CellType
import requests, json

class Pesquisa:

    def __init__(self, cep):
        self.cep = cep

    def pesquisar(self):
        if self.cep.isnumeric():
            if len(self.cep) != 8:
                print("CEP inválido!")
            else:
                pass
        else:
            print("Só é permitido números!")
            exit()

        request = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/")
        dados_endereco = request.json()
        cidade = dados_endereco['localidade']
        estado = dados_endereco['uf']
        bairro = dados_endereco['bairro']
        rua = dados_endereco['logradouro']

        if 'erro' not in dados_endereco:
            print(f"\nCidade: {cidade}\nEstado: {estado}\nBairro: {bairro}\nRua: {rua}\n")
        else:
            print("CEP inválido!")