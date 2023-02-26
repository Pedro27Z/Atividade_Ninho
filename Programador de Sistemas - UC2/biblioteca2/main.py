import psycopg2
from Controle.classConexao import Conexao
from Modelo.classAutores import Autores
from Modelo.classClientes import Clientes
from Modelo.classLivros import Livros

def criarTabelaAutor(conexao):
    conexao.manipularBanco('''
        CREATE TABLE "Autores"(
            "ID" int GENERATED ALWAYS AS IDENTITY,
            "Nome" varchar (255) NOT NULL,
            PRIMARY KEY ("ID")
        )
    ''')

def criarTabelaLivros(conexao):
    conexao.manipularBanco('''
        CREATE TABLE "Livros"(
            "ID" int GENERATED ALWAYS AS IDENTITY,
            "Nome" varchar (255) NOT NULL,
            "Pag" int,
            "Ano" timestamp,
            "Autor" int, 
            PRIMARY KEY ("ID"),

            Constraint fk_autor
            Foreign Key ("Autor")
            References "Autor" ("ID")
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
        )
    ''')

def criarTabelaClientes(conexao):
    conexao.manipularBanco('''
        CREATE TABLE "Clientes" (
        "ID" int GENERATED ALWAYS AS IDENTITY,
        "Nome" varchar (255) NOT NULL,
        PRIMARY KEY ("ID")
        )
    ''')

def criarTabelaAluguel(conexao):
    conexao.manipularBanco('''
        CREATE TABLE "Aluguel" (
        "ID" int GENERATED ALWAYS AS IDENTITY,
        "Cliente" int,
        "Livro" int,
        "Data" timestamp default current_timestamp,
        PRIMARY KEY ("ID"),

        Constraint fk_cliente
        Foreign Key ("Cliente")
        References "Clientes" ("ID")
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,

        Constraint fk_livro
        Foreign Key ("Livro")
        References "Livros" ("ID")
        ON DELETE NO ACTION
        ON UPDATE NO ACTION
        )
    ''')


def verClientes(conexao):

    clientes = conexao.consultarBanco('''
    Select * FROM "Clientes"
    ORDER BY "ID" ASC
    ''')
    print("ID | Nome")

    for cliente in clientes:

        print(f'{cliente[0]} | {cliente[1]}')

def verLivros(conexao):

    livros = conexao.consultarBanco('''
    Select * FROM "Livros"
    ORDER BY "ID" ASC
    ''')
    print("ID | Nome")

    for livro in livros:

        print(f'{livro[0]} | {livro[1]}')

    menuLivros(con)

