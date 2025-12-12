🎨 AI Virtual Painter

Python OpenCV Mediapipe | Gesture Control | Real-time Drawing | Secure & Modular Codebase
A smart, gesture-controlled virtual painting application powered by AI hand-tracking technology.
Draw, erase, switch colors, and clear the canvas — fully hands-free using your webcam!

✨ Highlights
🤖 AI Hand Tracking (MediaPipe)

Tracks 21 real-time hand landmarks

Detects finger states for gesture recognition

Accurate and fast, even on lower-end devices

✍️ Gesture-Based Drawing (Mouse-Free!)

Index finger up → Draw

Index + Middle → Select tools/colors

All five fingers up → Clear Canvas

Natural, intuitive interaction — like air-drawing

🎨 Modern Virtual Painting Tools

Color palette inside a dynamic header

Eraser mode (Black)

Smooth lines using coordinate filtering

Persistent drawing canvas with OpenCV bitwise merging

⚙️ Robust & Clean Code Architecture

Fully modular with a reusable HandTrackingModule.py

Smart gesture detection (fingersUp, findPosition, etc.)

Header images auto-resized to avoid runtime errors

🖥️ UI/UX Enhancements

Real-time FPS display

Mirror-correct webcam feed

Smooth transitions between modes

Clear gesture feedback on screen

🧠 How It Works
✋ Gesture Detection → 🎨 Action Mapping
Gesture	Action
Index Finger Up	Drawing Mode
Index + Middle	Tool Selection
All Five Fingers Up	Clear Canvas
Black Color Selected	Eraser Mode
Press S	Save the artwork
Press ESC	Exit the app
Drawing Flow

Hand landmarks detected via MediaPipe

Index finger coordinates tracked frame-by-frame

Lines drawn on both live frame + canvas

Bitwise operations merge canvas & camera feed seamlessly

🛠️ Tech Stack
Layer	Technology
AI / CV	MediaPipe Hands, OpenCV
Programming	Python
Visualization	Webcam + Canvas overlay
Interface	Gesture-based interaction
Deployment	Local system (any OS supported by OpenCV)
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/<your-username>/AI-Virtual-Painter.git
cd AI-Virtual-Painter

2️⃣ Create a virtual environment
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
python VirtualPainter.py


Then visit your webcam preview — start drawing in the air! 🎉

📝 Key Features (Before & After Enhancements)
Category	Before	After
Hand Tracking	Basic detection	Stable, gesture-aware detection
Drawing Lines	Jittery lines	Smoothed movement + canvas blending
Header Interaction	Hardcoded sizes	Auto-resized, safe broadcasting
Error Handling	Crashes on camera errors	Full frame validation logic
Code Quality	Mixed logic	Modular, reusable, scalable
UX	Basic	Clean, responsive, intuitive
📂 Project Structure
AI-Virtual-Painter/
│
├── Header/                  # Color & tool images
├── HandTrackingModule.py    # AI-based hand tracking module
├── VirtualPainter.py        # Main interactive painter app
├── requirements.txt
└── README.md

🧑‍💻 Contributors
Name	Role	GitHub
Beran Teja	Project Owner, Developer	@Tejaaa14
ChatGPT (Assistant)	Architecture, Code Improvement, Documentation	—

Want to contribute? PRs are welcome!

🛡️ Stability & Safety Enhancements
Issue	Fix
Frame empty → App crash	Added camera read validation
Incorrect header size → Broadcasting error	Auto-resize headers
Gesture misreads	Finger-ID validation added
Code duplication	Centralized logic inside HandTrackingModule
Jittery drawing	Introduced smoothing hooks
📜 License

This project is licensed under the MIT License.
You may use, modify, and distribute this project with attribution.

💬 Feedback & Contributions

Contributions are always welcome!
Suggestions? Found a bug? Want to add new gestures?

How to contribute:
fork → new branch → commit → push → open PR


Message or reach out via GitHub:

@Tejaaa14

⭐ Support the Project

If you like this project, please ⭐ the repo!
Your support motivates more AI-powered projects like this.
