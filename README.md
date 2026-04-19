# ✋ Hand Boundary POC — Real-Time Finger vs Virtual Danger Zone

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-27ae60?style=for-the-badge&logo=opencv&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![WebRTC](https://img.shields.io/badge/WebRTC-Real_Time-2196F3?style=for-the-badge&logo=webrtc&logoColor=white)
![CPU Only](https://img.shields.io/badge/CPU-Only-FF6F00?style=for-the-badge&logo=intel&logoColor=white)

**A real-time safety boundary system — pure OpenCV, no MediaPipe, no cloud, no GPU.**

[![Launch App](https://img.shields.io/badge/🚀%20Launch%20Live%20App-FF4B4B?style=for-the-badge)](https://finger-danger-zone-rvxmehtcvory4mcnau5w6x.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/View%20on%20GitHub-181717?style=for-the-badge&logo=github)](https://github.com/coderjaynt/finger-danger-zone)

</div>

---

## 📌 Overview

Imagine a virtual safety zone drawn on your screen. Your webcam shows your real hand. As you move a finger toward the box, the system transitions through three states — displayed live on the video feed.

```
Finger far away     →   🟢  SAFE
Finger getting close →   🟡  WARNING  
Finger inside zone  →   🔴  DANGER
```

> No pose estimation APIs. No cloud calls. Just geometry-based distance math running on your CPU in real time.

---

## 🎯 Key Features

| Feature | Detail |
|---|---|
| 🖐 Fingertip Detection | OpenCV-based contour tracking |
| 📦 Virtual Boundary | Configurable danger zone overlay |
| ⚡ Real-Time | Live WebRTC camera stream |
| 🖥 CPU Only | No GPU or cloud required |
| 🌐 Browser-Based | Runs fully in-browser via Streamlit |
| 🔒 Private | No data leaves your device |

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.8+ |
| Computer Vision | OpenCV, NumPy |
| Web UI | Streamlit |
| Camera Stream | streamlit-webrtc |
| Video Frames | av |
| Hardware | Any webcam |

> ✦ No MediaPipe · No OpenPose · No cloud services · No GPU required

---

## 🗂 Project Structure

```
finger-danger-zone/
├── README.md
├── requirements.txt
├── packages.txt
├── streamlit_app.py        ← entry point
└── src/
    ├── __init__.py
    ├── config.py           ← thresholds & zone config
    ├── hand_tracking.py    ← fingertip detection logic
    ├── virtual_boundary.py ← danger zone geometry
    └── main.py             ← state machine (SAFE / WARNING / DANGER)
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/coderjaynt/finger-danger-zone
cd finger-danger-zone
```

### 2. Create a virtual environment

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run streamlit_app.py
```

Then open `http://localhost:8501` in your browser and allow webcam access.

---

## 🌐 Live Demo

<div align="center">

### 🟢 Live on Streamlit Cloud

[![Launch App](https://img.shields.io/badge/Open%20Live%20App%20→-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://finger-danger-zone-rvxmehtcvory4mcnau5w6x.streamlit.app/)

**No install needed** — open in any browser with a webcam and start moving your finger.

</div>

---

## 📦 Dependencies

**`requirements.txt`**
```
opencv-python-headless
numpy
streamlit
streamlit-webrtc
av
```

**`packages.txt`**
```
libgl1
libxext6
```

---

## 🚀 How It Works

1. **Camera feed** is captured live via WebRTC in the browser
2. **OpenCV** processes each frame to detect skin-colored contours
3. **Fingertip coordinates** are extracted from the largest contour's convex hull
4. **Distance** from the fingertip to the virtual boundary box is calculated
5. **State machine** transitions between `SAFE → WARNING → DANGER` based on thresholds
6. **Overlay** is drawn directly on the video frame and streamed back to the browser

---

<div align="center">

Made by [@CoderJaynt](https://github.com/coderjaynt) &nbsp;·&nbsp; OpenCV · Streamlit · WebRTC

</div>