def menuLivros(conexao):
    print("\n")
    print("""O Que Deseja Fazer :
    1 - Descrição do Livro
    2 - Cadastrar Livro
    3 - Atualizar Livro
    4 - Remover Livro
    0 - Voltar
    """)#CRUD
    menuLivro = input()
    match menuLivro:
        case "1":
            LivroID = input("Digite o ID do Livro: ")
            livro = Livros(LivroID, None, None, None, None)
            resultado = conexao.consultarBanco(livro.imprimirLivro())[0]
            autor = Autores(resultado[4], None)
            nomeAutor = conexao.consultarBanco(autor.imprimirAutores())[0][1]
            print (nomeAutor)

            if resultado != []:
                livroNome = resultado[1]
                livroPag = resultado[2]
                livroAno = resultado[3]
                print(f"""Nome - {livroNome}
Páginas - {livroPag}
Ano de Lançamento - {livroAno}
Autor - {nomeAutor}
                """)
            else:
                verLivros(con)

        case "2":
            print(" Cadastrar Livro ")
            novoLivroNome = input("Digite o Nome do Novo Livro: ")
            novoLivroNumPag = input("Digite o Numero de Páginas do Novo Livro: ")
            novoLivroAno = input("Digite o Ano de Lançamento do Novo Livro(Ano/Mes/Dia): ")
            novoLivroAutor = input("Digite o Nome do Autor")
            autores = conexao.consultarBanco('''
                      SELECT * FROM "Livros"
                      ORDER BY "ID" ASC
                                             ''')
            for autor in autores:
                if autor[1] != novoLivroAutor:# Caso autor não exista na tabela "Autor(es)", ele será 
                                              #inserido nela
                    novoAutor = Autores(None, novoLivroAutor)
                    conexao.manipularBanco(novoAutor.inserirAutores())
                    novoLivroAutorID = conexao.consultarBanco(f'''
                      SELECT * FROM "Autores"
                      WHERE "Nome" = '{novoAutor.Nome}'
            ''')[0][0]# Pegar o ID do autor
                    novoLivro = Livros(None, novoLivroNome, novoLivroNumPag, novoLivroAno , novoLivroAutorID)
                    conexao.manipularBanco(novoLivro.inserirLivro())
                elif autor[1] == novoLivroAutor:# Caso autor já exista na tabela "Autor(es)"
                    autor = Autores(None, novoLivroAutor)
                    LivroAutorID = conexao.consultarBanco(f'''
                      SELECT * FROM "Autores"
                      WHERE "Nome" = '{autor.Nome}'
            ''')[0][0]# Pegar o ID do autor
                    novoLivro = Livros(None, novoLivroNome, novoLivroNumPag, novoLivroAno , LivroAutorID)
                    conexao.manipularBanco(novoLivro.inserirLivro())
                else:
                    verLivros(con)
            
        case "3":
            print("Atualizar Livro")
            LivroID = input("Digite o ID do Livro: ")
            livro = Livros(LivroID, None, None, None, None)
            resultado = conexao.consultarBanco(livro.imprimirLivro())[0]
            if resultado != []:
                menuAlterarLivro = input("""Que Informação Deseja Atualizar?
    1 - Nome
    2 - Número de Páginas
    3 - Ano de Lançamento
    4 - Autor
    0 - Voltar
                      """)
                match menuAlterarLivro:
                    case "1":
                        novoLivroNome = input("Digite o Nome do Livro: ")
                        conexao.manipularBanco(livro.atualizarLivro("Nome", novoLivroNome))
                    case "2":
                        novoLivroNumPag = input("Digite o Numero de Páginas do Livro: ")
                        conexao.manipularBanco(livro.atualizarLivro("Pag", novoLivroNumPag))
                    case "3":
                        novoLivroAno = input("Digite o Ano de Lançamento do Livro(Ano/Mes/Dia): ")
                        conexao.manipularBanco(livro.atualizarLivro("Ano", novoLivroAno))
                    case "4":
                        novoLivroAutor = input("Digite o Nome do Autor do Livro: ")
                        autores = conexao.consultarBanco('''
                            SELECT * FROM "Livros"
                            ORDER BY "ID" ASC
                                                         ''')
                        for autor in autores:
                            if autor[1] != novoLivroAutor:# Caso autor não exista na tabela "Autor(es)", 
                                                          #ele será inserido nela
                                novoAutor = Autores(None, novoLivroAutor)
                                conexao.manipularBanco(novoAutor.inserirAutores())
                                novoLivroAutorID = conexao.consultarBanco(f'''
                                SELECT * FROM "Autores"
                                WHERE "Nome" = '{novoAutor.Nome}'
                        ''')[0][0]# Pegar o ID do autor
                                conexao.manipularBanco(livro.atualizarLivro("Autor", novoLivroAutorID))
                            elif autor[1] == novoLivroAutor:# Caso autor não exista na tabela "Autor(es)"
                                autor = Autores(None, novoLivroAutor)
                                LivroAutorID = conexao.consultarBanco(f'''
                                SELECT * FROM "Autores"
                                WHERE "Nome" = '{autor.Nome}'
                        ''')[0][0]# Pegar o ID do autor
                                conexao.manipularBanco(livro.atualizarLivro("Autor", novoLivroAutorID))
                            else:
                                verLivros(con)
                    case "0":  
                        verLivros(con)
                    case _:
                        print("Você digitou algo inválido!!!")
                        verLivros(con)

        case "4":
            print("Remover Livro")
            LivroID = input("Digite o ID do Livro: ")
            livro = Livros(LivroID, None, None, None, None)
            resultado = conexao.consultarBanco(livro.imprimirLivro())[0]
            if resultado != []:
                conexao.manipularBanco(livro.removerLivro())

        case "0":
            verLivros(con)

        case _:
            print("Você digitou algo inválido!!!")
            verLivros(con)

def verAlugueisSimples(conexao):

    alugueis = conexao.consultarBanco('''
    Select * FROM "Aluguel"
    ORDER BY "ID" ASC
    ''')
    print("ID Aluguel | ID Cliente | ID Livro | Data de Aluguel")

    for aluguel in alugueis:

        print(f'{aluguel[0]} | {aluguel[1]} | {aluguel[2]} | {aluguel[3]}')

def verAlugueisCompleto(conexao):

    alugueis = conexao.consultarBanco('''
    Select * FROM "Aluguel"
    ORDER BY "ID" ASC
    ''')
    print("ID Aluguel | Nome Cliente | Nome Livro | Data de Aluguel")

    for aluguel in alugueis:

        nomeDoCliente = conexao.consultarBanco(f'''
        SELECT "Nome" FROM "Cliente"
        WHERE "ID" = {aluguel[1]}
        ''')[0][0]

        nomeDoLivro = conexao.consultarBanco(f'''
        SELECT "Nome" FROM "Livros"
        WHERE "ID" = {aluguel[2]}
        ''')[0][0]
        
        print(f'{aluguel[0]} | {nomeDoCliente} | {nomeDoLivro} | {aluguel[3]}')



try:

    con = Conexao("Biblioteca","localhost","5432","postgres","postgres")

    while True:

        print('''Bem vindo a Biblioteca
        
        Menu:
        1. Ver Clientes
        2. Ver Livros
        3. Ver Alugueis (Simples)
        4. Ver Alugueis (Completo)
        0. Sair
        
        ''')

        opcoes = input("Digite a opção escolhida: ")

        match opcoes:
            case "1":
                verClientes(con)
            case "2":
                verLivros(con)
                menuLivros(con)
            case "3":
                verAlugueisSimples(con)
            case "4":
                verAlugueisCompleto(con)
            case "0":
                break
            case _:
                print("Você escolheu uma opção inválida!\n")

        input("Tecle Enter para continuar.")
    con.fechar()


except(Exception, psycopg2.Error) as error:

    print("Ocorreu um erro", error)
