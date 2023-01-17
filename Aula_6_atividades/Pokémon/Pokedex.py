from movedex import*

class Pokemon: #requisito obrigatório 1
   def __init__(self, apelido, nome, HP, tipos, moves, ataque, defesa, velocidade, especial, status):
     self.apelido = apelido
     self.nome = nome
     self.HP = HP
     self.tipos = tipos
     self.moves = moves
     self.ataque = ataque
     self.defesa = defesa
     self.velocidade = velocidade
     self.especial = especial
     self.status = status
     self.maxHP = HP  

   def listarMoves(self):
     for i in range(len(self.moves)):
       print(f"{i+1}.{self.moves[i].nome}\n")




class InicialGrama(Pokemon):
  def __init__(self, apelido, nome, HP, tipos, moves, ataque, defesa, velocidade, especial, status):
    super().__init__(apelido, nome, HP, tipos, moves, ataque, defesa, velocidade, especial, status)
    self.moves = [moves[142], moves[79], moves[157], moves[101]]


class InicialFogo(Pokemon):
  def __init__(self, apelido, nome, HP, tipos, moves, ataque, defesa, velocidade, especial, status):
    super().__init__(apelido, nome, HP, tipos, moves, ataque, defesa, velocidade, especial, status)
    self.moves = [moves[111], moves[39], moves[45], moves[120]]

class InicialAgua(Pokemon):
  def __init__(self, apelido, nome, HP, tipos, moves, ataque, defesa, velocidade, especial, status):
    super().__init__(apelido, nome, HP, tipos, moves, ataque, defesa, velocidade, especial, status)
    self.moves = [moves[142], moves[158], moves[10], moves[16]]

pokemons_iniciais = [
 InicialGrama("", "Bulbasaur",  45, ["Grama", "Veneno"], moves, 49,  49, 45, 65, "OK"),
                        InicialFogo("","Charmander", 39, ["Fogo", ""], moves, 52, 43, 65, 50, "OK"),
                     InicialAgua("","Squirtle", 44, ["Água", ""], moves, 48, 65, 43, 50, "OK")
]

m = [moves[144], moves[101], moves[79], moves[126]]
    
