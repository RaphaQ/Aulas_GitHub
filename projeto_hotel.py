import flet as ft
from datetime import datetime

class Pessoa:
    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    def exibir_informacoes(self):
        return f"Nome: {self.__nome}, Telefone: {self.__telefone}, Email: {self.__email}"

    # Getters e Setters
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

class Cliente(Pessoa):
    id_counter = 1

    def __init__(self, nome, telefone, email):
        super().__init__(nome, telefone, email)
        self.__id_cliente = Cliente.id_counter
        Cliente.id_counter += 1

    def get_id(self):
        return self.__id_cliente

    def exibir_informacoes(self):
        return f"ID: {self.__id_cliente} | {super().exibir_informacoes()}"
    
class Quarto:
    def __init__(self, numero, tipo, preco):
        self.__numero = numero
        self.__tipo = tipo
        self.__preco = preco
        self.__disponivel = True

    def get_numero(self):
        return self.__numero

    def get_tipo(self):
        return self.__tipo

    def get_preco(self):
        return self.__preco

    def esta_disponivel(self):
        return self.__disponivel

    def set_disponibilidade(self, status):
        self.__disponivel = status

class Reserva:
    def __init__(self, cliente, quarto, checkin, checkout):
        self.cliente = cliente
        self.quarto = quarto
        self.checkin = checkin
        self.checkout = checkout
        self.status = "Ativa"

    def cancelar(self):
        self.status = "Cancelada"
        self.quarto.set_disponibilidade(True)

class GerenciadorDeReservas:
    def __init__(self):
        self.clientes = []
        self.quartos = []
        self.reservas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def verificar_disponibilidade(self):
        return [q for q in self.quartos if q.esta_disponivel()]

    def criar_reserva(self, cliente_id, numero_quarto, checkin, checkout):
        cliente = next((c for c in self.clientes if c.get_id() == cliente_id), None)
        quarto = next((q for q in self.quartos if q.get_numero() == numero_quarto and q.esta_disponivel()), None)

        if cliente and quarto:
            reserva = Reserva(cliente, quarto, checkin, checkout)
            self.reservas.append(reserva)
            quarto.set_disponibilidade(False)
            return reserva
        return None

    def listar_reservas(self):
        return self.reservas

    def cancelar_reserva(self, reserva):
        reserva.cancelar()


def main(page: ft.Page):
    gerenciador = GerenciadorDeReservas()

    # Dados iniciais de exemplo
    gerenciador.adicionar_quarto(Quarto(101, "Single", 150))
    gerenciador.adicionar_quarto(Quarto(102, "Double", 200))
    gerenciador.adicionar_quarto(Quarto(201, "Suite", 350))

    def listar_quartos(e):
        page.controls.clear()
        page.controls.append(ft.Text("Lista de Quartos:"))
        for q in gerenciador.quartos:
            status = "Disponível" if q.esta_disponivel() else "Ocupado"
            page.controls.append(ft.Text(f"Quarto {q.get_numero()} - {q.get_tipo()} - R${q.get_preco()} - {status}"))
        page.controls.append(ft.ElevatedButton("Voltar", on_click=tela_inicial))
        page.update()

    def tela_inicial(e=None):
        page.controls.clear()
        page.controls.append(ft.Text(f"Sistema - Refúgio dos Sonhos"))

        page.controls.append(ft.ElevatedButton("Ver Quartos", on_click=listar_quartos))
        page.controls.append(ft.ElevatedButton("Gerenciar Clientes", on_click=tela_clientes))
        page.controls.append(ft.ElevatedButton("Gerenciar Reservas", on_click=tela_reservas))
        page.update()

    def tela_clientes(e):
        page.controls.clear()
        page.controls.append(ft.Text("Clientes:"))

        for cliente in gerenciador.clientes:
            page.controls.append(ft.Text(cliente.exibir_informacoes()))

        def adicionar_cliente(e):
            nome = nome_input.value
            telefone = telefone_input.value
            email = email_input.value
            gerenciador.adicionar_cliente(Cliente(nome, telefone, email))
            tela_clientes(None)

        nome_input = ft.TextField(label="Nome")
        telefone_input = ft.TextField(label="Telefone")
        email_input = ft.TextField(label="Email")
        page.controls.extend([nome_input, telefone_input, email_input])
        page.controls.append(ft.ElevatedButton("Adicionar Cliente", on_click=adicionar_cliente))
        page.controls.append(ft.ElevatedButton("Voltar", on_click=tela_inicial))
        page.update()

    def tela_reservas(e):
        page.controls.clear()
        page.controls.append(ft.Text("Reservas Atuais:"))

        for reserva in gerenciador.reservas:
            info = f"Reserva de {reserva.cliente.get_nome()} no Quarto {reserva.quarto.get_numero()} - {reserva.status}"
            page.controls.append(ft.Text(info))

        def criar_reserva(e):
            try:
                cliente_id = int(cliente_id_input.value)
                numero_quarto = int(quarto_input.value)
                checkin = datetime.strptime(checkin_input.value, "%Y-%m-%d")
                checkout = datetime.strptime(checkout_input.value, "%Y-%m-%d")

                reserva = gerenciador.criar_reserva(cliente_id, numero_quarto, checkin, checkout)
                if reserva:
                    page.snack_bar = ft.SnackBar(ft.Text("Reserva criada com sucesso!"))
                else:
                    page.snack_bar = ft.SnackBar(ft.Text("Falha ao criar reserva. Verifique os dados."))

                tela_reservas(None)
            except Exception as ex:
                page.snack_bar = ft.SnackBar(ft.Text(f"Erro: {str(ex)}"))
                page.update()

        cliente_id_input = ft.TextField(label="ID Cliente")
        quarto_input = ft.TextField(label="Número do Quarto")
        checkin_input = ft.TextField(label="Data Check-in (YYYY-MM-DD)")
        checkout_input = ft.TextField(label="Data Check-out (YYYY-MM-DD)")

        page.controls.extend([cliente_id_input, quarto_input, checkin_input, checkout_input])
        page.controls.append(ft.ElevatedButton("Criar Reserva", on_click=criar_reserva))
        page.controls.append(ft.ElevatedButton("Voltar", on_click=tela_inicial))
        page.update()

    tela_inicial()

ft.app(target=main)