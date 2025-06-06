import ft
import requests


def novo_cliente():
    url = "http://10.135.232.31:5000/novo_cliente"

    post_cliente = {
        "nome": input_nome.value,
        "cpf": input_cpf.value,
        'telefone': input_telef.value,
        'endereco': input_ender.value
    }

    verificar_cliente = requests.post(url, json=post_cliente)

    if verificar_cliente.status_code == 201:
        dados_post_cliente = verificar_cliente.json()
        return dados_post_cliente

    else:
        f"Error: {verificar_cliente.status_code}"
        return {
            "erro": novo_cliente.json()
        }

novo_cliente()

    input_nome = ft.TextField(label="Nome",hint_text="Digite seu nome")
    input_cpf = ft.TextField(label="CPF",hint_text="Digite seu cpf")
    input_telef = ft.TextField(label="Telefone",hint_text="Digite seu telefone")
    input_ender = ft.TextField(label="Endereço",hint_text="Digite seu endereço")