from urllib import response
import flet as ft
import requests
from flet import AppBar, Text, View, ElevatedButton
from flet.core.colors import Colors
from flet.core.types import FontWeight, MainAxisAlignment, CrossAxisAlignment


def main(page: ft.Page):
    page.title = "Oficina Mecânica"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667
    import requests

    # funçoes

    def novo_cliente():
        url = "http://10.135.235.37:5000/novo_cliente"

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

    def novo_veiculo():
        url = "http://10.135.235.37:5000/novo_veiculo"

        post_veiculo = {
            'marca': input_marca.value,
            'modelo': input_modelo.value,
            'placa': input_placa.value,
            'ano_fabri': input_ano.value,
            'id_cliente': input_id_cliente.value
        }

        verificar_veiculo  = requests.post(url, json=post_veiculo)

        if verificar_veiculo.status_code == 201:
            dados_post_veiculo = verificar_veiculo.json()
            return dados_post_veiculo

        else:
            f"Error: {verificar_veiculo.status_code}"
            return {
                "erro": novo_veiculo.json()
            }

    def novo_servico():
        url = "http://10.135.235.37:5000/novo_veiculo"

        post_servico = {
            "veiculo": input_veiculo.value,
            "id_veiculo": input_id_veiculo.value,
            "data_abertura": input_data.value,
            'descricao': input_descricao.value,
            'status': input_status.value,
            'valor': input_valor.value
        }

        verificar_orden = requests.post(url, json=post_servico)

        if verificar_orden.status_code == 200:
            dados_post_servico = verificar_orden.json()
            return dados_post_servico


        else:
            f"Error: {verificar_orden.status_code}"
            return {
                "erro": novo_servico.json()
            }



    def lista_clientes():
        url = f"http://10.135.235.37:5000/lista_clientes"

        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados_clientes = resposta.json()
            print(dados_clientes)
            return dados_clientes['lista_clientes']
        else:
            return resposta.json()

    def info_clientes(cliente):
        txt_nome.value = (f'Nome: {cliente["Nome"]}')
        txt_ender.value = (f'Endereço:{cliente["Endereco"]}')
        txt_cpf.value = (f'CPF:{cliente["CPF"]}')
        txt_telef.value = (f'Telefone:{cliente["telefone"]}')

        page.go("/decima")

    def exibir_clientes():
        lv.controls.clear()
        resultado_lista = lista_clientes()
        for cliente in resultado_lista:
            lv.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(f'{cliente["Nome"]}'),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons(ft.Icons.MORE_VERT),
                        items=[
                            ft.PopupMenuItem(text="Ver Dados", on_click=lambda _, c=cliente: info_clientes(c)),
                        ]
                    )
                )
            )



    def lista_veiculos():
        url = f"http://10.135.235.37:5000/lista_veiculos"

        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados_veiculos = resposta.json()
            print(dados_veiculos)
            return dados_veiculos
        else:
            return resposta.json()

    def info_veiculos(veiculo):
        txt_marca.value = (f'Marca: {veiculo["Marca"]}')
        txt_modelo.value = (f'Modelo:{veiculo["Modelo"]}')
        txt_placa.value = (f'Placa:{veiculo["placa"]}')
        txt_ano_fabri.value = (f'Ano de Fabricação:{veiculo["ano_fabri"]}')
        txt_id_cliente.value = (f'ID Cliente:{veiculo["id_cliente"]}')

        page.go("/onze")

    def exibir_veiculos():
        lv.controls.clear()
        resultado_lista = lista_veiculos()
        for veiculo in resultado_lista['lista_veiculos']:
            lv.controls.append(
                ft.ListTile(
                    title=ft.Text(f' Veiculo: {veiculo["placa"]}'),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons(ft.Icons.MORE_VERT),
                        items=[
                            ft.PopupMenuItem(text="Ver Dados", on_click=lambda _, v=veiculo: info_veiculos(v)),
                        ]
                    )
                )
            )



    def lista_servicos():
        url = f"http://10.135.235.37:5000/lista_servicos"

        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados_servicos = resposta.json()
            print(dados_servicos)
            return dados_servicos
        else:
            return resposta.json()

    def info_servico(servico):
        txt_veiculo.value = (f'Veiculo: {servico["veiculo"]}')
        txt_id_veiculo.value = (f'ID Veiculo:{servico["id_veiculo"]}')
        txt_data.value = (f'Data de entrada:{servico["data_abertura"]}')
        txt_descricao.value = (f'Descrição:{servico["descricao"]}')
        txt_status.value = (f'Status:{servico["status"]}')
        txt_valor.value = (f'Valor:{servico["valor"]}')
        txt_id_orden.value = (f'ID Orden:{servico["id_orden"]}')

        page.go("/doze")

    def exibir_ordens():
        lv.controls.clear()
        resultado_lista = lista_servicos()
        print(resultado_lista)
        for servico in resultado_lista['ordens_serviço']:
            lv.controls.append(
                ft.ListTile(
                    title=ft.Text(f'{servico["veiculo"]}'),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons(ft.Icons.MORE_VERT),
                        items=[
                            ft.PopupMenuItem(text="Ver mais informações", on_click=lambda _, s=servico: info_servico(s)),
                        ]
                    )
                )
            )



    def editar_clientar():
        global id_cliente_global
        print(id_cliente_global)
        url = f'http://10.135.232.20:5000/editar_livro/{id_cliente_global}'

        cliente_atualizado = {
            'nome': input_nome.value,
            'cpf': input_cpf.value,
            'telefone': input_telef.value,
            'endereco': input_ender.value,
        }

        response = requests.put(url, json=cliente_atualizado)

        if response.status_code == 200:
            page.go("/lista_clientes")
            page.update()
        else:
            print(f' Erro: {response.json()}')
            return {
                "error": response.json()
            }

    def popular_input_cliente(cliente):
        input_nome.value = nome['nome']
        input_cpf.value = cpf['cpf']
        input_telef.value = telefone['telefone']
        input_ender.value = endereco['endereco']

        global id_cliente_global
        id_cliente_global = cliente['id']

        page.go("/treze")



    def verificar_cliente():
        progress.visible = True
        page.update()
        if input_nome.value == "" or input_cpf.value == "" or input_telef.value == "" or input_ender.value == "":
            msg_error.content = ft.Text("Preencha todos os campos")
            page.overlay.append(msg_error)
            msg_error.open = True

        if input_cpf.value == "" or input_telef.value == "":
            msg_error.content = ft.Text("CPF ou Numero de Telefone Invalidos")
            page.overlay.append(msg_error)
            msg_error.open = True

        resposta = novo_cliente()
        if 'error' in resposta:
            msg_error.content = ft.Text(resposta("error"))
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()

        else:

            if "erro" in dados:
                page.overlay.append(msg_error)
                msg_error.open = True
            else:
                txt_cpf.value = dados["input_cpf"].value
                txt_telef.value = dados["input_telefone"].value
                page.go("/segunda")

                input_cep.value = ""
                msg_sucesso.open = ft.Text("CPF Valido")
                page.overlay.append(msg_sucesso)
                msg_sucesso.open = True





                novo_cliente()

        page.update()


    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/primeira",
                [
                    AppBar(title=Text(""), bgcolor=Colors.BLUE_100),
                    ft.Image(src="../Logo.png"),
                    ft.ElevatedButton(text="Cadastrar", color=Colors.WHITE, on_click=lambda _: page.go("/segunda")),
                    ft.ElevatedButton(text="Listas", color=Colors.WHITE,on_click=lambda _: page.go("/terceira")),
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                bgcolor=Colors.BLUE_100


            )
        )

        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Cadastros"), bgcolor=Colors.BLUE_300),
                        ft.ElevatedButton(text="Cadastrar Cliente", color=Colors.WHITE, on_click=lambda _: page.go("/quarta")),
                        ft.ElevatedButton(text="Cadastrar Veiculo", color=Colors.WHITE, on_click=lambda _: page.go("/quinta")),
                        ft.ElevatedButton(text="Cadastrar Serviço", color=Colors.WHITE, on_click=lambda _: page.go("/sexta")),
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    bgcolor=Colors.BLUE_100
                )
            )

        if page.route == "/terceira":
            page.views.append(
                View(
                    "/terceira",
                    [
                        AppBar(title=Text("Listas"), bgcolor=Colors.BLUE_300),
                        ft.ElevatedButton(text="Lista de Clientes", color=Colors.WHITE, on_click=lambda _: page.go("/setima")),
                        ft.ElevatedButton(text="Lista de Veiculos", color=Colors.WHITE, on_click=lambda _: page.go("/oitava")),
                        ft.ElevatedButton(text="Lista de Serviços", color=Colors.WHITE, on_click=lambda _: page.go("/nona")),
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    bgcolor=Colors.BLUE_100
                )
            )

        if page.route == "/quarta":
            page.views.append(
                View(
                    "/quarta",
                    [
                        AppBar(title=Text("Cadastro de Cliente"), bgcolor=Colors.BLUE_200),
                        Text(value=f"Preencha os campos com seus dados", color=Colors.BLACK),
                        input_nome,
                        input_cpf,
                        input_telef,
                        input_ender,
                        ElevatedButton(text="Cadastrar-se", color=Colors.WHITE, on_click=lambda _: verificar_cliente())
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    bgcolor=Colors.BLUE_100
                )
            )

        if page.route == "/quinta":
            page.views.append(
                View(
                    "/quinta",
                    [
                        AppBar(title=Text("Cadastro de Veiculos"), bgcolor=Colors.BLUE_200),
                        Text(value=f"Preencha os campos com os dados do veiculo", color=Colors.BLACK),
                        input_marca,
                        input_modelo,
                        input_placa,
                        input_ano,
                        input_id_cliente,
                        ElevatedButton(text="Cadastrar-se", color=Colors.WHITE, on_click=lambda _: verificar())
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    bgcolor=Colors.BLUE_100
                )
            )

        if page.route == "/sexta":
            page.views.append(
                View(
                    "/sexta",
                    [
                        AppBar(title=Text("Cadastro de Serviços"), bgcolor=Colors.BLUE_200),
                        Text(value=f"Preencha os campos com as informações do seviço", color=Colors.BLACK),
                        input_veiculo,
                        input_id_veiculo,
                        input_data,
                        input_descricao,
                        input_status,
                        input_valor,
                        ElevatedButton(text="Cadastrar-se", color=Colors.WHITE, on_click=lambda _: novo_cliente())
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    bgcolor=Colors.BLUE_100
                )
            )


        if page.route == "/setima":
            exibir_clientes()
            page.views.append(
                View(
                    "/setima",
                    [
                        AppBar(title=Text("Lista de Clientes"), bgcolor=Colors.BLUE_200),
                        lv,
                        ElevatedButton(text="Editar", color=Colors.WHITE, on_click=lambda _: editar_cliente())
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    bgcolor=Colors.BLUE_100
                )
            )

        if page.route == "/oitava":
            exibir_veiculos()
            page.views.append(
                View(
                    "/oitava",
                    [
                        AppBar(title=Text("Lista de Veiculos"), bgcolor=Colors.BLUE_200),
                        lv,
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    bgcolor=Colors.BLUE_100
                )
            )

        if page.route == "/nona":
            exibir_ordens()
            page.views.append(
                View(
                    "/nona",
                    [
                        AppBar(title=Text("Lista de Serviços"), bgcolor=Colors.BLUE_200),
                        lv,
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    bgcolor=Colors.BLUE_100
                )
            )

        if page.route == "/decima":
            page.views.append(
                View(
                    "/decima",
                    [
                        AppBar(title=Text("Informaçoes sobre o cliente"), bgcolor=Colors.BLUE_200),
                        txt_nome,
                        txt_cpf,
                        txt_telef,
                        txt_ender,
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    bgcolor=Colors.BLUE_100
                )
            )

        if page.route == "/onze":
            page.views.append(
                View(
                    "/onze",
                    [
                        AppBar(title=Text("Informações sobre o Veiculo"), bgcolor=Colors.BLUE_200),
                        txt_marca,
                        txt_modelo,
                        txt_placa,
                        txt_ano_fabri,
                        txt_id_cliente
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    bgcolor=Colors.BLUE_100
                )
            )

        if page.route == "/doze":
            page.views.append(
                View(
                    "/doze",
                    [
                        AppBar(title=Text("Informações sobre o Serviço"), bgcolor=Colors.BLUE_200),
                        txt_veiculo,
                        txt_id_veiculo,
                        txt_data,
                        txt_descricao,
                        txt_status,
                        txt_valor,
                        txt_id_orden
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    bgcolor=Colors.BLUE_100
                )
            )

        if page.route == "/treze":
            page.views.append(
                View(
                    "/treze",
                    [
                        AppBar(title=Text("Editar dados Cliente"), bgcolor=Colors.BLUE_200),
                        input_nome,
                        input_cpf,
                        input_telef,
                        input_ender,
                        ElevatedButton(text="Enviar",
                                       color=ft.Colors.WHITE,
                                       on_click=lambda _: editar_clientar(),
                                       bgcolor=Colors.BLACK,
                                       width=page.window.width),
                        ElevatedButton(text="Voltar",
                                       color=ft.Colors.BLACK,
                                       on_click=lambda _: page.go("/lista_cliente"),
                                       bgcolor=Colors.WHITE,
                                       width=page.window.width),

                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    bgcolor=Colors.BLUE_100
                )
            )


        page.update()

    def voltar(e):
        print("Views", page.views)
        removida = page.views.pop()
        print(removida)
        top_view = page.views[-1]
        print(top_view)
        page.go(top_view.route)


    progress = ft.ProgressRing(visible=False)

    msg_sucesso = ft.SnackBar(
        content=ft.Text(""),
        bgcolor=Colors.GREEN
    )
    msg_error = ft.SnackBar(
        content=ft.Text(""),
        bgcolor=Colors.RED
    )


    input_nome = ft.TextField(label="Nome",hint_text="Digite seu nome")
    input_cpf = ft.TextField(label="CPF",hint_text="Digite seu cpf")
    input_telef = ft.TextField(label="Telefone",hint_text="Digite seu telefone")
    input_ender = ft.TextField(label="Endereço",hint_text="Digite seu endereço")


    input_marca = ft.TextField(label="Marca",hint_text="Marca do veiculo")
    input_modelo = ft.TextField(label="Modelo",hint_text="Modelo do veiculo")
    input_placa = ft.TextField(label="Placa",hint_text="Placa do veiculo")
    input_ano = ft.TextField(label="Ano de Fabricação",hint_text="Ano de fabricação")
    input_id_cliente = ft.TextField(label="ID do Cliente",hint_text="Id do cliente responsavel pelo veiculo")


    input_veiculo = ft.TextField(label="Veiculo",hint_text="Veiculo")
    input_id_veiculo= ft.TextField(label="ID do Veiculo",hint_text="Id do Veiculo em questão")
    input_data= ft.TextField(label="ID do Veiculo",hint_text="Data de Abertura")
    input_descricao= ft.TextField(label="Descrição",hint_text="Descricão do serviço")
    input_status= ft.TextField(label="Status",hint_text="Status")
    input_valor= ft.TextField(label="Valor",hint_text="Valor do serviço")


    lv = ft.ListView(
        height=500
    )

    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=lambda _: verificar()
    )

    msg_sucesso = ft.SnackBar(
        content=ft.Text('Dados salvos com sucesso!'),
        bgcolor=Colors.GREEN,
    )

    msg_erro = ft.SnackBar(
        content=ft.Text('Preencha os campos!'),
        bgcolor=Colors.RED,
    )


    txt_nome = ft.Text()
    txt_cpf = ft.Text()
    txt_telef = ft.Text()
    txt_ender = ft.Text()

    txt_marca = ft.Text()
    txt_modelo = ft.Text()
    txt_placa = ft.Text()
    txt_ano_fabri = ft.Text()
    txt_id_cliente = ft.Text()

    txt_veiculo = ft.Text()
    txt_id_veiculo = ft.Text()
    txt_data = ft.Text()
    txt_descricao = ft.Text()
    txt_status = ft.Text()
    txt_valor = ft.Text()
    txt_id_orden = ft.Text()


    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar
    page.go(page.route)
ft.app(main)