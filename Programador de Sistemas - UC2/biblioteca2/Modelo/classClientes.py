class Clientes:
    def __init__(self, ID, Nome):
        self.ID = ID
        self.Nome = Nome

    def inserirCliente(self):#Create
        sql = (f'''
    INSERT INTO "Clientes"
    VALUES(default, '{self.Nome}')
    ''')
        return sql
    
    def imprimirCliente(self):#Read
        sql = (f'''
    SELECT * FROM "Clientes"
    WHERE "ID" = '{self.ID}' 
    ''')
        return sql
    
    def atualizarCliente(self, coluna, update):#Update
        sql = (f'''
    UPDATE "Clientes"
    SET "{coluna}" = '{update}'
    WHERE "ID" = '{self.ID}'
    ''')
        return sql
    
    def removerCliente(self):#Delete
        sql = (f'''
    DELETE FROM "Clientes"
    WHERE "ID" = '{self.ID}'
    ''')
        return sql