pokemons = [
   Pokemon("", "Bulbasaur",  45, ["Grama", "Veneno"], [moves[142], moves[101], moves[79], moves[157]], 49,  49, 45, 65, "OK"),
   Pokemon("", "Ivysaur", 60, ["Grama", "Veneno"], [moves[144], moves[101], moves[79], moves[157]], 62, 63, 60, 80, "OK"),
   Pokemon("","Venusaur", 80, ["Grama", "Veneno"], [moves[144], moves[101], moves[79], moves[126]],  82, 83, 80, 100, "OK"),
   Pokemon("","Charmander", 39, ["Fogo", ""], [moves[111], moves[39], moves[120], moves[100]], 52, 43, 65, 50, "OK"),
   Pokemon("","Charmeleon", 58, ["Fogo", ""], [moves[111], moves[45], moves[120], moves[81]], 64, 58, 80, 65, "OK"),
   Pokemon("","Charizard", 78, ["Fogo", "Voador"], [moves[144], moves[45], moves[120], moves[81]], 84, 78, 100, 85, "OK"),
   Pokemon("","Squirtle", 44, ["Água", ""], [moves[142], moves[10], moves[158], moves[15]], 48, 65, 43, 50, "OK"),
   Pokemon("","Wartortle", 59, ["Água", ""], [moves[117], moves[10], moves[16], moves[158]], 63, 80, 58, 65, "OK"),
   Pokemon("","Blastoise", 79, ["Água", ""], [moves[117], moves[139], moves[62], moves[158]], 83, 100, 78,85, "OK"),
   Pokemon("","Caterpie", 45, ["Inseto", ""], [moves[142], moves[10], moves[6], moves[95]], 30, 35, 45, 20, "OK"),
   Pokemon("","Metapod", 50, ["Inseto", ""], [moves[142], moves[10], moves[6], moves[95]],20, 55, 30, 25, "OK"),
   Pokemon("","Butterfree", 60,["Inseto", "Voador"], [moves[142], moves[102], moves[20], moves[96]], 45, 50, 70, 80, "OK"),
   Pokemon("","Weedle", 40, ["Inseto", "Veneno"], [moves[142], moves[10], moves[6], moves[94]], 35, 30, 50, 20, "OK"),
   Pokemon("","Kakuna", 45, ["Inseto", "Veneno"], [moves[142], moves[10], moves[6], moves[94]], 25, 50, 35, 25, "OK"),
   Pokemon("","Beedrill", 65, ["Inseto", "Veneno"], [moves[49], moves[100], moves[155], moves[91]], 80, 40, 75, 45, "OK"),
   Pokemon("","Pidgey", 40,["Normal", "Voador"], [moves[55], moves[102], moves[161], moves[99]], 45, 40, 56, 35, "OK"),
   Pokemon("","Pidgeotto", 63, ["Normal", "Voador"], [moves[99], moves[102], moves[161], moves[47]], 60, 55, 71, 50, "OK"),
   Pokemon("","Pidgeot", 83, ["Normal", "Voador"], [moves[102], moves[118], moves[161], moves[47]], 80, 75, 91, 70, "OK"),
   Pokemon("","Rattata", 30, ["Normal", ""], [moves[142], moves[100], moves[64], moves[99]], 56, 35, 72, 25, "OK"),
   Pokemon("","Raticate", 55,["Normal", ""], [moves[99], moves[12], moves[63], moves[64]] , 81, 60, 97, 50, "OK"),
   Pokemon("","Spearow", 40, ["Normal", "Voador"], [moves[102], moves[118], moves[36], moves[49]], 60, 30, 70, 31, "OK"),
   Pokemon("","Fearow", 65, ["Normal", "Voador"], [moves[102], moves[118], moves[36], moves[49]], 90, 65, 100, 61, "OK"),
   Pokemon("","Ekans", 35,[ "Veneno", ""], [moves[10], moves[1], moves[27], moves[12]], 60, 44, 55, 40, "OK"),
   Pokemon("","Arbok", 60,["Veneno", ""], [moves[10], moves[1], moves[27], moves[12]], 85, 69, 80, 65, "OK"),
   Pokemon("","Pikachu", 35,["Elétrico", ""], [moves[99], moves[140], moves[147], moves[149]], 55, 30, 90, 50, "OK"),
   Pokemon("","Raichu", 60,["Elétrico", ""], [moves[99], moves[140], moves[147], moves[149]], 90, 55, 100, 90, "OK"),
   Pokemon("","Sandshrew", 50,["Terra", ""], ["Tackle"], 75, 85, 40, 30, "OK"),
   Pokemon("","Sandslash", 75,["Terra", ""], ["Tackle"], 100, 110, 65, 55, "OK"),
   Pokemon("","Nidoran♀", 55,["Veneno", ""], ["Tackle"], 47, 52, 41, 40, "OK"),
   Pokemon("","Nidorina", 70,["Veneno", ""], ["Tackle"], 62, 67, 56, 55, "OK"),
   Pokemon("","Nidoqueen", 90, ["Veneno", "Terra"], ["Tackle"], 82, 87, 76, 75, "OK"),
   Pokemon("","Nidoran♂", 46,["Veneno", ""], ["Tackle"], 57, 40, 50, 40, "OK"),
   Pokemon("","Nidorino", 61,["Veneno", ""], ["Tackle"], 72, 57, 65, 55, "OK"),
   Pokemon("","Nidoking", 81,[ "Veneno", "Terra"], ["Tackle"], 92, 77, 85, 75, "OK"),
   Pokemon("","Clefairy", 70,["Normal", ""], ["Tackle"], 45, 48, 35, 60, "OK"),
   Pokemon("","Clefable", 95,["Normal", ""], ["Tackle"], 70, 73, 60, 85, "OK"),
   Pokemon("","Vulpix", 38,["Fogo", ""], ["Tackle"], 41, 40, 65, 65, "OK"),
   Pokemon("","Ninetales", 73,["Fogo", ""], ["Tackle"], 76, 75, 100, 100, "OK"),
   Pokemon("","Jigglypuff", 115,["Normal", ""], ["Tackle"], 45, 20, 20, 25, "OK"),
   Pokemon("","Wigglytuff", 140,["Normal", ""], ["Tackle"], 70, 45, 45, 50, "OK"),
   Pokemon("","Zubat", 40,["Veneno", "Voador"], ["Tackle"], 45, 35, 55, 40, "OK"),
   Pokemon("","Golbat", 75,["Veneno", "Voador"], ["Tackle"], 80, 70, 90, 75, "OK"),
   Pokemon("","Oddish", 45,["Grama", "Veneno"], ["Tackle"], 50, 55, 30, 75, "OK"),
   Pokemon("","Gloom", 60,["Grama", "Veneno"], ["Tackle"], 65, 70, 40, 85, "OK"),
   Pokemon("","Vileplume", 75,["Grama", "Veneno"], ["Tackle"], 80, 85, 50, 100, "OK"),
   Pokemon("","Paras", 35,["Inseto","Grama"], ["Tackle"], 70, 55, 25, 55, "OK"),
   Pokemon("","Parasect", 60,["Inseto","Grama"], ["Tackle"], 95, 80, 30, 80, "OK"),
   Pokemon("","Venonat", 60,["Inseto", "Veneno"], ["Tackle"], 55, 50, 45, 40, "OK"),
   Pokemon("","'Venomoth", 70,["Inseto", "Veneno"], ["Tackle"], 65, 60, 90, 90, "OK"),
   Pokemon("", "Diglett", 10, ["Terra", ""], ["Tackle"], 55, 25, 95, 45, "OK"), 
   Pokemon("", "Dugtrio", 35, ["", ""], ["Tackle"], 80, 50, 120, 70, "OK"),
   Pokemon("", "Meowth", 40, ["Normal", ""], ["Tackle"], 45, 35, 90, 40, "OK"),
   Pokemon("", "Persian", 65, ["Normal", ""], ["Tackle"], 70, 60, 115, 65, "OK"),
   Pokemon ("", "Psyduck", 50, ["Água", ""], ["Tackle"], 52, 48, 55, 50, "OK"),
   Pokemon("", "Golduck", 80, ["Água", ""], ["Tackle"], 82, 78, 85, 80, "OK"),
   Pokemon("", "Mankey", 40, ["Lutador", ""], ["Tackle"], 80, 35, 70, 35, "OK"),
   Pokemon("", "Primeape", 65, ["Lutador", ""], ["Tackle"], 105, 60, 95, 60, "OK"),
   Pokemon("", "Growlithe", 55, ["Fogo", ""], ["Tackle"], 70, 45, 60, 50, "OK"),
   Pokemon("", "Arcanine", 90, ["Fogo", "Veneno"], ["Tackle"], 110, 80, 95, 80, "OK"),
   Pokemon("", "Poliwag", 40, ["Água", ""], ["Tackle"], 50, 40, 90, 40, "OK"),
   Pokemon("", "Poliwhirl", 65, ["Água", ""], ["Tackle"], 65, 65, 90, 50, "OK"),
   Pokemon("", "Poliwrath", 90, ["Água", "Lutador"], ["Tackle"], 85, 95, 70, 70, "OK"),
   Pokemon("", "Abra", 25, ["Psíquico", ""], ["Tackle"], 20, 15, 90, 105, "OK"),
   Pokemon("", "Kadabra", 40, ["Psíquico", ""], ["Tackle"], 35, 30, 105, 120, "OK"),
   Pokemon("", "Alakazam", 55, ["Psíquico", ""], ["Tackle"], 50, 45, 120, 135, "OK"),
   Pokemon("", "Machop", 70, ["Lutador", ""], ["Tackle"], 80, 50, 35, 35, "OK"),
   Pokemon("", "Machoke", 80, ["Lutador", ""], ["Tackle"], 100, 70, 45, 50, "OK"),
   Pokemon("", "Machamp", 90, ["Lutador", ""], ["Tackle"], 130, 80, 55, 65, "OK"),
   Pokemon("", "Bellsprout", 50, ["Grama", "Veneno"], ["Tackle"], 75, 35, 40, 70, "OK"),
   Pokemon("", "Weepinbell", 65, ["Grama", "Veneno"], ["Tackle"], 90, 50, 55, 85, "OK"),
   Pokemon("", "Victreebel", 80, ["Grama", "Veneno"], ["Tackle"], 105, 65, 70, 100, "OK"),
   Pokemon("", "Tentacool", 40, ["Água", "Veneno"], ["Tackle"], 40, 35, 70, 100, "OK"),
   Pokemon("", "Tentacruel", 80, ["Água", "Veneno"], ["Tackle"], 70, 65, 100, 120, "OK"),
   Pokemon("", "Geodude", 40, ["Pedra", "Terra"], ["Tackle"], 80, 100, 20, 30, "OK"),
   Pokemon("", "Graveler", 55, ["Pedra", "Terra"], ["Tackle"], 95, 115, 35, 45, "OK"),
   Pokemon("", "Golem", 80, ["Pedra", "Terra"], ["Tackle"], 110, 130, 45, 55, "OK"),
   Pokemon("", "Ponyta", 50, ["Fogo", ""], ["Tackle"], 85, 55, 90, 65, "OK"),
   Pokemon("", "Rapidash", 65, ["Fogo", ""], ["Tackle"], 100, 70, 105, 80, "OK"),
   Pokemon("", "Slowpoke", 90, ["Água", "Psíquico"], ["Tackle"], 65, 65, 15, 40, "OK"),
   Pokemon("", "Slowbro", 95, ["Água", "Psíquico"], ["Tackle"], 75, 110, 30, 80, "OK"),
   Pokemon("", "Magnemite", 25, ["Elétrico", ""], ["Tackle"], 35, 70, 45, 95, "OK"),
   Pokemon("", "Magneton", 50, ["Elétrico", ""], ["Tackle"], 60, 95, 70, 120, "OK"),
   Pokemon("", "Farfetchd", 52, ["Normal", "Voador"], ["Tackle"], 65, 55, 60, 58, "OK"),
   Pokemon("", "Doduo", 35, ["Normal", "Voador"], ["Tackle"], 85, 45, 75, 35, "OK"),
   Pokemon("", "Dodrio", 60, ["Normal", "Voador"], ["Tackle"], 110, 70, 100, 60, "OK"),
   Pokemon("", "Seel", 65, ["Água", ""], ["Tackle"], 45, 55, 45, 70, "OK"),
   Pokemon("", "Dewgong", 90, ["Água ", "Gelo"], ["Tackle"], 70, 80, 70, 95, "OK"),
   Pokemon("", "Grimer", 80, ["Veneno", ""], ["Tackle"], 80, 50, 25, 40, "OK"),
   Pokemon("", "Muk", 105, ["Veneno", ""], ["Tackle"], 105, 75, 50, 65, "OK"),
   Pokemon ("", "Shellder", 30, ["Água", ""], ["Tackle"], 65, 100, 40, 45, "OK"),
   Pokemon("", "Cloyster", 50, ["Água", "Gelo"], ["Tackle"], 95, 180, 70, 85, "OK"),
   Pokemon("", "Gastly", 30, ["Fantasma", "Veneno"], ["Tackle"], 35, 30, 80, 100, "OK"),
   Pokemon("", "Haunter", 45, ["Fantasma", "Veneno"], ["Tackle"], 50, 45, 95, 115, "OK"),
   Pokemon ("", "Gengar", 60, ["Fantasma", "Veneno"], ["Tackle"], 65, 60, 110, 130, "OK"),
   Pokemon ("", "Onix", 35, ["Pedra", "Terra"], ["Tackle"], 45, 160, 70, 30, "OK"),
   Pokemon("", "Drowzee", 60, ["Psíquico", ""], ["Tackle"], 48, 45, 42, 90, "OK"),
   Pokemon("", "Hypno", 85, ["Psíquico", ""], ["Tackle"], 73, 70, 67, 115, "OK"),
   Pokemon("", "Krabby", 30, ["Água", ""], ["Tackle"], 105, 90, 50, 25, "OK"),
   Pokemon("", "Kingler", 55, ["Água", ""], ["Tackle"], 130, 115, 75, 50, "OK"),
   Pokemon("", "Voltorb", 40, ["Elétrico", ""], ["Tackle"], 30, 50, 100, 55, "OK"),
   Pokemon("", "Electrode", 60, ["Elétrico", ""], ["Tackle"], 50, 70, 140, 80, "OK"),
   Pokemon("", "Exeggcute", 60, ["Grama", "Psíquico"], ["Tackle"], 40, 80, 40, 60, "OK"),
   Pokemon ("", "Exeggutor", 95, ["Grama", "Psíquico"], ["Tackle"], 95, 85, 55, 125, "OK"),
   Pokemon("", "Cubone", 50, ["Terra", ""], ["Tackle"], 50, 95, 95, 35, "OK"),
   Pokemon("", "Marowak", 60, ["Terra", ""], ["Tackle"], 80, 110, 45, 50, "OK"),
   Pokemon("", "Hitmonlee", 50, ["Lutador", ""], ["Tackle"], 120, 53, 87, 35, "OK"),
   Pokemon("", "Hitmonchan", 50, ["Lutador", ""], ["Tackle"], 105, 79, 76, 35, "OK"),
   Pokemon("", "Lickitung", 90, ["Normal", ""], ["Tackle"], 55, 75, 30, 60, "OK"),
   Pokemon("", "Koffing", 40, ["Veneno", ""], ["Tackle"], 65, 95, 35, 60, "OK"),
   Pokemon("", "Weezing", 65, ["Veneno", ""], ["Tackle"], 90, 120, 60, 85, "OK"),
   Pokemon("", "Rhyhorn", 80, ["Terra", "Pedra"], ["Tackle"], 85, 95, 25, 30, "OK"),
   Pokemon("", "Rhydon", 105, ["Terra", "Pedra"], ["Tackle"], 130, 120, 40, 45, "OK"),
   Pokemon("", "Chansey", 250, ["Normal", ""], ["Tackle"], 5, 5, 50, 105, "OK"),
   Pokemon("", "Tangela", 65, ["Grama", ""], ["Tackle"], 55, 115, 60, 100, "OK"),
   Pokemon("", "Kangaskhan", 105, ["Normal", ""], ["Tackle"], 95, 80, 90, 40, "OK"),
   Pokemon("", "Horsea", 30, ["Água", ""], ["Tackle"], 40, 70, 60, 70, "OK"),
   Pokemon("", "Seadra", 55, ["Água", ""], ["Tackle"], 65, 95, 85, 95, "OK"),
   Pokemon("", "Goldeen", 45, ["Água", ""], ["Tackle"], 67, 60, 63, 50, "OK"),
   Pokemon("", "Seaking", 80, ["Água", ""], ["Tackle"], 92, 65, 68,80, "OK"),
   Pokemon("", "Staryu", 30, ["Água", ""], ["Tackle"], 45, 55, 85, 70, "OK"),
   Pokemon("", "Starmie", 60, ["Água", "Psíquico"], ["Tackle"], 75, 85, 115, 100, "OK"),
   Pokemon("", "Mr. Mime", 40, ["Psíquico", ""], ["Tackle"], 45, 65, 90, 100, "OK"),
   Pokemon("", "Scyther", 70, ["Inseto", "Voador"], ["Tackle"], 110, 80, 105, 55, "OK"),
   Pokemon("", "Jynx", 65, ["Psíquico", "Gelo"], ["Tackle"], 50, 35, 95, 95, "OK"),
   Pokemon("", "Electabuzz", 65, ["Elétrico", ""], ["Tackle"], 83, 57, 105, 85, "OK"),
   Pokemon("", "Magmar", 65, ["Fogo", ""], ["Tackle"], 95, 57, 93, 85, "OK"),
   Pokemon("", "Pinsir", 65, ["Inseto", ""], ["Tackle"], 125, 100, 85, 55, "OK"),
   Pokemon("", "Tauros", 75, ["Normal", ""], ["Tackle"], 100, 95, 110, 70, "OK"),
   Pokemon("", "Magikarp", 20, ["Água", ""], ["Tackle"], 10, 55, 80, 20, "OK"),
   Pokemon("", "Gyarados", 95, ["Água", ""], ["Tackle"], 125, 79, 81, 100, "OK"),
   Pokemon("", "Lapras", 130, ["Água", "Gelo"], ["Tackle"], 85, 80, 60, 95, "OK"),
   Pokemon("", "Ditto", 48, ["Normal", ""], ["Tackle"], 48, 48, 48, 48, "OK"),
   Pokemon("", "Eevee", 55, ["Normal", ""], ["Tackle"], 55, 50, 55, 65, "OK"),
   Pokemon("", "Vaporeon", 130, ["Água", ""], ["Tackle"], 65, 60, 65, 110, "OK"),
   Pokemon("", "Jolteon", 65, ["Elétrico", ""], ["Tackle"], 65, 60, 130, 110, "OK"),
   Pokemon("", "Flareon", 65, ["Fogo", ""], ["Tackle"], 130, 60, 65, 110, "OK"),
   Pokemon("", "Porygon", 65, ["Normal", ""], ["Tackle"], 60, 70, 40, 75, "OK"),
   Pokemon("", "Omanyte", 35, ["Pedra", "Água"], ["Tackle"], 40, 100, 35, 90, "OK"),
   Pokemon ("", "Omastar", 70, ["Pedra", "Água"], ["Tackle"], 60, 125, 55, 115, "OK"),
   Pokemon ("", "Kabuto", 30, ["Pedra", "Água"], ["Tackle"], 80, 90, 55, 45, "OK"),
   Pokemon ("", "Kabutops", 60, ["Pedra", "Água"], ["Tackle"], 115, 105, 80, 70, "OK"),
   Pokemon("", "Aerodactyl", 80, ["Pedra", "Voador"], ["Tackle"], 105, 65, 130, 60, "OK"),
   Pokemon("", "Snorlax", 160, ["Normal", ""], ["Tackle"], 110, 65, 30, 65, "OK"),
   Pokemon("", "Articuno", 90, ["Gelo", "Voador"], ["Tackle"], 85, 100, 85, 125, "OK"),
   Pokemon("", "Zapdos", 90, ["Elétrico", "Voador"], ["Tackle"], 90, 85, 100, 125, "OK"),
   Pokemon("", "Moltres", 90, ["Fogo", "Voador"], ["Tackle"], 100, 90, 90, 125, "OK"),
   Pokemon("", "Dratini", 41, ["Dragão", ""], ["Tackle"], 64, 45, 50, 50, "OK"),
   Pokemon("", "Dragonair", 61, ["Dragão", ""], ["Tackle"], 84, 65, 70, 70, "OK"),
   Pokemon("", "Dragonite", 91, ["Dragão", "Voador"], ["Tackle"], 134, 95, 80, 100, "OK"),
   Pokemon("", "Mewtwo", 106, ["Psíquico", ""], ["Tackle"], 110, 90, 130, 154, "OK"),
   Pokemon ("", "Mew", 100, ["Psíquico", ""], ["Tackle"], 100, 100, 100, 100, "OK")]
