class Livros:
    def __init__(self, ID, Nome, Pag, Ano, Autor):
        self.ID = ID
        self.Nome = Nome
        self.Pag = Pag
        self.Ano = Ano
        self.Autor = Autor

    def inserirLivro(self):#Create
        sql = (f'''
    INSERT INTO "Livros"
    VALUES(default, '{self.Nome}', '{self.Pag}', '{self.Ano}', '{self.Autor}')
    ''')
        return sql
    
    def imprimirLivro(self):#Read
        sql = (f'''
    SELECT * FROM "Livros"
    WHERE "ID" = '{self.ID}' 
    ''')
        return sql
    
    def atualizarLivro(self, coluna, update):#Update
        sql = (f'''
    UPDATE "Livros"
    SET "{coluna}" = '{update}'
    WHERE "ID" = '{self.ID}'
    ''')
        return sql
    
    def removerLivro(self):#Delete
        sql = (f'''
    DELETE FROM "Livros"
    WHERE "ID" = '{self.ID}'
    ''')
        return sql
