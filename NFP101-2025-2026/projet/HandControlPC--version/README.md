# HandControlPC

Contrôle gestuel du PC par webcam — détection de mains en temps réel via MediaPipe.

---

## Description

HandControlPC capte les gestes de la main via la webcam et les traduit en actions système macOS :

| Geste | Action |
|-------|--------|
| Index seul levé | Contrôle du volume (pincement pouce-index) |
| 3 doigts levés | Capture d'écran |
| 2 mains avec écartement | Zoom sur le flux vidéo |
| Séquence de signes B-O-N-J-O-U-R | Reconnaissance de signes (épeler « BONJOUR ») |

Le projet est structuré en modules Python avec héritage POO, configuration JSON, et tests unitaires automatisés.

---

## Public cible

Utilisateurs souhaitant contrôler leur PC sans toucher le clavier/souris, ou toute personne intéressée par les interfaces gestuelles.

---

## Prérequis

- Python 3.11+
- macOS (les APIs volume et capture sont macOS-spécifiques)
- Webcam fonctionnelle

---

## Installation

```bash
# 1. Cloner le dépôt
git clone <url-du-depot>
cd HandControlPC--version

# 2. Créer un environnement virtuel
python3.11 -m venv .venv
source .venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt
```

---

## Lancement

```bash
python main.py
```

### Reconnaissance de signes — épeler « BONJOUR »

```bash
python test_sign_recognition.py
```

Épelez les lettres dans l'ordre **B → O → N → J → O → U → R**. Chaque lettre validée
s'affiche en vert ; une erreur réinitialise la séquence (touche `R` pour réinitialiser
manuellement). La séquence complète déclenche une synthèse vocale « Bonjour ».

---

## Tests unitaires

```bash
# Avec l'environnement virtuel activé
python -m pytest tests/ -v
```

Les tests couvrent : la logique de reconnaissance de signes, le calcul de volume, le zoom, le chargement de configuration, et l'héritage des classes.

---

## Configuration

Le fichier `config.json` permet de personnaliser tous les paramètres sans toucher au code :

```json
{
  "camera": { "width": 1280, "height": 720, "index": 0 },
  "volume": { "min": 0, "max": 100 },
  "screenshot": { "folder": "screenshots" }
}
```

---

## Structure du projet

```
HandControlPC--version/
├── main.py                    # Point d'entrée principal
├── test_sign_recognition.py   # Démo reconnaissance de signes
├── config.json                # Configuration personnalisable
├── requirements.txt
├── utils/
│   ├── gesture_action.py      # Classe de base abstraite (ABC)
│   ├── hand_tracking.py       # Détection des mains (MediaPipe)
│   ├── volume_control.py      # Contrôle volume (hérite GestureAction)
│   ├── screenshot.py          # Capture d'écran (hérite GestureAction)
│   ├── zoom_control.py        # Zoom vidéo (hérite GestureAction)
│   └── config_loader.py       # Chargement de la configuration JSON
├── tests/
│   ├── test_gesture_logic.py  # Tests logique gestuelle
│   ├── test_config.py         # Tests configuration
│   └── test_screenshot.py     # Tests héritage et dossiers
└── docs/
    ├── rapport_projet_POO.pdf        # Documentation technique (PDF)
    └── HandControlPC_Presentation.pdf # Support de présentation orale
```

---

## Documentation et démonstration

- **Documentation technique** : [`docs/rapport_projet_POO.pdf`](docs/rapport_projet_POO.pdf) — contexte, architecture, choix techniques, usage IA.
- **Présentation orale** : [`docs/HandControlPC_Presentation.pdf`](docs/HandControlPC_Presentation.pdf).
- **Vidéos de démonstration** : fournies séparément (trop volumineuses pour le dépôt Git).

---

## Permissions macOS requises

- **Accessibilité** : pour PyAutoGUI (contrôle souris/clavier)
- **Enregistrement d'écran** : pour MSS (captures d'écran)

Autoriser ces permissions dans `Réglages système > Confidentialité et sécurité`.

---

## Fonctionnalités détaillées

- **Volume** : pincement pouce-index proportionnel au volume système (0–100%). Retour au menu : ouvrir complètement la main.
- **Screenshot** : lever 3 doigts → maintenir le geste stable (~0.7s) → capture sauvegardée dans `screenshots/` avec horodatage + son de confirmation.
- **Zoom** : approcher ou écarter les index des deux mains pour zoomer/dézoomer le flux vidéo en temps réel.

---

## Limites et pistes d'amélioration

- Contrôle volume et captures limités à macOS (APIs `osascript` et `afplay`)
- La reconnaissance de gestes peut être perturbée par une luminosité faible
- Ajout possible : déplacement de la souris, contrôle des fenêtres, support Windows/Linux
- Ajout possible : persistance des préférences utilisateur, interface de configuration graphique

---

## Usage IA

Deux outils d'IA ont été utilisés et sont déclarés ci-dessous :

| IA | Fichier(s) concerné(s) | Apport |
|----|------------------------|--------|
| **Claude (Anthropic)** | `utils/volume_control.py` (classe `VolumeController`, `_get_volume`, `_set_volume`) | Assistance à l'écriture |
| **Claude (Anthropic)** | `utils/zoom_control.py` (méthode `adjust()`) | Assistance à l'écriture |
| **GitHub Copilot** | `main.py` | Refactorisation légère |

Le code assisté par Claude est encadré dans le code source avec :
```python
# ############### CODE IA (Claude) ################
...
# ########################################
```

---

## Stack technique

- [OpenCV](https://opencv.org/) — Capture et traitement vidéo
- [MediaPipe](https://mediapipe.dev/) — Détection et suivi des mains
- [PyAutoGUI](https://pyautogui.readthedocs.io/) — Contrôle système
- [MSS](https://python-mss.readthedocs.io/) — Capture d'écran
- [NumPy](https://numpy.org/) — Calculs vectoriels
- [pytest](https://pytest.org/) — Tests unitaires
