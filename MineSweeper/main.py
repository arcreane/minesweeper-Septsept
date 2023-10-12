import display
import StartGame
import engine

# Lancement du jeu
display.header()

# Variables de difficultés
width, height, bombs = StartGame.difficulty()

# Placement des mines
mines_map = StartGame.set_mines(width, height, bombs)

# Création de la map
displayed_map = list(width * height * "█")

# Affichage de la map de mine
display.display_map(mines_map, width)

# Ajout du display de la map
engine.play(width, height, bombs, displayed_map, mines_map)
