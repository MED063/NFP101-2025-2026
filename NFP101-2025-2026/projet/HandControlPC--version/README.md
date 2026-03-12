# HandControlPC

Controle gestuel du PC par webcam, utilisant la detection de mains en temps reel.

## Description

HandControlPC capte les gestes de la main via la webcam et les traduit en actions systeme :

| Geste | Action |
|-------|--------|
| Pincement pouce-index | Controle du volume (macOS) |
| 3 doigts leves | Capture d'ecran |
| 2 mains avec ecartement | Zoom sur le flux video |

## Prerequis

- Python 3.11+
- macOS (le controle du volume et les captures utilisent des APIs macOS)
- Webcam fonctionnelle

## Installation

```bash
pip install -r requirements.txt
```

## Lancement

```bash
python main.py
```

## Permissions macOS requises

- **Accessibilite** : pour PyAutoGUI (controle souris/clavier)
- **Enregistrement d'ecran** : pour MSS (captures d'ecran)

Autoriser ces permissions dans `Reglages systeme > Confidentialite et securite`.

## Stack technique

- [OpenCV](https://opencv.org/) - Capture et traitement video
- [MediaPipe](https://mediapipe.dev/) - Detection et suivi des mains
- [PyAutoGUI](https://pyautogui.readthedocs.io/) - Controle de la souris
- [MSS](https://python-mss.readthedocs.io/) - Capture d'ecran
- [NumPy](https://numpy.org/) - Calculs vectoriels
