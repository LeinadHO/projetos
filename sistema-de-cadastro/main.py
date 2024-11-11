from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from openpyxl import Workbook
from openpyxl import load_workbook
import pathlib

# Ckasse que representa a janela do sistema
class CadastroDeClientes:
    def __init__(self, root):

        # Criação da tela principal
        root.title("Cadastro de Clientes")
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Botão que vai salvar as mudanças
        botao_salvar = ttk.Button(mainframe, text='Salvar', command=self.salvar)
        botao_salvar.grid(column=4, row=4)

        # Botão que vai limpar os campos
        botao_limpar = ttk.Button(mainframe, text='Limpar', command=self.limpar)
        botao_limpar.grid(column=3, row=4)

        # Campo para escrever o nome completo
        label_nome = ttk.Label(mainframe, text='Nome Completo:')
        label_nome.grid(column=1, row=1, sticky=(E))
        self.nome = StringVar()
        entry_nome = ttk.Entry(mainframe, width=25, textvariable=self.nome)
        entry_nome.grid(column=2, row=1, sticky=(W))

        # Campo para escrever o CPF
        label_cpf = ttk.Label(mainframe, text='CPF:')
        label_cpf.grid(column=1, row=2, sticky=(E))
        self.cpf = StringVar()
        entry_cpf = ttk.Entry(mainframe, width=18, textvariable=self.cpf)
        entry_cpf.grid(column=2, row=2, sticky=(W))

        # Campo para escrever o CEP
        label_cep = ttk.Label(mainframe, text='CEP:')
        label_cep.grid(column=1, row=3, sticky=(E))
        self.cep = StringVar()
        entry_cep = ttk.Entry(mainframe, width=18, textvariable=self.cep)
        entry_cep.grid(column=2, row=3, sticky=(W))

        # Ajustes na exibição dos elementos - FICA PRA DEPOIS     

    # Função que salva os dados no arquivo
    def salvar(self, *args):

        # Verifica se o arquivo já existe. Caso não exista, ele o cria
        wb = pathlib.Path('Clientes.xlsx')
        if wb.exists():
            pass
        else:
            wb = Workbook()
            ws = wb.active
            ws['A1'] = 'Nome Completo'
            ws['B1'] = 'CPF'
            ws['C1'] = 'CEP'
            wb.save('Clientes.xlsx')

        # Captura e salvamento dos dados
        nome = self.nome.get()
        cpf = self.cpf.get()
        cep = self.cep.get()

        if nome == '' or cpf == '' or cep == '':
            messagebox.showerror("Sistema", "Erro! Todos os campos devem ser preenchidos!")
        else:
            wb = load_workbook('Clientes.xlsx')
            ws = wb.active
            ws.cell(column=1, row=ws.max_row+1, value=nome)
            ws.cell(column=2, row=ws.max_row, value=cpf)
            ws.cell(column=3, row=ws.max_row, value=cep)
            wb.save('Clientes.xlsx')
            messagebox.showinfo('Sistema', 'Dados salvos com sucesso!')

        
    # Função que limpa o conteúdo escrito nos campos
    def limpar(self, *args):
        self.nome.set('')
        self.cpf.set('')
        self.cep.set('')


root = Tk()
CadastroDeClientes(root)
root.mainloop()

