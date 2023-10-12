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
Map = list(Width * Height * "█")

# Affichage de la map de mine
display.display_map(Mines, Width)
print("\n")

# Ajout du display de la map
engine.play(Width, Height, Bombs, Map, Mines)
