import display
import StartGame
import engine

# Lancement du jeu
display.header()

# Variables de difficultés
Width, Height, Bombs = StartGame.difficulty()

# Placement des mines
Mines = StartGame.set_mines(Width, Height, Bombs)

# Création de la map
Map = list(Width*Height*"█")

# Ajout du display de la map
display.display_map(Map, Width)
