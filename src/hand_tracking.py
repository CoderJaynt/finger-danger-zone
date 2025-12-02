

import cv2
import numpy as np

from .config import LOWER_HSV, UPPER_HSV, MIN_CONTOUR_AREA, MIN_RADIUS
from .virtual_boundary import point_to_rect_distance


def detect_hand(frame, target_rect=None):
    """
    Detect a skin-colored 'hand' in the frame.

    If target_rect is provided (x1, y1, x2, y2), we will prefer the skin blob
    whose center is closest to that rectangle (to avoid picking the face).

    Returns:
        center:   (x, y) tuple of the hand region's center, or None
        radius:   int radius of an enclosing circle, or 0
        fingertip:(x, y) tuple of the detected fingertip (topmost point), or None
        mask:     binary mask where skin pixels are white
    """
    # 1) Convert BGR frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 2) Threshold in HSV to get skin-colored pixels
    mask = cv2.inRange(hsv, LOWER_HSV, UPPER_HSV)

    # 3) Morphological operations to clean noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # 4) Find contours of the white regions
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    best_center = None
    best_radius = 0
    best_contour = None
    best_score = None  # smaller is better

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < MIN_CONTOUR_AREA:
            continue

        (x, y), radius = cv2.minEnclosingCircle(cnt)
        if radius < MIN_RADIUS:
            continue

        center = (int(x), int(y))

        # Scoring:
        #   If no target_rect given: prefer largest area (use -area)
        #   If target_rect given: prefer smallest distance to that rectangle
        if target_rect is None:
            score = -area
        else:
            px, py = center
            score = point_to_rect_distance(px, py, *target_rect)

        if best_score is None or score < best_score:
            best_score = score
            best_center = center
            best_radius = int(radius)
            best_contour = cnt

    fingertip = None
    if best_contour is not None:
        # Fingertip ≈ topmost point (smallest y) of the chosen contour
        topmost = tuple(best_contour[best_contour[:, :, 1].argmin()][0])
        fingertip = topmost

    return best_center, best_radius, fingertip, mask