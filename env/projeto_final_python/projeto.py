#imports das bibliotecas usadas
import requests
from faker import Faker 
import json

#"ativando" o faker - instanciando
fake = Faker('pt_BR')

#função para enviar os dados 
def enviar_dados_post(url, dados):
    # Enviar a requisição POST e obter a resposta
    response = requests.post(url, data=dados)
    return response

#função para processar a resposta da requisição
def processar_resposta(response):
    # Verificar se a requisição foi bem-sucedida (código 200 ou 201)
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    else:
        # Caso haja um erro na requisição, exibir o código de status
        print(f'Erro na requisição: {response.status_code}')
        return None

#função para salvar a resposta json em um arquivo txt
def save_json(dados_json, nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as file: 
            #pegar os dados, inserir no arquivo conforme a linha acima e idente no formato 4 
            json.dump(dados_json, file, indent=4)
            print(f"Resposta salva em '{nome_arquivo}'.")
    except IOError as e:
        print(f"Erro ao salvar o arquivo: {e}")

#dados para serem usados na criação de usuario
dados ={
    "username": fake.user_name(),
    "email": fake.email(),
    "password": fake.password(length=10),
    "phone": fake.cellphone_number(),
    "address": fake.address(),
    "cpf": fake.cpf()
}

#dados recuperados do dicionario acima para uso no login 
dados_login = {
    "email": dados["email"],
    "password": dados["password"]
}

#variaveis de url(endpoints) para uso nas funções onde seram feitas as requisições
url_create_user = "https://desafiopython.jogajuntoinstituto.org/api/users/"
url_login = "http://desafiopython.jogajuntoinstituto.org/api/users/login/"

#----------criação de usuario---------
#envia dados via post para criar usuario  e guarda a resposta na variável 
resposta_create = enviar_dados_post(url= url_create_user, dados= dados)

#processa a resposta do post feito acima
dados_json_create = processar_resposta(response= resposta_create)

#salvar resposta em um arquivo txt
save_json(dados_json= dados_json_create, nome_arquivo= 'resposta_create.txt')

#---------login de usuario--------------
#envia dados via post para fazer login 
resposta_login = enviar_dados_post(url= url_login, dados= dados_login)

#processa a resposta do post feito acima
dados_json__login = processar_resposta(response= resposta_login)

#salvar resposta em um arquivo json
save_json(dados_json= dados_json__login, nome_arquivo= 'resposta_login.txt')