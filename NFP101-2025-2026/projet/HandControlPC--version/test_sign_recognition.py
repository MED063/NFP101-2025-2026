import cv2
import subprocess
import threading
from utils.hand_tracking import HandDetector

# Patterns: [pouce, index, majeur, annulaire, auriculaire]
SIGNS = {
    "A": [1, 0, 0, 0, 0],  # Poing, pouce sur le cote
    "B": [0, 1, 1, 1, 1],  # 4 doigts leves, pouce replie
    "L": [1, 1, 0, 0, 0],  # Index + pouce (forme pistolet)
}

HOLD_FRAMES = 20   # frames stables avant validation (~0.7s a 30fps)
COOLDOWN_FRAMES = 45  # frames d'attente apres chaque detection


def recognize_sign(fingers):
    for name, pattern in SIGNS.items():
        if fingers == pattern:
            return name
    return None


def speak(text):
    threading.Thread(target=lambda: subprocess.run(["say", text]), daemon=True).start()


def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    current_sign = None
    hold_counter = 0
    cooldown = 0
    last_detected = None

    print("Test langage des signes - A, B, L")
    print("Appuyez sur ESC pour quitter")

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

            # Afficher les doigts detectes (debug)
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

        # Validation apres HOLD_FRAMES stables
        if hold_counter >= HOLD_FRAMES and detected != last_detected:
            last_detected = detected
            cooldown = COOLDOWN_FRAMES
            hold_counter = 0
            print(f"Signe detecte: {detected}")
            speak(detected)

        # Barre de progression
        if current_sign and cooldown == 0:
            progress = int((hold_counter / HOLD_FRAMES) * img.shape[1])
            cv2.rectangle(img, (0, img.shape[0] - 15), (progress, img.shape[0]),
                          (0, 255, 100), -1)

        # Affichage principal
        sign_text = current_sign if current_sign else "..."
        color = (0, 255, 0) if cooldown > 0 else (255, 255, 255)
        cv2.putText(img, f"Signe: {sign_text}", (10, 80),
                    cv2.FONT_HERSHEY_COMPLEX, 2, color, 3)

        # Legende
        for i, (k, v) in enumerate(SIGNS.items()):
            cv2.putText(img, f"{k}: {v}", (10, 150 + i * 35),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (150, 150, 255), 2)

        cv2.imshow("Test Langage des Signes - A B L", img)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
