from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from CTkTable import *
from PIL import Image
import pywinstyles
import customtkinter
import tkinter
import random
import pymysql
import csv
from datetime import datetime
import numpy as np


#aparencia customtkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


#definição de variaveis
janela = customtkinter.CTk()
janela.title("Controlador de Estoque")
janela.geometry("720x640") #tamanho da janela
my_tree =ttk.Treeview(janela, show='headings', height=20)
style = ttk.Style

placeholderArray=['','','','','']

for i in range(0,5):
    placeholderArray[i]=tkinter.StringVar()



moldura = tkinter.Frame(janela, bg="#242424") #moldura, bg = cor
moldura.pack()

corBotao = "#196E78"



manageFrame = customtkinter.CTkLabel(moldura, text="Gerenciar", text_color="black", bg_color="#333333", anchor=E, corner_radius=10)
manageFrame.grid(row=0, column=0, sticky="w", padx=[3,200], pady=20, ipadx=[6])

botaoSalvar = customtkinter.CTkButton(manageFrame, text="SALVAR", corner_radius=30, width=10, bg_color="#333333")
botaoAtualizar = customtkinter.CTkButton(master=manageFrame, text="ATUALIZAR", corner_radius=30, width=10, bg_color="#333333")
botaoDeletar = customtkinter.CTkButton(manageFrame, text="DELETAR", corner_radius=30, width=10, bg_color="#333333")
botaoSelecionar = customtkinter.CTkButton(manageFrame, text="SELECIONAR", corner_radius=30, width=10, bg_color="#333333")
botaoProcurar = customtkinter.CTkButton(manageFrame, text="PROCURAR", corner_radius=30, width=10, bg_color="#333333")
botaoLimpar = customtkinter.CTkButton(manageFrame, text="LIMPAR", corner_radius=30, width=10, bg_color="#333333")
botaoExportar = customtkinter.CTkButton(manageFrame, text="EXPORTAR", corner_radius=30, width=10, bg_color="#333333")

botaoSalvar.grid(row=1, column=0, padx=5, pady=5)
botaoAtualizar.grid(row=1, column=1, padx=5, pady=5)
botaoDeletar.grid(row=1, column=2, padx=5, pady=5)
botaoSelecionar.grid(row=1, column=3, padx=5, pady=5)
botaoProcurar.grid(row=1, column=4, padx=5, pady=5)
botaoLimpar.grid(row=1, column=5, padx=5, pady=5)
botaoExportar.grid(row=1, column=6, padx=5, pady=5)

entriesFrame = customtkinter.CTkLabel(moldura, text="Formulário", text_color="black", bg_color="#333333")
entriesFrame.grid(row=1, column=0, sticky="w", padx=[3,200], pady=[0,20], ipadx=[6])

itemIdLabel=customtkinter.CTkLabel(entriesFrame, text="ITEM ID", anchor="e", width=10, bg_color="#333333", text_color="black")
nomeLabel=customtkinter.CTkLabel(entriesFrame, text="NOME", anchor="e", width=10, bg_color="#333333", text_color="black")
precoLabel=customtkinter.CTkLabel(entriesFrame, text="PREÇO", anchor="e", width=10, bg_color="#333333", text_color="black")
quantidadeLabel=customtkinter.CTkLabel(entriesFrame, text="QUANTIDADE", anchor="e", width=10, bg_color="#333333", text_color="black")
categoriaLabel=customtkinter.CTkLabel(entriesFrame, text="CATEGORIA", anchor="e", width=10, bg_color="#333333", text_color="black")

itemIdLabel.grid(row=1, column=0, padx=10)
nomeLabel.grid(row=2, column=0, padx=10)
precoLabel.grid(row=3, column=0, padx=10)
quantidadeLabel.grid(row=4, column=0, padx=10)
categoriaLabel.grid(row=5, column=0, padx=10)

categoriaArray = ["Exemplo 1", "Exemplo 2", "Exemplo 3"]

itemIdEntry=customtkinter.CTkEntry(entriesFrame, width=200, textvariable=placeholderArray[0], bg_color="#333333")
nomeEntry=customtkinter.CTkEntry(entriesFrame, width=200, textvariable=placeholderArray[1], bg_color="#333333")
precoEntry=customtkinter.CTkEntry(entriesFrame, width=200, textvariable=placeholderArray[2], bg_color="#333333")
quantidadeEntry=customtkinter.CTkEntry(entriesFrame, width=200, textvariable=placeholderArray[3], bg_color="#333333")
categoriaCombo=customtkinter.CTkComboBox(entriesFrame, width=200, variable=placeholderArray[4], values=categoriaArray, bg_color="#333333")

itemIdEntry.grid(row = 1, column= 2, padx= 5, pady = 5)
nomeEntry.grid(row = 2, column= 2, padx= 5, pady = 5)
precoEntry.grid(row = 3, column= 2, padx= 5, pady = 5)
quantidadeEntry.grid(row = 4, column= 2, padx= 5, pady = 5)
categoriaCombo.grid(row = 5, column= 2, padx= 5, pady = 5)

gerarIdBtn = customtkinter.CTkButton(entriesFrame, text="GERAR ID", corner_radius=30, width=10, bg_color="#333333")
gerarIdBtn.grid(row=0, column=2, padx=5, pady=5)

manageFrame = customtkinter.CTkLabel(moldura, text="Gerenciar", text_color="black", bg_color="#333333", anchor=E, corner_radius=10)
manageFrame.grid(row=3, column=0, sticky="w", padx=[3,200], pady=20, ipadx=[6])

textoId = customtkinter.CTkButton(manageFrame, text="SALVAR", corner_radius=30, width=10, bg_color="#333333")
textoNome = customtkinter.CTkButton(master=manageFrame, text="ATUALIZAR", corner_radius=30, width=10, bg_color="#333333")
textoPreco = customtkinter.CTkButton(manageFrame, text="DELETAR", corner_radius=30, width=10, bg_color="#333333")
textoQuantidade = customtkinter.CTkButton(manageFrame, text="SELECIONAR", corner_radius=30, width=10, bg_color="#333333")
textoCategoria = customtkinter.CTkButton(manageFrame, text="PROCURAR", corner_radius=30, width=10, bg_color="#333333")



value = [[1,"teste1","R$20,00",10,"x"],
         [2,"teste2","R$20,00",3,"y"],
         [3,"teste3","R$20,00",9,"z"],
         [4,"teste4","R$20,00",4,"x"],
         [5,"teste5","R$20,00",15,"z"]]

table = CTkTable(janela, row=5, column=5, values = value)
table.pack(expand=True, fill="both", padx=20, pady=20)

janela.resizable(False,False)
janela.mainloop()
