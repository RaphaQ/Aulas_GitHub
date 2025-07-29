# import flet as ft

# def main(page: ft.Page):
#     page.title = "Minha Aplicação Flet"
#     page.add(
#         ft.Text("Bem-vindo ao Flet!"),
#         ft.ElevatedButton("Clique Aqui !", on_click=lambda _: page.add(ft.Text("Botao Clicado!")))
#     )

# ft.app(target=main)





# import flet as ft

# def main(page: ft.Page):
#     page.title = "Minha Aplicação Flet"

#     layout = ft.Column(
#         controls=[
#             ft. Text("Janela Principal", color='pink', size=20, weight=ft.FontWeight.BOLD), 
#             ft. ElevatedButton ("Botão 1"),
#             ft. ElevatedButton ("Botão 2"), 
#             ft. ElevatedButton("Botão 3"),
#         ]
#     )

#     page.add(layout)

# ft.app(target=main)


# import flet as ft

# def main(page: ft.Page):
#     page.title = "Formulário de Cadastro"
#     page.scroll = "auto"

#     nome = ft.TextField(label="Nome", width=300)
#     sobrenome = ft.TextField(label="Sobrenome", width=300)
#     email = ft.TextField(label="Email", width=300)
#     telefone = ft.TextField(label="Telefone", width=300)
#     nascimento = ft.TextField(label="Data de Nascimento", hint_text="dd/mm/aaaa", width=300)
    
#     genero = ft.Dropdown(
#         label="Gênero",
#         options=[
#             ft.dropdown.Option("Masculino"),
#             ft.dropdown.Option("Feminino"),
#             ft.dropdown.Option("Outro"),
#             ft.dropdown.Option("Prefiro não dizer"),
#         ],
#         width=300
#     )

#     endereco = ft.TextField(label="Endereço", multiline=True, width=400)
#     comentarios = ft.TextField(label="Comentários adicionais", multiline=True, width=400)

#     def enviar_dados(e):
#         page.snack_bar = ft.SnackBar(
#             ft.Text(f"Cadastro enviado para {nome.value} {sobrenome.value}!"),
#             open=True
#         )
#         page.update()

#     botao_enviar = ft.ElevatedButton(text="Enviar", on_click=enviar_dados)

#     page.add(
#         ft.Column([
#             ft.Row([nome, sobrenome]),
#             email,
#             telefone,
#             nascimento,
#             genero,
#             endereco,
#             comentarios,
#             botao_enviar
#         ], spacing=10)
#     )

# ft.app(target=main)

# import flet as ft

# def main(page: ft.Page):
#     page.title = "Lista de Tarefas"

#     tarefas = []

#     campo_tarefa = ft.TextField(label="Nova tarefa", expand=True)

#     def adicionar_tarefa(e):
#         if campo_tarefa.value.strip() == "":
#             return

#         checkbox = ft.Checkbox(label=campo_tarefa.value)
        
#         def remover_tarefa(ev):
#             tarefas_container.controls.remove(linha_tarefa)
#             page.update()

#         linha_tarefa = ft.Row([
#             checkbox,
#             ft.IconButton(icon=ft.icons.DELETE, on_click=remover_tarefa)
#         ])
#         tarefas_container.controls.append(linha_tarefa)
#         campo_tarefa.value = ""
#         page.update()

#     botao_adicionar = ft.ElevatedButton(text="Adicionar", on_click=adicionar_tarefa)

#     tarefas_container = ft.Column()

#     page.add(
#         ft.Row([campo_tarefa, botao_adicionar]),
#         tarefas_container
#     )

# ft.app(target=main)

# import flet as ft
# import re

# def main(page: ft.Page):
#     page.title = "Calculadora com %"

#     expressao = ft.Text(value="", size=30)

#     def adicionar_valor(e):
#         expressao.value += e.control.text
#         page.update()

#     def calcular(e):
#         try:
#             resultado = str(eval(expressao.value))
#             expressao.value = resultado
#         except:
#             expressao.value = "Erro"
#         page.update()

#     def limpar(e):
#         expressao.value = ""
#         page.update()

#     def aplicar_porcentagem(e):
#         try:
#             # Encontra o último número da expressão
#             partes = re.split(r'([\+\-\*/])', expressao.value)
#             if partes:
#                 ultimo = partes[-1]
#                 if ultimo.strip().replace('.', '', 1).isdigit():
#                     porcento = str(float(ultimo) / 100)
#                     partes[-1] = porcento
#                     expressao.value = ''.join(partes)
#                     page.update()
#         except:
#             expressao.value = "Erro"
#             page.update()

#     botoes = [
#         ["7", "8", "9", "/"],
#         ["4", "5", "6", "*"],
#         ["1", "2", "3", "-"],
#         ["0", ".", "%", "+"],
#         ["limpar", "="]
#     ]

#     linhas_botoes = []
#     for linha in botoes:
#         linha_controles = []
#         for simbolo in linha:
#             if simbolo == "=":
#                 btn = ft.ElevatedButton(text=simbolo, on_click=calcular, expand=True)
#             elif simbolo == "limpar":
#                 btn = ft.ElevatedButton(text=simbolo, on_click=limpar, expand=True)
#             elif simbolo == "%":
#                 btn = ft.ElevatedButton(text=simbolo, on_click=aplicar_porcentagem, expand=True)
#             else:
#                 btn = ft.ElevatedButton(text=simbolo, on_click=adicionar_valor, expand=True)
#             linha_controles.append(btn)
#         linhas_botoes.append(ft.Row(linha_controles, alignment="center"))

#     page.add(
#         expressao,
#         *linhas_botoes
#     )

# ft.app(target=main)



# import flet as ft

# def main(page: ft.Page):
#     page.title = "Bloco de Notas"
#     page.scroll = "auto"

#     texto_area = ft.TextField(
#         multiline=True,
#         min_lines=20,
#         max_lines=40,
#         expand=True,
#         border="outline",
#         label="Digite seu texto aqui..."
#     )

#     contador = ft.Text(value="0 palavras", size=12, italic=True, color= ft.Colors.GREY)

#     def atualizar_contador(e):
#         palavras = texto_area.value.strip().split()
#         contador.value = f"{len(palavras)} palavras"
#         page.update()

#     texto_area.on_change = atualizar_contador

#     def limpar_texto(e):
#         texto_area.value = ""
#         contador.value = "0 palavras"
#         page.update()

#     def salvar_texto(e):
#         with open("bloco_de_notas.txt", "w", encoding="utf-8") as f:
#             f.write(texto_area.value)
#         page.snack_bar = ft.SnackBar(ft.Text("Texto salvo com sucesso!"), open=True)
#         page.update()

#     def abrir_texto(e):
#         try:
#             with open("bloco_de_notas.txt", "r", encoding="utf-8") as f:
#                 texto_area.value = f.read()
#                 atualizar_contador(None)
#                 page.update()
#         except FileNotFoundError:
#             page.snack_bar = ft.SnackBar(ft.Text("Arquivo não encontrado."), open=True)
#             page.update()

#     # Layout com botões
#     botoes = ft.Row([
#         ft.ElevatedButton(text="Abrir", on_click=abrir_texto),
#         ft.ElevatedButton(text="Salvar", on_click=salvar_texto),
#         ft.ElevatedButton(text="Limpar", on_click=limpar_texto)
#     ], alignment="center")

#     # Página
#     page.add(
#         botoes,
#         texto_area,
#         contador
#     )

# ft.app(target=main)






