import random
import time
from trainerdex import*
from pokedex import*
from movedex import*

def novoJogo(jogador, pokemons_iniciais):
  while jogador.nome == "":
    nomeJogador = input("Digite seu nome:\n")
    jogador.nome = nomeJogador
  while jogador.pokemonTreinador == []:

    print("Escolha seu pokémon inicial:")
    
    for i in range(len(pokemons_iniciais)):
      print(f"{i+1}.{pokemons_iniciais[i].nome}")

    pokemonInicial = input()

    if pokemonInicial == "1":
      print(f"Parabéns você escolheu {pokemons_iniciais[0].nome}.\n")
      jogador.pokemonTreinador.append(pokemons_iniciais[0])
    elif pokemonInicial == "2":
      print(f"Parabéns você escolheu {pokemons_iniciais[1].nome}.\n")
      jogador.pokemonTreinador.append(pokemons_iniciais[1])
    elif pokemonInicial == "3":
      print(f"Parabéns você escolheu {pokemons_iniciais[2].nome}.\n")
      jogador.pokemonTreinador.append(pokemons_iniciais[2])
      
    else:
      print("Você escolheu uma opção inválida, por favor escolha um dos três pokémons:\n")
      jogador.nomearPokemon(jogador.pokemonTreinador[0])

def batalhaPokemon(pokemonJogador, pokemonOponente):
  print(f"Vai {pokemonJogador.nome}")
  mostrarBarraVida(pokemonJogador, pokemonOponente)
  while (pokemonJogador.status != "FNT") and (pokemonOponente.status != "FNT"): 
   
    movimentoJogador = escolherMove(pokemonJogador)
    movimentoOponente = random.choice(pokemonOponente.moves)
    
    pokemonJogadorVel = calcularVelocidade(pokemonJogador)
    pokemonOponenteVel = calcularVelocidade(pokemonOponente)

    if pokemonJogadorVel > pokemonOponenteVel:

      print(f"{pokemonJogador.nome} usou {movimentoJogador.nome}")
      time.sleep(1)
      
      calcularDano(pokemonJogador, movimentoJogador, pokemonOponente)
      mostrarBarraVida(pokemonJogador, pokemonOponente)
      

      time.sleep(1)

      print(f"{pokemonOponente.nome} usou {movimentoOponente.nome}")
      time.sleep(1)
      
      calcularDano(pokemonOponente, movimentoOponente, pokemonJogador)
      mostrarBarraVida(pokemonJogador, pokemonOponente)
      
    else:
       print(f"{pokemonOponente.nome} usou {movimentoOponente.nome}")
       time.sleep(1)
      
       calcularDano(pokemonOponente, movimentoOponente, pokemonJogador)
       mostrarBarraVida(pokemonJogador, pokemonOponente)

       time.sleep(1)

       print(f"{pokemonJogador.nome} usou {movimentoJogador.nome}")
       time.sleep(1)
      
       calcularDano(pokemonJogador, movimentoJogador, pokemonOponente)
       mostrarBarraVida(pokemonJogador, pokemonOponente)

def escolherMove(pokemonJogador):
      while True:
        print("Escolha seu movimento: ")
        for i in range(len(pokemonJogador.moves)):
          print(f"{i+1}. {pokemonJogador.moves[i].nome}")
        movimentoEscolhido = input("Digite o número do movimento escolhido:\n")
        if movimentoEscolhido.isnumeric():
          if (int(movimentoEscolhido)) <= len(pokemonJogador.moves):
            return pokemonJogador.moves[int(movimentoEscolhido)-1]
          else:
            print("Digite um numero válido")
        else:
          print("Digite um numero válido")

    
def calcularDano(pokemonAtaca, move, pokemonDefende):
  dano = ((pokemonAtaca.ataque)+(move.poder)-(pokemonDefende.defesa))//3
  pokemonDefende.HP -= dano
  if pokemonDefende.HP <= 0:
    pokemonDefende.HP = 0
    pokemonDefende.status = "FNT"#FAINTED
    print(f"{pokemonDefende.nome} foi derrotado")
  
def mostrarBarraVida(pokemonJogador, pokemonOponente):
  maxBarraVidaPJ = ((pokemonJogador.HP*100)/pokemonJogador.maxHP)//10
  maxBarraVidaPO = ((pokemonOponente.HP*100)/pokemonOponente.maxHP)//10
  barraVidaPJ = "=" * int(maxBarraVidaPJ)
  barraVidaPO = "=" * int(maxBarraVidaPO)
  print(f"{pokemonJogador.nome.capitalize()}\n\t{barraVidaPJ}\n\t {pokemonJogador.HP}/{pokemonJogador.maxHP} {pokemonJogador.status}")
  print("\n")
  print(f"{pokemonOponente.nome.capitalize()}\n\t{barraVidaPO}\n\t {pokemonOponente.HP}/{pokemonOponente.maxHP} {pokemonOponente.status}")
  print("\n")

def calcularVelocidade(pokemon):
  velocidadePokemon = random.randint((pokemon.velocidade*.2), pokemon.velocidade)
  return velocidadePokemon

#---------Loop Principal----------

while True:
  novoJogo(jogador, pokemons_iniciais)
  print("""Escolha uma ação:
  1. Ver meus pokémons
  2. Capturar pokémons 
  3. Enfrentar oponentes
  4. Sair do jogo
  """) 
  menu = input()
  if menu == "1":
    print("""
    1.Pokemons comigo
    2.Pokemons do laboratório\n
    """)
    menuVerPokemons = input()
    if menuVerPokemons == "1":
      jogador.listarPokemon()
      print("\n")
    elif menuVerPokemons == "2":
      jogador.listarPokemonLab()
      print("\n")
    else:
      print("Você escolheu uma opção inválida.")
      
  elif menu == "2":
    pokemonSelvagem = pokemons[int(random.randint(0, 25))]
    print (f"""Um {pokemonSelvagem.nome} selvagem apareceu...\n
Decida o que irá fazer.
    1.Usar pokébola
    2.Fugir
    """)
    menuPokemonSelvagem = input()

    if menuPokemonSelvagem == "1":
      jogador.capturarPokemon(pokemonSelvagem)
      print("\n")
    else:
      print("Fugiu com sucesso")
  elif menu == "3":
    pokemon1 = jogador.escolherPokemon()
    pokemon2 = inimigo1.escolherPokemon()
    batalhaPokemon(pokemon1, pokemon2)
    print("\n")
  elif menu == "4":
    print("sair do jogo")
    break
  else:
    print("Digite uma opção valida")


    
