import flet as ft
import requests

def main(page: ft.Page):
    page.bgcolor = ft.Colors.DEEP_ORANGE_400

    def enviar_post(e):
        dados = {
            'title': titulo_post.value,
            'body': conteudo_post.value,
            'userId': 1
        }
        resposta = requests.post('https://jsonplaceholder.typicode.com/posts',
                                 data=dados)
        if resposta.status_code == 201:
            mensagem.value = "POST CRIADO COM SUCESSO!"
        page.update()

    label_titulo = ft.Text("Título do Post", color="white")
    titulo_post = ft.TextField(bgcolor="white")
    label_conteudo = ft.Text("Conteúdo", color="white")
    conteudo_post = ft.TextField(bgcolor="white", multiline=True, min_lines=10)
    enviar = ft.ElevatedButton(icon=ft.Icons.SEND , text="Enviar", on_click=enviar_post)

    # mensagem = ft.Text("POST CRIADO COM SUCESSO!", color="white", size=20)
    mensagem = ft.Text("", color="white", size=20)

    page.add(
        ft.Column(
            [
                label_titulo,
                titulo_post,
                label_conteudo,
                conteudo_post,
                enviar,
                mensagem
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
            )
        )


ft.app(main)
