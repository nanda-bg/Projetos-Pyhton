import flet as ft #framework do Python

def main(pagina):
    texto = ft.Text("Luna's Zap")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        texto_entrada = ft.Text(mensagem)
        chat.controls.append(texto_entrada)

        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)   #criar tunel de comunicação entre usuarios

    def enviar_mensagem(evento):
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")
        campo_mensagem.value = ""

        pagina.update()


    

    campo_mensagem = ft.TextField(label= "Digite sua mensagem", on_submit=enviar_mensagem )
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem,botao_enviar])
    
    def entrar_chat(evento):
        popup.open = False      #fechar popup
        pagina.remove(botao_iniciar)
        pagina.remove(texto)

        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")

        pagina.add(linha_enviar)

        
        pagina.update()

    titulo_popup = ft.Text("Bem-vindo ao Hashzap")
    nome_usuario = ft.TextField(label="Escreva seu nome", on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    popup = ft.AlertDialog(
        open = False, 
        modal = True, #para o popup abrir em uma janelinha no meio da pagina
        title = titulo_popup, 
        content = nome_usuario, 
        actions = [botao_entrar] #sempre passar no action uma lista
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton(text="Iniciar Chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)
    
ft.app(target=main, view= ft.WEB_BROWSER)