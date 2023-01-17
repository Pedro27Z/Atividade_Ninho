class Move:
  def __init__(self, nome, tipo, categoria, poder, precisao, pp):
    self.nome = nome
    self.tipo = tipo
    self.categoria = categoria
    self.poder = poder
    self.precisao = precisao
    self.pp = pp

moves = [
  Move("Absorção", "Grama", "Especial", 20, 10, 20),#Absorb
  Move("Ácido", "Veneno", "Físico", 40, 10, 30),#Acid
  Move("Armadura Ácida", "Veneno", "Status", "", "", 30),#Acid Armor                   
  Move("Agilidade", "Psíquico", "Status", "", "", 30),#Agility
  Move("Amnésia", "Psíquico", "Status", "", "", 20),#Amnesia
  Move("Raio Aurora", "Gelo", "Especial", 65, 10, 20),#Aurora Beam
  Move("Barragem", "Normal", "Físico", 15, 8, 20),#Barrage
  Move("Barreira", "Psíquico", "Status", "", "", 30),#Barrier
  Move("Resistência", "Normal", "Físico", "", "", 10),#Bide
  Move("Ligação", "Normal", "Físico", 15, 7, 20),#Bind
  Move("Mordida", "Normal", "Físico", 60, 10, 25),#Bite
  Move("Nevasca", "Gelo", "Especial", 120, 9, 5),#Blizzard
  Move("Ataque de Corpo", "Normal", "Físico", 85, 10, 15),#Body Slam
  Move("Bastão de Osso", "Terra", "Físico", 65, 8, 20),#Bone Club
  Move("Ossomerangue", "Normal", "Físico", 50, 9, 10),#Bonemerang
  Move("Bolhas", "Água", "Especial", 20, 10, 30),#Bubble
  Move("Jato de Bolhas", "Água", "Especial", 65, 10, 20),#Bubblebeam
  Move("Clamp", "Água", "Especial", 35, 7, 10),#Clamp
  Move("Punho Cometa", "Normal", "Físico", 18, 8, 15),#Comet Punch
  Move("Raio de Confusão", "Fantasma", "Status", "", 10, 10),#Confuse Ray
  Move("Contrair", "Normal", "Físico", 10, 10, 35),#Constrict
  Move("Confusão", "Psíquico", "Especial", 50, 10, 25),#Confusion
  Move("Conversão", "Normal", "Status", "", "", 30),#Conversion
  Move("Contra-ataque", "Lutador", "Físico", 1, 10, 20),#Counter
  Move("Martelo", "Água", "Especial", 90, 8, 10),#Crab Hammer
  Move("Cortar", "Normal", "Físico", 50, 9, 30),#Cut
  Move("Espiral de Defesa", "Normal", "Status", "", "", 40),#Defense Curl
  Move("Cavar", "Terra", "Físico", 100, 10, 10),#Dig
  Move("Desabilitar", "Normal", "Status", "", 5, 20),#Disable
  Move("Soco Atordoante", "Normal", "Físico", 70, 10, 10),#Dizzy Punch
  Move("Chute Duplo", "Lutador", "Físico", 30, 10, 30),#Double Kick
  Move("Tapa Duplo", "Normal", "Físico", 15, 8, 10),#Double Slap
  Move("Time Duplo", "Normal", "Status", "", "", 15),#Double Team
  Move("Faca de 2 Gumes", "Normal", "Físico", 18, 8, 15),#Double Edge
  Move("Fúria do Dragão", "Dragão", "Especial", 1, 10, 10),#Dragon Rage
  Move("Devorador de Sonhos", "Psíquico", "Especial", "", 10, 10),#Dream Eater
  Move("Bico Broca", "Voador", "Físico", 80, 10, 20),#Drill Peck
  Move("Terremoto", "Terra", "Físico", 100, 10, 10),#Earthquake
  Move("Bomba de Ovo", "Normal", "Físico", 100, 7, 10),#Egg Bomb
  Move("Brasa", "Fogo", "Especial", 40, 10, 25),#Ember
  Move("Explosão", "Normal", "Físico", 170, 10, 5),#Explosion
  Move("Explosão de Fogo", "Fogo", "Especial", 120, 8, 5),#Fire Blast
  Move("Punho de Fogo", "Fogo", "Especial", 75, 10, 15),#Fire Punch
  Move("Chama Furacão", "Fogo", "Especial", 15, 7, 15),#Fire Spin
  Move("Fissura", "Terra", "Físico", "", 3, 5),#Fissure
  Move("Lança-chamas", "Fogo", "Especial", 90, 10, 15),#Flamethrower
  Move("Flash", "Normal", "Status", "", 7, 20),#Flash
  Move("Voar", "Voador", "Físico", 70, 9, 15),#Fly
  Move("Foco de Energia", "Normal", "Status", "", "", 30),#Focus Energy
  Move("Ataque de Fúria", "Normal", "Físico", 15, 8, 20),#Fury Attack
  Move("Golpes de Fúria", "Normal", "Físico", 18, 8, 15),#Fury Swipes
  Move("Olhar Penetrante", "Normal", "Status", "", 7, 30),#Glare
  Move("Rosnar", "Normal", "Status", "", 10, 40),#Growl
  Move("Crescimento", "Normal", "Status", "", "", 40),#Growth
  Move("Guilhotina", "Normal", "Físico", "", 3, 5),#Guilhotine
  Move("Redemoinho", "Normal", "Físico", 40, 10, 35),#Gust
  Move("Endurecer", "Normal", "Status", "", "", 30),#Harden
  Move("Nevoeiro", "Gelo", "Status", "", "", 30),#Haze
  Move("Cabeçada", "Normal", "Físico", 70, 10, 15),#Headbutt
  Move("Super Voadora", "Lutador", "Físico", 85, 9, 20),#High Jump Kick
  Move("Ataque de Chifre", "Normal", "Físico", 65, 10, 25),# Horn Attack
  Move("Chifre Broca", "Normal", "Físico", "", 30, 5),#Horn Drill
  Move("Hidrobomba", "Água", "Especial", 120, 8, 5),#Hidro Pump
  Move("Hiper Raio", "Normal", "Físico", 150, 9, 5),#Hyper Beam
  Move("Hiper Presas", "Normal", "Físico", 80, 9, 15),#Hyper Fang
  Move("Hipnose", "Psíquico", "Status", "", 6, 20),#Hypnosis
  Move("Raio de Gelo", "Gelo", "Especial", 15, 8, 20),#Ice Beam
  Move("Punho de Gelo", "Gelo", "Especial", 75, 10, 15),#Ice Punch
  Move("Voadora", "Lutador", "Físico", 70, 9, 25),#Jump Kick
  Move("Golpe de Karatê", "Normal", "Físico ", 50, 10, 25),#Karate Chop
  Move("Cinese", "Psíquico", "Status", "", 8, 15),
  #Kinesis
  Move("Sanguessuga", "Inseto", "Físico", 20, 10, 15),#Leech Life
  Move("Semente Sanguessuga", "Grama", "Status", "", 9, 10),#Leech Seed
  Move("Encarar", "Normal", "Status", "", 10, 30),#Leer
  Move("Lambida", "Fantasma", "Físico", 20, 10, 30),#Lick
  Move("Tela de Luz", "Psíquico", "Status", "", "", 30),#Light Screen
  Move("Beijo Amoroso", "Normal", "Status", "", 7, 10),#Lovely Kiss
  Move("Rasteira", "Lutador", "Físico", 50, 9, 20),#Low Kick
  Move("Meditação", "Psíquico", "Status", "", "", 40),#Meditate
  Move("Megadreno", "Grama", "Especial", 40, 10, 10),#Mega Drain
  Move("Mega Chute", "Normal", "Físico", 120, 7, 5),#Mega Kick
  Move("Mega Soco", "Normal", "Físico", 80, 8, 20),#Mega Punch
  Move("Metrônomo", "Normal", "Status", "", "", 10),#Metronome
  Move("Mímica", "Normal", "Status", "", 10, 10),#Mimic
  Move("Minimizar", "Normal", "Status", "", "", 20),#Minimize
  Move("Espelho", "Voador", "Status", "", "", 20),#Mirror Move
  Move("Névoa", "Gelo", "Status", "", "", 20),#Mist
  Move("Sombra Noturna", "Fantasma", "Físico", 1, 10, 15),#Night Shade
  Move("Dia de Pagamento", "Normal", "Físico", 40, 10, 20),#Pay Day
  Move("Bicada", "Voador", "Físico", 35, 10, 35),#Peck
  Move("Dança das Pétalas", "Grama", "Especial", 70, 10, 20),#Petal Dance
  Move("Míssel de Espinhos", "Inseto", "Físico", 14, 8, 20),#Pin Missile
  Move("Gás Venenoso", "Veneno", "Status", "", 5, 40),#Poison Gas
  Move("Pó Venenoso", "Veneno", "Status", "", 7, 35),#Poison Powder
  Move("Ferrão Venenoso", "Veneno", "Físico", 15, 10, 35),#Poison Sting
  Move("Lapada", "Normal", "Físico", 40, 10, 35),#Pound
  Move("Psíquico", "Psíquico", "Especial", 65, 10, 20),#Psychic
  Move("Raio Psíquico", "Psíquico", "Especial", 90, 10, 10),#Psybeam
  Move("Onda Psíquica", "Psíquico", "Especial", 1, 8, 15),#Psywave
  Move("Ataque Rápido", "Normal", "Físico", 40, 10, 30),#Quick Attack
  Move("Fúria", "Normal", "Físico", 20, 10, 20),#Rage
  Move("Folha Navalha", "Grama", "Especial", 55, 9, 25),#Razor Leaf
  Move("Vento Cortante", "Normal", "Físico", 80, 7, 10),#Razor Wind
  Move("Recuperação", "Normal", "Status", "", "", 20),#Recover
  Move("Refletir", "Psíquico", "Status", "", "", 20),#Reflect
  Move("Descansar", "Psíquico", "Status", "", "", 10),#Rest
  Move("Rugido", "Normal", "Status", "", 10, 20),#Roar
  Move("Deslizamento de Rocha", "Pedra", "Físico", 75, 9, 10),#Rock Slide
  Move("Arremesso de Rocha", "Normal", "Físico", 50, 6, 15),#Rock Throw
  Move("Chute Giratório", "Lutador", "Físico", 60, 8, 15),#Rolling Kick
  Move("Ataque de Areia", "Normal", "Status", "", 10, 15),#Sand Attack
  Move("Arranhão", "Normal", "Físico", 40, 10, 35),#Scratch
  Move("Som Agudo", "Normal", "Status", "", 8, 40),#Screech
  Move("Arremesso Sísmico", "Lutador", "Físico", 1, 10, 20),#Seismic Toss
  Move("Auto-destruição", "Normal", "Físico", 130, 10, 5),#Self Destruct
  Move("Afiar", "Normal", "Status", "", "", 30),#Sharpen
  Move("Canção de Ninar", "Normal", "Status", "", 5, 15),#Sing
  Move("Quebra Crânio", "Normal", "Físico", 100, 10, 15),#Skull Bash
  Move("Ataque Aéreo", "Voador", "Físico", 140, 9, 5),#Sky Attack
  Move("Pancada", "Normal", "Físico", 80, 7, 20),#Slam
  Move("Cortante", "Normal", "Físico", 70, 10, 20),#Slash
  Move("Pó do Sono", "Grama", "Status", "", 7, 15),#Sleep Powder
  Move("Lodo", "Veneno", "Físico", 65, 10, 20), #Sludge
  Move("Poluição", "Veneno", "Físico", 20, 7, 20),#Smog
  Move("Cortina de Fumaça", "Normal", "Status", "", 10, 20),#Smokescreen
  Move("Cozidos", "Normal", "Status", "", "",10),#Soft-boiled
  Move("Raio Solar", "Grama", "Especial", 120, 10, 10),#Solar Beam
  Move("Explosão Sônica", "Normal", "Físico", 1, 9, 20),#Sonic Boom
  Move("Splash", "Normal", "Status", "", "", 20),#Splash
  Move("Esporos", "Grama", "Status", "", 10, 20),#Spore
  Move("Pisotear", "Normal", "Físico", 65, 10, 20),#Stomp
  Move("Força", "Normal", "Físico", 80, 10, 15),#Strength
  Move("Estilingada", "Inseto", "Status", "", 9, 40),#String Shot
  Move("Insistência", "Normal", "Físico", 50, 10, 10),#Strugle
  Move("Esporos Paralizantes", "", "Status", "", 7, 30),#Stun Spore
  Move("Submissão", "Lutador", "Físico", 80, 8, 25),#Submission
  Move("Substituto", "Normal", "Status", "", "", 10),#Substitute
  Move("Super Presas", "Normal", "Físico", 1, 9, 10),#Super Fang
  Move("Supersônico", "Normal", "Status", "", 5, 20),#Super Fang
  Move("Surf", "Água", "Especial", 95, 10, 15),#Surf
  Move("Ataque Veloz", "Normal", "Físico", 60, "", 20),#Swift
  Move("Dança das Espadas", "Normal", "Status", "", "", 30),#Sword Dance
  Move("Investida", "Normal", "Físico", 35, 9, 35),#Tackle
  Move("Chicote de Cauda", "Normal", "Status", "", 10, 30),#Tail Whip
  Move("Derrubada", "Normal", "Físico", 90, 8, 20),#Take Down
  Move("Teleporte", "Psíquico", "Status", "", "", 20),#Teleport
  Move("Castigar", "Normal", "Físico", 90, 10, 20),#Thrash
  Move("Trovão", "Elétrico", "Especial", 120, 7, 10),#Thunder
  Move("Punho do Trovão", "Elétrico", "Especial", 75, 10, 15),#Thunder Punch
  Move("Trovoada", "Elétrico", "Especial", 40, 10, 30),#Thundershock
  Move("Onda de Choque", "Elétrico", "Status", "", 10, 20),#Thunder Wave
  Move("Choque do Trovão", "Elétrico", "Especial", 95, 10, 15),#Thunderbolt
  Move("Tóxico", "Veneno", "Status", "", 8, 20),#Toxic
  Move("Transformar", "Normal", "Status", "", "", 10),#Transform
  Move("Triataque", "Normal", "Físico", 80, 10, 10),#Triattack
  Move("Agulhas Gêmeas", "Inseto", "Físico", 25, 10, 20),#Twineedle
  Move("Prensa das Garras", "Normal", "Físico", 55, 10, 30),#Vice Grip
  Move("Chicote de Vinha", "Grama", "Especial", 35, 10,10),#Vine Whip
  Move("Jato D'água", "Água", "Especial", 40, 10, 25),#Water Gun
  Move("Cachoeira", "Água", "Especial", 80, 10, 15),#Waterfall
  Move("Ataque de Vento", "Normal", "Status", "", 8, 20),#Whirlwind
  Move("Ataque de Asas", "Voador", "Físico", 35, 10, 35),#Wing Attack
  Move("Retirada", "Água", "Status", "", "", 40),#Withdraw
  Move("Embrulhar", "Normal", "Físico", 15, 8, 20),#Wrap
]

