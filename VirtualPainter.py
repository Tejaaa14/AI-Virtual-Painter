# VirtualPainter.py (fixed header resize)
import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

#######################
brushThickness = 25
eraserThickness = 100
########################

# change this if your webcam is not at index 0
camera_index = 0

folderPath = "Header"
if not os.path.exists(folderPath):
    raise FileNotFoundError(f"Header folder not found: {folderPath}")

myList = os.listdir(folderPath)
overlayList = []
# target header size used in the code
HEADER_W = 1280
HEADER_H = 125

for imPath in sorted(myList):
    full_path = os.path.join(folderPath, imPath)
    image = cv2.imread(full_path)
    if image is None:
        print(f"Warning: failed to read {imPath} (skipping).")
        continue
    # Resize header to exact width x height to avoid broadcasting errors
    image_resized = cv2.resize(image, (HEADER_W, HEADER_H), interpolation=cv2.INTER_AREA)
    overlayList.append(image_resized)

if len(overlayList) == 0:
    raise RuntimeError("No valid header images found in Header folder.")

print(f"Loaded {len(overlayList)} header images.")
header = overlayList[0].copy()
drawColor = (255, 0, 255)

cap = cv2.VideoCapture(camera_index)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon=0.65, maxHands=1)
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

while True:
    # 1. Import image
    success, img = cap.read()
    if not success:
        print("Failed to read frame from camera. Check camera index.")
        break
    img = cv2.flip(img, 1)

    # 2. Find Hand Landmarks
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # tip of index and middle fingers
        x1, y1 = lmList[8][1], lmList[8][2]
        x2, y2 = lmList[12][1], lmList[12][2]

        # 3. Check which fingers are up
        fingers = detector.fingersUp()

        # 4. If Selection Mode - Two fingers are up
        if fingers[1] == 1 and fingers[2] == 1:
            xp, yp = 0, 0
            # Checking for the click in the header area
            if y1 < HEADER_H:
                # Using number of overlays and safer index checks
                if 250 < x1 < 450 and len(overlayList) > 0:
                    header = overlayList[0].copy()
                    drawColor = (255, 0, 255)
                elif 550 < x1 < 750 and len(overlayList) > 1:
                    header = overlayList[1].copy()
                    drawColor = (255, 0, 0)
                elif 800 < x1 < 950 and len(overlayList) > 2:
                    header = overlayList[2].copy()
                    drawColor = (0, 255, 0)
                elif 1050 < x1 < 1200 and len(overlayList) > 3:
                    header = overlayList[3].copy()
                    drawColor = (0, 0, 0)
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

        # 5. If Drawing Mode - Index finger is up, middle finger is down
        if fingers[1] == 1 and fingers[2] == 0:
            cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
            if xp == 0 and yp == 0:
                xp, yp = x1, y1
            # draw on both img and imgCanvas for persistent strokes
            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
            xp, yp = x1, y1

        # Clear Canvas when all fingers are up
        if all(x == 1 for x in fingers):
            imgCanvas = np.zeros((720, 1280, 3), np.uint8)

    # merge imgCanvas into the live image
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    # Setting the header image (safe: header height matches HEADER_H)
    img[0:HEADER_H, 0:HEADER_W] = header

    cv2.imshow("Image", img)
    cv2.imshow("Canvas", imgCanvas)
    cv2.imshow("Inv", imgInv)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    if key == ord('c'):
        imgCanvas = np.zeros((720, 1280, 3), np.uint8)

cap.release()
cv2.destroyAllWindows()