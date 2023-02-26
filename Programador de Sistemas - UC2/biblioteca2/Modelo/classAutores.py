class Autores:
    def __init__(self, ID, Nome):
        self.ID = ID
        self.Nome = Nome

    def inserirAutores(self):#Create
        sql = (f'''
    INSERT INTO "Autores"
    VALUES(default, '{self.Nome}')
    ''')
        return sql
    
    def imprimirAutores(self):#Read
        sql = (f'''
    SELECT * FROM "Autores"
    WHERE "ID" = '{self.ID}' 
    ''')
        return sql
    
    def atualizarAutores(self, coluna, update):#Update
        sql = (f'''
    UPDATE "Autores"
    SET "{coluna}" = '{update}'
    WHERE "ID" = '{self.ID}'
    ''')
        return sql
    
    def removerAutores(self):#Delete
        sql = (f'''
    DELETE FROM "Autores"
    WHERE "ID" = '{self.ID}'
    ''')
        return sql