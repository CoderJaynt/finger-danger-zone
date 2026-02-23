# ✋ Hand Boundary POC – Real-Time Finger vs Virtual Danger Zone
## Streamlit UI Preview

<p align="center"> <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv" /> <img src="https://img.shields.io/badge/Streamlit-Web%20App-ff4b4b?style=for-the-badge&logo=streamlit" /> <img src="https://img.shields.io/badge/WebRTC-Real%20Time-blue?style=for-the-badge" /> <img src="https://img.shields.io/badge/CPU-Only-orange?style=for-the-badge" /> </p>

## 📚 1. What this prototype does
<div style=" background: linear-gradient(135deg,#141E30,#243B55); padding:25px; border-radius:18px; box-shadow: 0px 0px 20px rgba(36,59,85,0.5); color:white; line-height:1.8; ">

Conceptually, imagine a virtual safety zone on the screen.
Your camera shows your real hand. As you move a finger towards the box:

1. When your finger is far → the system shows SAFE

2. When your finger gets close → it turns to WARNING

3. When your finger is very close / touching the box → it displays DANGER DANGER directly on the live video

### This demonstrates:

* Hand/finger tracking without any pose API

* Geometry-based interaction with virtual objects

* A simple but working distance-based state machine

* Real-time processing on CPU only

</div>

## 🛠 2. Tech Stack
<p align="center"> <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python" /> <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv" /> <img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-yellow?style=for-the-badge&logo=numpy" /> <img src="https://img.shields.io/badge/Streamlit-Web%20UI-ff4b4b?style=for-the-badge&logo=streamlit" /> <img src="https://img.shields.io/badge/WebRTC-streamlit--webrtc-blue?style=for-the-badge" /> <img src="https://img.shields.io/badge/AV-Video%20Frames-lightgrey?style=for-the-badge" /> </p>

1. Language: Python

2. Computer Vision: OpenCV, NumPy

3. Web UI: Streamlit, streamlit-webrtc, av

3. Hardware: Any webcam

4. Processing: CPU only

** No cloud services. No MediaPipe. No OpenPose.

## 🗂 3. Project Structure
<div style=" background: linear-gradient(135deg,#141E30,#243B55); padding:25px; border-radius:18px; box-shadow: 0px 0px 20px rgba(36,59,85,0.5); color:white; line-height:1.8; "> <pre> hand_boundary_poc/ ├─ README.md ├─ requirements.txt ├─ streamlit_app.py └─ src/ ├─ __init__.py ├─ config.py ├─ hand_tracking.py ├─ virtual_boundary.py └─ main.py </pre> </div>

## ⚙ 4. Installation & Setup
<div style=" background: linear-gradient(135deg,#42275a,#734b6d); padding:25px; border-radius:18px; box-shadow: 0px 0px 20px rgba(115,75,109,0.5); color:white; line-height:1.8; ">
1️⃣ Create Virtual Environment (Recommended)

<strong>Windows:</strong>

<pre> python -m venv .venv .\.venv\Scripts\activate </pre>

<strong>macOS / Linux:</strong>

<pre> python3 -m venv .venv source .venv/bin/activate </pre> </div>

<div style=" background: linear-gradient(135deg,#1f4037,#99f2c8); padding:25px; border-radius:18px; box-shadow: 0px 0px 20px rgba(153,242,200,0.4); color:black; line-height:1.8; ">

   2️⃣ Install Dependencies
<pre> pip install -r requirements.txt </pre> </div>

## 🌐 5. Live Demo
<div style=" background: linear-gradient(135deg,#000428,#004e92); padding:30px; border-radius:20px; box-shadow: 0px 0px 25px rgba(0,78,146,0.6); color:white; line-height:1.8; ">
🚀 Try the Live Streamlit App
<a href="https://finger-danger-zone-rvxmehtcvory4mcnau5w6x.streamlit.app/" target="_blank"> <img src="https://img.shields.io/badge/Launch-Live%20App-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white"> </a>

<br><br>

1. Runs fully in-browser

2. Real-time fingertip tracking

3. Virtual boundary interaction

4. CPU-only processing

</div>
