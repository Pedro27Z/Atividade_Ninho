import psycopg2

class Conexao:
    def __init__(self, parDB, parHost, parPort, parUser,parPassword):
        self._db = psycopg2.connect(database = parDB, 
                                    host = parHost, 
                                    port = parPort, 
                                    user = parUser, 
                                    password = parPassword)

    def consultarBanco(self, sql):
        cursor = self._db.cursor()

        cursor.execute(sql)

        resultado = cursor.fetchall()

        cursor.close()

        return resultado
    
    def manipularBanco(self, sql):

        cursor = self._db.cursor()

        cursor.execute(sql)

        self._db.commit()

        cursor.close()

        return True
    


    def fechar(self):
        self._db.close()