

import cv2

from .hand_tracking import detect_hand
from .virtual_boundary import (
    get_centered_rectangle,
    point_to_rect_distance,
    classify_state,
)


def main():
    cap = cv2.VideoCapture(0)  # 0 = default webcam

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Optional: set smaller resolution for performance
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to read frame from webcam.")
            break

        # Flip horizontally for mirror-like view (optional)
        frame = cv2.flip(frame, 1)

        h, w = frame.shape[:2]

        # 1) Define virtual rectangle (placed slightly to the right)
        x1, y1, x2, y2 = get_centered_rectangle(w, h)

        # 2) Detect hand / fingertip (skin) in the whole frame
        center, radius, fingertip, mask = detect_hand(
            frame, target_rect=(x1, y1, x2, y2)
        )

        # 3) Decide which point to use for distance: fingertip preferred
        hand_point = fingertip if fingertip is not None else center

        distance = None
        if hand_point is not None:
            px, py = hand_point
            distance = point_to_rect_distance(px, py, x1, y1, x2, y2)

        # 4) Classify state based on distance
        state, rect_color = classify_state(distance)

        # 5) Draw hand circle (approx. hand region) and fingertip
        if center is not None and radius > 0:
            cv2.circle(frame, center, radius, (0, 0, 255), 2)  # red circle around hand

        if fingertip is not None:
            cv2.circle(frame, fingertip, 6, (0, 255, 0), -1)  # green dot at fingertip
            cv2.putText(
                frame, "Finger",
                (fingertip[0] + 5, fingertip[1] - 5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1
            )

        # 6) Draw virtual rectangle and state text
        cv2.rectangle(frame, (x1, y1), (x2, y2), rect_color, 2)

        cv2.putText(
            frame, f"STATE: {state}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, rect_color, 2
        )

        # If in DANGER state, show big warning
        if state == "DANGER":
            cv2.putText(
                frame, "DANGER DANGER", (50, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3
            )

        # 7) Show windows
        cv2.imshow("Hand Tracking - Live View", frame)
        cv2.imshow("Skin Mask", mask)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()