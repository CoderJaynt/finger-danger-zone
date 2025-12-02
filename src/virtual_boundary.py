

import math
from typing import Tuple, Optional

from .config import RECT_WIDTH, RECT_HEIGHT, SAFE_THRESHOLD, WARNING_THRESHOLD


def get_centered_rectangle(frame_width: int, frame_height: int) -> Tuple[int, int, int, int]:
    """
    Returns coordinates (x1, y1, x2, y2) of a rectangle.
    We place it a bit to the right side of the frame so your face
    (usually in the center) doesn't interfere.
    """
    x_center = int(frame_width * 0.7)     # 70% from the left
    y_center = frame_height // 2

    x1 = x_center - RECT_WIDTH // 2
    y1 = y_center - RECT_HEIGHT // 2
    x2 = x1 + RECT_WIDTH
    y2 = y1 + RECT_HEIGHT
    return x1, y1, x2, y2


def point_to_rect_distance(px: int, py: int,
                           x1: int, y1: int, x2: int, y2: int) -> float:
    """
    Shortest distance from point (px, py) to an axis-aligned rectangle (x1, y1, x2, y2).
    If the point is inside the rectangle, distance is 0.
    """
    cx = min(max(px, x1), x2)
    cy = min(max(py, y1), y2)

    dx = px - cx
    dy = py - cy
    return math.hypot(dx, dy)


def classify_state(distance: Optional[float]) -> Tuple[str, Tuple[int, int, int]]:
    """
    Given a distance (in pixels), return:
      - state string: "SAFE", "WARNING", "DANGER", or "NO HAND"
      - BGR color for drawing the rectangle/state

    If distance is None (no hand detected), we return "NO HAND" and white color.
    """
    if distance is None:
        return "NO HAND", (255, 255, 255)  # white

    if distance > SAFE_THRESHOLD:
        return "SAFE", (0, 255, 0)         # green
    elif distance > WARNING_THRESHOLD:
        return "WARNING", (0, 255, 255)    # yellow
    else:
        return "DANGER", (0, 0, 255)       # red