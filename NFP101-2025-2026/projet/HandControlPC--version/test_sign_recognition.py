import cv2
import subprocess
import threading
from utils.hand_tracking import HandDetector

# Patterns: [pouce, index, majeur, annulaire, auriculaire]
SIGNS = {
    "A": [1, 0, 0, 0, 0],   # Poing, pouce sur le côté
    "B": [0, 1, 1, 1, 1],   # 4 doigts levés, pouce replié
    "J": [0, 0, 0, 0, 1],   # Auriculaire seul (crochet)
    "L": [1, 1, 0, 0, 0],   # Index + pouce (pistolet)
    "N": [1, 0, 1, 0, 0],   # Pouce + majeur
    "O": [1, 0, 0, 0, 1],   # Pouce + auriculaire (forme arrondie)
    "R": [0, 1, 0, 0, 0],   # Index seul pointé
    "U": [0, 1, 1, 0, 0],   # Index + majeur (deux doigts côte à côte)
}

BONJOUR_SEQUENCE = list("BONJOUR")

HOLD_FRAMES = 20    # frames stables avant validation (~0.7s à 30fps)
COOLDOWN_FRAMES = 45  # frames d'attente après chaque détection


def recognize_sign(fingers):
    for name, pattern in SIGNS.items():
        if fingers == pattern:
            return name
    return None


def speak(text):
    threading.Thread(target=lambda: subprocess.run(["say", text]), daemon=True).start()


def draw_sequence(img, sequence_progress):
    """Affiche la progression de la séquence BONJOUR."""
    x = 10
    y = img.shape[0] - 50
    for i, letter in enumerate(BONJOUR_SEQUENCE):
        if i < len(sequence_progress):
            color = (0, 220, 0)    # vert = lettre validée
        elif i == len(sequence_progress):
            color = (0, 200, 255)  # jaune = lettre attendue
        else:
            color = (120, 120, 120)  # gris = pas encore atteinte
        cv2.putText(img, letter, (x + i * 45, y),
                    cv2.FONT_HERSHEY_COMPLEX, 1.4, color, 3)


def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    current_sign = None
    hold_counter = 0
    cooldown = 0
    last_detected = None

    sequence_progress = []   # lettres de BONJOUR déjà validées dans l'ordre
    bonjour_said = False

    print("Reconnaissance de signes — épelez B-O-N-J-O-U-R")
    print("Signes disponibles :", ", ".join(SIGNS.keys()))
    print("Appuyez sur ESC pour quitter | R pour réinitialiser la séquence")

    while True:
        success, img = cap.read()
        if not success:
            break

        img = detector.find_hands(img)
        hands = detector.get_landmarks(img)

        detected = None
        if hands:
            fingers = detector.fingers_up(hands[0])
            detected = recognize_sign(fingers)

            # Afficher les doigts détectés (debug)
            cv2.putText(img, str(fingers), (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 2)

        # Logique de stabilisation
        if cooldown > 0:
            cooldown -= 1
        elif detected == current_sign and detected is not None:
            hold_counter += 1
        else:
            current_sign = detected
            hold_counter = 0

        # Validation après HOLD_FRAMES stables
        if hold_counter >= HOLD_FRAMES and detected != last_detected:
            last_detected = detected
            cooldown = COOLDOWN_FRAMES
            hold_counter = 0
            print(f"Signe détecté : {detected}")
            speak(detected)

            # Vérification de la séquence BONJOUR
            if not bonjour_said:
                expected = BONJOUR_SEQUENCE[len(sequence_progress)]
                if detected == expected:
                    sequence_progress.append(detected)
                    if sequence_progress == BONJOUR_SEQUENCE:
                        bonjour_said = True
                        speak("Bonjour")
                        print("BONJOUR épelé ! Séquence complète.")
                else:
                    # Mauvaise lettre : on repart du début
                    if sequence_progress:
                        print(f"Erreur — attendu '{expected}', reçu '{detected}'. Réinitialisation.")
                    sequence_progress = []
                    # Re-tester si la lettre détectée est le premier signe
                    if detected == BONJOUR_SEQUENCE[0]:
                        sequence_progress.append(detected)

        # Barre de progression du geste
        if current_sign and cooldown == 0:
            progress = int((hold_counter / HOLD_FRAMES) * img.shape[1])
            cv2.rectangle(img, (0, img.shape[0] - 15), (progress, img.shape[0]),
                          (0, 255, 100), -1)

        # Affichage du signe courant
        sign_text = current_sign if current_sign else "..."
        color = (0, 255, 0) if cooldown > 0 else (255, 255, 255)
        cv2.putText(img, f"Signe: {sign_text}", (10, 80),
                    cv2.FONT_HERSHEY_COMPLEX, 2, color, 3)

        # Affichage de la séquence BONJOUR
        draw_sequence(img, sequence_progress)

        # Message de félicitations
        if bonjour_said:
            cv2.putText(img, "BONJOUR !", (img.shape[1] // 2 - 160, img.shape[0] // 2),
                        cv2.FONT_HERSHEY_COMPLEX, 2.5, (0, 220, 0), 4)

        # Légende des signes disponibles
        for i, (k, v) in enumerate(SIGNS.items()):
            cv2.putText(img, f"{k}: {v}", (10, 150 + i * 32),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (150, 150, 255), 2)

        cv2.imshow("Reconnaissance de signes — BONJOUR", img)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC
            break
        elif key == ord('r'):  # Réinitialiser la séquence
            sequence_progress = []
            bonjour_said = False
            print("Séquence réinitialisée.")

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
