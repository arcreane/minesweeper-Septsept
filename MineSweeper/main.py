import display
import StartGame

# Lancement du jeu
display.header()

# Variables de difficultés
Width, Height, Bombs = StartGame.difficulty()

# Définition de la map
Map = StartGame.set_map(Width, Height, Bombs)

# Ajout du display de la map
display.display_map(Map, Width)

