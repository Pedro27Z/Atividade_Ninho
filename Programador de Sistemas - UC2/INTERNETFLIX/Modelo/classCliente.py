class Cliente:
    def __init__(self, ID, Nome, CPF):
        self.ID = ID
        self.Nome = Nome
        self.CPF = CPF

    def inserirCliente(self):#Create
        sql = (f'''
    INSERT INTO "Cliente"
    VALUES(default, '{self.Nome}', '{self.CPF}')
    ''')
        return sql
    
    def imprimirCliente(self):#Read
        sql = (f'''
    SELECT * FROM "Cliente"
    WHERE "ID" = '{self.ID}' 
    ''')
        return sql
    
    def atualizarCliente(self, coluna, update):#Update
        sql = (f'''
    UPDATE "Cliente"
    SET "{coluna}" = '{update}'
    WHERE "ID" = '{self.ID}'
    ''')
        return sql
    
    def removerCliente(self):#Delete
        sql = (f'''
    DELETE FROM "Cliente"
    WHERE "ID" = '{self.ID}'
    ''')
        return sql