# src/config.py

import numpy as np

# === COLOR RANGE FOR SKIN (IN HSV) ===
# This is a common approximate range. You may tweak later if needed.
LOWER_HSV = np.array([0, 48, 80])
UPPER_HSV = np.array([20, 255, 255])

# === HAND DETECTION FILTERS ===
# Ignore very small blobs/noise
MIN_CONTOUR_AREA = 800   # adjust up/down if needed
MIN_RADIUS = 5           # ignore very tiny circles

# === VIRTUAL RECTANGLE SETTINGS ===
RECT_WIDTH = 200
RECT_HEIGHT = 150

# === DISTANCE THRESHOLDS (PIXELS) FOR STATES ===
SAFE_THRESHOLD = 120     # >120 px from rectangle → SAFE
WARNING_THRESHOLD = 60   # 60–120 px → WARNING
# <60 px → DANGER