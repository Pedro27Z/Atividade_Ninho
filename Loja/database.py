import psycopg2

class DataBase():
    def __init__(self, name= "system", user="postgres", password="postgres", host="localhost", port=5432):
        self.name = name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def conecta(self):
        self.connection = psycopg2.connect(
            dbname=self.name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    
    def criarTabelaFornecedores(self):
        cursor = self.connection.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS Fornecedores(
            
            CNPJ TEXT,
            NOME TEXT,
            LOGRADOURO TEXT,
            NUMERO TEXT,
            COMPLEMENTO TEXT,
            BAIRRO TEXT,
            MUNICIPIO TEXT,
            UF TEXT,
            CEP TEXT,
            TELEFONE TEXT,
            EMAIL TEXT,
            PRIMARY KEY(CNPJ)
            );
        ''')

    #def registrarFornecedor(self, fullDataSet):
    #    cursor = self.connection.cursor()
    #    try:
    #        cursor.execute('''INSERT INTO Fornecedores VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', fullDataSet)
    #        self.connection.commit()
    #        return "OK"
    #    except:
    #        return "Erro"
    
    def registrarFornecedor(self, fullDataSet):
        campos_tabela = ('CNPJ', 'NOME', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO', 'BAIRRO', 'MUNICIPIO', 'UF', 'CEP', 'TELEFONE', 'EMAIL')
        qntd = ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s")
        cursor = self.connection.cursor()
        try:
            cursor.execute(f'''INSERT INTO Fornecedores ({", ".join(campos_tabela)})
            VALUES({qntd})''', fullDataSet)
            self.connection.commit()
            return "OK"
        except:
            return "Erro"



        
    def verFornecedores(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Fornecedores ORDER BY NOME")
            fornecedores = cursor.fetchall()
            return fornecedores
        except:
            pass

    def removerFornecedor(self,id):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Fornecedores WHERE CNPJ = '{id}' ")
            self.connection.commit()
            return "Cadastro de fornecedor removido com sucesso!"
        except:
            return "Erro ao excluir registro!"

    def atualizar_Fornecedor(self, fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f'''UPDATE Fornecedores set
            CNPJ = '{fullDataSet[0]}',
            NOME = '{fullDataSet[1]}',
            LOGRADOURO = '{fullDataSet[2]}',
            NUMERO = '{fullDataSet[3]}',
            COMPLEMENTO = '{fullDataSet[4]}',
            BAIRRO = '{fullDataSet[5]}',
            MUNICIPIO = '{fullDataSet[6]}',
            UF = '{fullDataSet[7]}',
            CEP = '{fullDataSet[8]}',
            TELEFONE = '{fullDataSet[9]}',
            EMAIL = '{fullDataSet[10]}'

            WHERE CNPJ = '{fullDataSet[0]}'
        ''')
        self.connection.commit()




    def criarTabelaUsuario(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                    name TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    access TEXT NOT NULL
                );
            ''')
            self.connection.commit()
        except AttributeError:
            print('Faça a conexão')

    def inserirUsuario(self,name,username,password,access):
        try:
            cursor= self.connection.cursor()
            cursor.execute('''
                INSERT INTO users(name,username,password,access) VALUES(%s,%s,%s,%s)
            ''',(name,username,password,access))
            self.connection.commit()
        except AttributeError:
            print('Faça a conexão')
        
    def checarUsuario(self, username, password):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT * FROM users;
            
            ''')
            for linha in cursor.fetchall():
                if linha[2].upper() == username.upper() and linha[3] == password and linha[4] == "Administrador":
                    return "Administrador"
                
                elif linha[2].upper() == username.upper() and linha[3] == password and linha[4] == "Usuário":
                    return "Usuário"
                
                else:
                    continue
            return "Sem acesso"
        except:
            pass

