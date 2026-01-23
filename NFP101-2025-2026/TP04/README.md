# Snake Game : TP04

**Date de rendu:** 23/01/2026

**Auteur:** Mohamed Amine Sobhi


**Module:** Programmation orientée objet en Python, Java et autres, code UE : NF101

  

**Année:** 2025-2026  

## Description

  

Implémentation d'un jeu Snake en Python avec Pygame, développé dans le cadre du TP04 noté. Démontre la programmation orientée objet avec encapsulation, héritage et polymorphisme.

  

## Architecture du projet

```
TP04/
├── snake.py                              # Point d'entrée principal
├── entities/                             # Module des entités
│   ├── __init__.py
│   ├── entity.py                         # Classe de base Entity
│   ├── moving_entity.py                  # Classe MovingEntity
│   ├── snake_entity.py                   # Classe Snake
│   └── food.py                           # Classe Food
├── game/                                 # Module du jeu
│   ├── __init__.py
│   └── game.py                           # Classe Game
├── executables/                          # Exécutables pré-compilés
│   ├── executable_Windows/
│   │   └── snake.exe                     # Windows
│   └── executable_MacOS/
│       └── SnakeGame                     # macOS
├── demos_D_Installation_Et_du_Jeu/       # Vidéos démo
│   ├── demo_Windows/
│   │   ├── lancement_Exe.mp4
│   │   └── installation_Lancement.mp4
│   ├── demo_MacOs/
│   │   └── demoMacOs.mp4
│   └── demo_Linux/
│       └── demo_Linux.mp4
├── requirements.txt                      # Dépendances Python
└── TP04.pdf                              # Énoncé du TP
```

  

## Installation

  

```bash

# Créer un environnement virtuel

python -m  venv  venv

  

# Activer l'environnement

source venv/bin/activate  # macOS/Linux

venv\Scripts\activate # Windows

  

# Installer les dépendances

pip install  -r  requirements.txt

```

  

## Lancement du jeu

### Méthode 1: Exécutables pré-compilés (recommandé)

Des exécutables sont fournis pour Windows et macOS:

**Windows:**
```bash
# Double-cliquer sur executables/executable_Windows/snake.exe
# OU via terminal:
executables/executable_Windows/snake.exe
```

**macOS:**
```bash
# Double-cliquer sur executables/executable_MacOS/SnakeGame
# OU via terminal:
./executables/executable_MacOS/SnakeGame
```

**Vidéos démo:**
- Windows: `demos_D_Installation_Et_du_Jeu/demo_Windows/lancement_Exe.mp4`
- macOS: `demos_D_Installation_Et_du_Jeu/demo_MacOs/demoMacOs.mp4`
- Linux: `demos_D_Installation_Et_du_Jeu/demo_Linux/demo_Linux.mp4`

### Méthode 2: Script Python

```bash
python snake.py
```

## Contrôles

  

-  **Flèches**: Diriger le serpent

-  **P**: Pause/Reprendre

-  **ESPACE/ENTRÉE**: Démarrer/Rejouer

-  **M**: Retour au menu (après game over)

-  **ESC**: Quitter

  

## Règles

  

1. Mangez la nourriture (rouge) pour grandir (+10 points)

2. Évitez les murs

3. Ne vous mordez pas vous-même

4. Le serpent ne peut pas faire demi-tour instantanément

  

## Réponses aux questions du TP

  

### 1. Rôles de Snake, Food, Game

  

-  **Snake**: Gère le serpent (déplacement, croissance, collisions)

-  **Food**: Gère la nourriture (position aléatoire, respawn)

-  **Game**: Orchestre le jeu (boucle, événements, score, affichage)

  

### 2. Pourquoi l'accès direct à `_body` est dangereux

  

Accès direct comme `snake._body.append((100, 100))` pourrait:

- Créer des discontinuités dans le corps

- Casser la cohérence avec `_grow_pending`

- Ajouter des segments hors grille

- Provoquer des bugs de collision

  

L'encapsulation via `get_body()` retourne une copie, protégeant l'état interne.

  

### 3. Polymorphisme et interface

  

Snake et Food implémentent l'interface Entity:

-  `update(game)`: Mise à jour

-  `draw(screen)`: Affichage

  

Le Game traite uniformément toutes les entités:

```python

for e in  self.entities:

e.update(self)

e.draw(self.screen)

```

  

### 4. Pourquoi `Food.update()` existe mais ne fait rien

  

- Respecte l'interface Entity

- Permet le polymorphisme dans la boucle

- Facilite les extensions futures

- Maintient une architecture cohérente

  

### 5. Logique factorisée par MovingEntity

  

- Direction (`_dx`, `_dy`)

- Paramètres globaux (`CELL_SIZE`, `DEFAULT_SPEED`)

- Méthode `set_direction()`

- Évite la duplication de code

  

### 6. CELL_SIZE et DEFAULT_SPEED en attributs de classe

  

Attributs de classe car:

-  **Partagés** par toutes les instances

-  **Cohérence**: même grille pour tous

-  **Modification globale**: un changement affecte tout

-  **Économie mémoire**: une seule copie

  

### 7. Protection par `set_cell_size()`

  

```python

MovingEntity.set_cell_size(-10) # Lève ValueError

MovingEntity.set_cell_size(0) # Lève ValueError

```

  

Sans validation: division par zéro, affichage invalide, boucles infinies.

  

### 8. Héritage vs alternatives

  

**Avec héritage (choix actuel):**

- Code factorié (DRY)

- Hiérarchie claire: Snake "est une" entité mobile

- Polymorphisme simple

- Extension facile

  

## Code avec IA

  

Les parties développées avec assistance IA sont marquées:

```python

# ############### CODE IA ################

# Code amélioré avec IA

# ########################################

```

  
