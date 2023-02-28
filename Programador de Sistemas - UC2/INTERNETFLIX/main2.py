import psycopg2
from tkinter import *
from Controle.classConexao import Conexao
from Modelo.classCliente import Cliente
from Modelo.classPlano import Plano

def verClientes():
    global con
    global tabela
    tabela = "Cliente"
    textoLabel["text"] = ""
    textoLabel2["text"] = ""
    clientes = con.consultarBanco('''
    Select * FROM "Cliente"
    ORDER BY "ID" ASC
    ''')
    textoLabel["text"] = ("ID | Nome")

    for cliente in clientes:

        textoLabel2["text"] += (f'{cliente[0]} | {cliente[1]}\n')

def cadastrar():
    global con 
    global tabela
    match tabela:
        case "Cliente":
            texto = "Digite o nome do cliente:"
        case "Plano":
            texto = "Digite o nome do Plano:"
        case "Assinatura":
            texto = "Digite o Id do cliente:"

    labelcadastrar = Label(janela, text = texto)
    labelcadastrar.grid()
    nome = Entry(janela,)
    

def atualizar():
    global con 
    global tabela
    match tabela:
        case "Cliente":
            pass
        case "Plano":
            pass
        case "Assinatura":
            pass

def excluir():
    global con 
    global tabela
    match tabela:
        case "Cliente":
            pass
        case "Plano":
            pass
        case "Assinatura":
            pass

def verPlanos():
    global con
    global tabela
    tabela = "Plano"
    textoLabel["text"] = ""
    textoLabel2["text"] = ""
    planos = con.consultarBanco('''
    Select * FROM "Plano"
    ORDER BY "ID" ASC
    ''')
    textoLabel["text"] = ("ID | Tipo de plano")

    for plano in planos:

        textoLabel["text"] +=(f'{plano[0]} | {plano[1]}')

def verAssinaturas():
    global con
    global tabela
    tabela = "Assinatura"
    textoLabel["text"] = ""
    textoLabel2["text"] = ""
    assinaturas = con.consultarBanco('''
    Select * FROM "Assinatura"
    ORDER BY "ID" ASC
    ''')
    textoLabel["text"] = ("ID |  Assinatura")

    for assinatura in assinaturas:

        textoLabel2["text"] +=(f'{assinatura[0]} | {assinatura[1]}')


try:

    con = Conexao("Plataforma","localhost","5432","postgres","postgres")
    tabela = ""

except(Exception, psycopg2.Error) as error:

    print("Ocorreu um erro", error)


janela = Tk()
janela.title("INTERNETFLIX")
janela.geometry("500x500")

botaoClientes = Button(janela, text = "Cliente", command = verClientes)
botaoClientes.grid(column = 0, row= 0, padx = 5, pady = 5)

botaoPlanos = Button(janela, text = "Planos", command = verPlanos)
botaoPlanos.grid(column = 0, row= 1, padx = 5, pady = 5)

botaoAssinaturas = Button(janela, text = "Assinaturas", command = verAssinaturas)
botaoAssinaturas.grid(column = 0, row= 2, padx = 5, pady = 5)

textoLabel = Label(janela, text = "")
textoLabel.grid(column = 0, row= 3)

textoLabel2 = Label(janela, text = "")
textoLabel2.grid(column = 0, row= 4)

botaoCadastrar = Button(janela, text = "Cadastrar", command = cadastrar)
botaoCadastrar.grid(column = 0, row= 5, padx = 5, pady = 5)

botaoAtualizar = Button(janela, text = "Atualizar", command = atualizar)
botaoAtualizar.grid(column = 0, row= 6, padx = 5, pady = 5)

botaoExcluir = Button(janela, text = "Excluir", command = excluir)
botaoExcluir.grid(column = 0, row= 7, padx = 5, pady = 5)


janela.mainloop()