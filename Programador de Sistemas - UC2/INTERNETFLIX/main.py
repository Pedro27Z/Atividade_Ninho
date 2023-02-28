import psycopg2
from Controle.classConexao import Conexao
from Modelo.classCliente import Cliente
from Modelo.classPlano import Plano

def verClientes(conexao):

    clientes = conexao.consultarBanco('''
    Select * FROM "Cliente"
    ORDER BY "ID" ASC
    ''')
    print("ID | Nome")

    for cliente in clientes:

        print(f'{cliente[0]} | {cliente[1]}')
    
    menuClientes(con)

def menuClientes(conexao):
    menu = input("""O que deseja fazer?
    1. Cadastrar Cliente
    2. Atualizar Cliente
    3. Excluir Cliente
    0. Voltar Para o Menu Principal
    """)
    match menu:
        case "1":
            novoClienteNome = input("Digite o nome do Cliente: ")
            novoClienteCPF = input("Digite o CPF do Cliente: ")
            novoCliente = Cliente(None, novoClienteNome, novoClienteCPF)
            conexao.manipularBanco(novoCliente.inserirCliente())
        case "2":
            clienteID = input("Digite o ID do Cliente: ")
            cliente = Cliente(clienteID, None, None)
            resultado = conexao.consultarBanco(cliente.imprimirCliente())[0]
            if resultado != []:
                menuAlterarCliente = input("""Que Informação Deseja Atualizar?
    1 - Nome
    2 - CPF
    
                      """)
                match menuAlterarCliente:
                    case "1":
                        novoClienteNome = input("Digite o Nome do Cliente: ")
                        conexao.manipularBanco(cliente.atualizarCliente("Nome", novoClienteNome))
                    case "2":
                        novoClienteCPF = input("Digite o CPF do Cliente: ")
                        conexao.manipularBanco(cliente.atualizarCliente("CPF", novoClienteCPF))

        case "3":
            clienteID = input("Digite o ID do Cliente: ")
            cliente = Cliente(clienteID, None, None)
            resultado = conexao.consultarBanco(cliente.imprimirCliente())[0]
            if resultado != []:
                conexao.manipularBanco(cliente.removerCliente())
        case "0":
            pass
        case _:
            print("Você escolheu uma opção inválida!\n")
            pass


    pass

def verPlanos(conexao):

    planos = conexao.consultarBanco('''
    Select * FROM "Plano"
    ORDER BY "ID" ASC
    ''')
    print("ID | Nome | Tipo | Valor")

    for plano in planos:

        print(f'{plano[0]} | {plano[1]} | {plano[2]} | {plano[3]}')

def verAssinaturas(conexao):

    assinaturas = conexao.consultarBanco('''
    Select * FROM "Assinatura"
    ORDER BY "ID" ASC
    ''')
    print("ID Assinatura | Nome Cliente | Nome Plano | Tipo de Plano | Valor")

    for assinatura in assinaturas:

        nomeDoCliente = conexao.consultarBanco(f'''
        SELECT "Nome" FROM "Cliente"
        WHERE "ID" = {assinatura[1]}
        ''')[0]

        nomeDoPlano = conexao.consultarBanco(f'''
        SELECT "Nome" FROM "Plano"
        WHERE "ID" = {assinatura[2]}
        ''')[0]

        tipoDePlano = conexao.consultarBanco(f'''
        SELECT "Tipo" FROM "Plano"
        WHERE "ID" = {assinatura[2]}
        ''')[0]

        valorPlano = conexao.consultarBanco(f'''
        SELECT "Valor" FROM "Plano"
        WHERE "ID" = {assinatura[2]}
        ''')[0]
        
        print(f'{assinatura[0]} | {nomeDoCliente[0]} | {nomeDoPlano[0]} | {tipoDePlano[0]} | {valorPlano[0]}')

def cadastrarAssinatura(conexao):
    clienteID = input("Digite o ID do Cliente: ")
    cliente = Cliente(clienteID, None, None)
    resultadoClienteID = conexao.consultarBanco(cliente.imprimirCliente())[0]
    if resultadoClienteID != []:
        idC = clienteID
        planoId = input("Digite o ID do Plano: ")
        plano = Plano(planoId, None, None, None)
        resultadoPlanoId = conexao.consultarBanco(plano.imprimirPlano())[0]
        if resultadoPlanoId != []:
            idP = planoId
        else:
            verPlanos(con)
        conexao.manipularBanco('''
                    INSERT INTO "Assinatura"
                    Values (default, '{idC}', '{idP}')
                                ''')
    else:
        verClientes(con)

try:

    con = Conexao("Plataforma","localhost","5432","postgres","postgres")

    cadastrarAssinatura(con)

    while True:

        print('''Bem vindo a Plataforma INTERNETFLIX
            
        Menu:
        1. Ver Clientes
        2. Ver Planos
        3. Ver Assinaturas
        0. Sair
            
            ''')

        opcoes = input("Digite a opção escolhida: ")

        match opcoes:
            case "1":
                verClientes(con)
            case "2":
                verPlanos(con)
            case "3":
                verAssinaturas(con)
            case "0":
                break
            case _:
                print("Você escolheu uma opção inválida!\n")

        input("Tecle Enter para continuar.")
        
    con.fechar()


except(Exception, psycopg2.Error) as error:

    print("Ocorreu um erro", error)


