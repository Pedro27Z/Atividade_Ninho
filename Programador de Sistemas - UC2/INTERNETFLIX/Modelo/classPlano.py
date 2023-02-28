class Plano:
    def __init__(self, ID, Nome, Tipo, Valor):
        self.ID = ID
        self.Nome = Nome
        self.Tipo = Tipo
        self.Valor = Valor

    def inserirPlano(self):#Create
        sql = (f'''
    INSERT INTO "Plano"
    VALUES(default, '{self.Nome}','{self.Tipo}', '{self.Valor}')
    ''')
        return sql
    
    def imprimirPlano(self):#Read
        sql = (f'''
    SELECT * FROM "Plano"
    WHERE "ID" = '{self.ID}' 
    ''')
        return sql
    
    def atualizarPlano(self, coluna, update):#Update
        sql = (f'''
    UPDATE "Plano"
    SET "{coluna}" = '{update}'
    WHERE "ID" = '{self.ID}'
    ''')
        return sql
    
    def removerPlano(self):#Delete
        sql = (f'''
    DELETE FROM "Plano"
    WHERE "ID" = '{self.ID}'
    ''')
        return sql