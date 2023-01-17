import random
from pokedex import*


class Treinador: #requisito obrigatório 3
   def __init__(self, nome , pokemonTreinador = [],):
     self.nome = nome
     self.pokemonTreinador = pokemonTreinador

   def listarPokemon(self):
     for i in range(len(self.pokemonTreinador)):
       if self.pokemonTreinador[i].apelido == "":
         print(f"{i+1}. {self.pokemonTreinador[i].nome}     {self.pokemonTreinador[i].status}")
       else:
          print(f"{i+1}. {self.pokemonTreinador[i].apelido}     {self.pokemonTreinador[i].status}")
     
   def escolherPokemon(self):
     while True:
       print("Escolha seu pokemon")
       for i in range(len(self.pokemonTreinador)):
         print(f"{i+1}. {self.pokemonTreinador[i].nome}")
       pokemonEscolhido = input("Digite o número do pokemon escolhido:\n")
       if pokemonEscolhido.isnumeric():
         if (int(pokemonEscolhido)) <= len(self.pokemonTreinador):
           return self.pokemonTreinador[int(pokemonEscolhido)-1]
         else:
           print("Digite um numero válido")
       else:
         print("Digite um numero válido")
     

   
     
class Jogador(Treinador): #requisito obrigatório 4
   def __init__(self, nome , pokemonTreinador, pokemonLab):
     super().__init__(nome , pokemonTreinador)
     self.nome = ""
     self.pokemonTreinador = []
     self.pokemonLab = []
     
   def listarPokemonLab(self):
     if self.pokemonLab == []:
       print("Você ainda não enviou pokémons para o laboratório do professor Carvalho.")
     else:
       for i in range(len(self.pokemonLab)):
         if self.pokemonLab[i].apelido == "":
           print(f"{i+1}.{self.pokemonLab[i].nome}")
         else:
           print(f"{i+1}.{self.pokemonLab[i].apelido}")

   def nomearPokemon(self, pokemonSelvagem):
     if pokemonSelvagem.apelido == "": 
        nomearPokemon = input("""Você gostaria de dar um nome ao seu novo pokémon?
  1.Sim
  2.Não
             """)
        if nomearPokemon == "1":
           novoNomePokemon = input("Digite um nome para o seu novo pokemon.\n")
           pokemonSelvagem.apelido = novoNomePokemon
        elif nomearPokemon == "2":
          print("Não? Tudo bem então!!")
        else:
          print("Não? Tudo bem então!!\n")
     
   def capturarPokemon(self, pokemonSelvagem):
     taxaCaptura = 0 #determinar se o pokemon será capturado ou não
     print ("""Ok, vou tentar captura-lo.\n
Pokébola vai!!!
     """)
     for i in range(3):
       taxaCaptura = random.randint(1,10)
       if taxaCaptura >= 7:
         if len(self.pokemonTreinador) < 6:
            print (f"Parabéns você capturou {pokemonSelvagem.nome}")
            self.nomearPokemon(pokemonSelvagem)
            self.pokemonTreinador.append(pokemonSelvagem)
            break 
         else:
           self.nomearPokemon(pokemonSelvagem)
           self.pokemonLab.append(pokemonSelvagem)
      
           print(f"Parabéns você capturou {pokemonSelvagem.nome}. Cada treinador só pode levar 6 pokémons com ele, então {pokemonSelvagem.nome} foi enviado ao laboratório do professor Carvalho.")
           break  
       else:
         print ("""
         .....
         """)
     else:
       print ("Oh não, ele escapou da pokebola...")

   def batalhaPokemon(treinador, oponente):
     pass

class Inimigo(Treinador): 
   def __init__(self, nome , pokemonTreinador):
     super().__init__(nome , pokemonTreinador)

jogador = Jogador("", [],[])
inimigo1 = Inimigo("Green", [pokemons[0]])
inimigo2 = Inimigo("Red", [pokemons[3]])
inimigo3 = Inimigo("Blue", [pokemons[6]])


