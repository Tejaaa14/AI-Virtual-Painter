# 🎨 AI Virtual Painter

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-blue)
![Gesture Control](https://img.shields.io/badge/Control-Gesture%20Based-purple)

An intelligent and interactive **AI-powered Virtual Painter** that lets you draw, erase, switch colors, and control tools using **hand gestures** — no mouse or touchscreen required.  
Built with **OpenCV** + **MediaPipe**, this project offers a smooth, real-time computer vision experience.

---

## ✨ Highlights

### 🖐️ Real-Time AI Hand Tracking
- Uses **MediaPipe Hands** to detect **21 hand landmarks**.
- Tracks index finger, middle finger, and thumb positions with high accuracy.
- Works smoothly even with fast hand movements.

### ✍️ Gesture-Based Drawing (Touchless Interaction)
- **Index Finger Up → Drawing Mode**
- **Index + Middle Finger → Tool / Color Selection**
- **All Fingers Up → Clear Canvas**
- **Black Color → Eraser Mode (Hand Eraser)**

### 🎨 Modern Virtual Studio UI
- Auto-resized, responsive **header toolbar**.
- Vibrant colors and brush visualizations.
- Real-time feedback for current mode.

### ⚙️ Clean & Modular Codebase
- Custom **HandTrackingModule.py** for gesture detection.
- Easy to integrate into other AI/CV projects.
- Logical flow with optimized operations for smooth drawing.

---

## 🧠 How It Works

1. The webcam detects your hand using **MediaPipe**.
2. The system tracks finger positions and identifies which fingers are up.
3. Based on gestures:
   - Switch modes  
   - Select brush color  
   - Draw or erase  
   - Clear the canvas  
4. OpenCV overlays the drawing onto a canvas using:
   - Bitwise AND  
   - Bitwise OR  
   - Masking & thresholding  
5. The output is a smooth virtual drawing interface.

### ✋ Gesture → Action Mapping

| Gesture | Mode |
|--------|------|
| Index Finger Up | Drawing Mode |
| Index + Middle Finger Up | Selection Mode |
| All Fingers Up | Clear Canvas |
| Black Color | Eraser Mode |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Computer Vision** | OpenCV |
| **AI Hand Tracking** | MediaPipe |
| **Programming** | Python |
| **UI Rendering** | Webcam feed + Canvas overlay |
| **Architecture** | Modular (Custom Gesture Module) |

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/AI-Virtual-Painter.git
cd AI-Virtual-Painter

# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python VirtualPainter.py
