import cv2
import time
import subprocess

from utils.hand_tracking import HandDetector
from utils.volume_control import VolumeController
from utils.screenshot import ScreenshotTaker
from utils.zoom_control import ZoomManager
from utils.config_loader import load_config


def main():
    cfg = load_config("config.json")
    cam_cfg = cfg["camera"]
    det_cfg = cfg["detection"]
    scr_cfg = cfg["screenshot"]
    vol_cfg = cfg["volume"]
    zoo_cfg = cfg["zoom"]

    cap = cv2.VideoCapture(cam_cfg["index"])
    cap.set(3, cam_cfg["width"])
    cap.set(4, cam_cfg["height"])

    detector = HandDetector(
        min_detection_confidence=det_cfg["min_detection_confidence"],
        min_tracking_confidence=det_cfg["min_tracking_confidence"]
    )
    vol_control = VolumeController(
        min_vol=vol_cfg["min"], max_vol=vol_cfg["max"],
        dist_min=vol_cfg["distance_min"], dist_max=vol_cfg["distance_max"]
    )
    screenshot = ScreenshotTaker(folder=scr_cfg["folder"])
    zoom = ZoomManager(min_scale=zoo_cfg["min_scale"], max_scale=zoo_cfg["max_scale"])

    SCREENSHOT_CONFIDENCE = det_cfg["screenshot_confidence"]
    GESTURE_HISTORY_LENGTH = det_cfg["gesture_history_length"]
    COOLDOWN_DEFAULT = det_cfg["cooldown_frames"]
    SCR_COOLDOWN = scr_cfg["cooldown"]
    SCR_STABLE = scr_cfg["stable_threshold"]
    wCam = cam_cfg["width"]
    hCam = cam_cfg["height"]

    pTime = 0
    mode = "menu"
    screenshot_cooldown = 0
    cooldown_frames = 0
    GESTURE_HISTORY = []

    while True:
        success, img = cap.read()
        if not success:
            continue

        img = detector.find_hands(img)
        hands_data = detector.get_landmarks(img)

        cTime = time.time()
        fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (40, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

        try:
            if mode == "menu":
                cv2.putText(img, "MENU :", (40, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 3)
                cv2.putText(img, "1. Index leve - Volume", (40, 180), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
                cv2.putText(img, "2. 3 Doigts - Capture", (40, 240), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
                cv2.putText(img, "3. 2 Mains - Zoom", (40, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)

                if hands_data and cooldown_frames == 0:
                    fingers = detector.fingers_up(hands_data[0], SCREENSHOT_CONFIDENCE)

                    if fingers == [0, 1, 0, 0, 0]:
                        mode = "volume"
                        cooldown_frames = COOLDOWN_DEFAULT

                    elif sum(fingers) == 3:
                        mode = "screenshot"
                        screenshot_cooldown = SCR_COOLDOWN
                        GESTURE_HISTORY = []
                        cooldown_frames = COOLDOWN_DEFAULT

                    elif len(hands_data) == 2:
                        mode = "zoom"
                        zoom.reset()
                        cooldown_frames = COOLDOWN_DEFAULT

            elif mode == "volume":
                if hands_data and len(hands_data[0]["lmList"]) >= 21:
                    hand = hands_data[0]
                    img = vol_control.adjust(img, hand["lmList"][4], hand["lmList"][8])

                    if detector.fingers_up(hand) == [1, 1, 1, 1, 1]:
                        mode = "menu"
                        cooldown_frames = COOLDOWN_DEFAULT

            elif mode == "screenshot":
                if screenshot_cooldown > 0:
                    if hands_data:
                        current_fingers = detector.fingers_up(hands_data[0], 0.35)
                        GESTURE_HISTORY.append(sum(current_fingers) >= 3)

                        if len(GESTURE_HISTORY) > GESTURE_HISTORY_LENGTH:
                            GESTURE_HISTORY.pop(0)

                        confidence_level = sum(GESTURE_HISTORY) / len(GESTURE_HISTORY) if GESTURE_HISTORY else 0
                        cv2.rectangle(img, (0, 0), (int(wCam * confidence_level), 30), (0, 255, 0), -1)

                        if confidence_level >= SCR_STABLE and screenshot_cooldown == SCR_COOLDOWN:
                            if screenshot.capture():
                                subprocess.Popen(["afplay", "/System/Library/Sounds/Tink.aiff"])
                                cv2.putText(img, "CAPTURE REUSSIE!", (wCam // 2 - 300, hCam // 2),
                                            cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 3)
                                cv2.imshow("Gesture Control", img)
                                cv2.waitKey(500)
                                screenshot_cooldown = SCR_COOLDOWN - 1

                    screenshot_cooldown -= 1
                else:
                    mode = "menu"
                    GESTURE_HISTORY = []
                    cooldown_frames = COOLDOWN_DEFAULT

            elif mode == "zoom":
                if len(hands_data) == 2:
                    img = zoom.adjust(img, hands_data)
                else:
                    mode = "menu"
                    zoom.reset()
                    cooldown_frames = COOLDOWN_DEFAULT

        except Exception as e:
            print(f"Erreur: {e}")
            mode = "menu"

        if cooldown_frames > 0:
            cooldown_frames -= 1

        cv2.imshow("Gesture Control", img)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
