import cv2
import mediapipe as mp
from win32api import GetKeyState as key
import keyboard as k


def detect_side(x1, y1, x2, y2):
    x = abs(x2 - x1)
    y = abs(y2 - y1)

    z = 'x'
    if x < y:
        z = 'y'
    if z == 'x' and x > 0.110:
        x = x2 - x1
        if x > 0:
            return 'left'
        else:
            return 'right'
    elif z == 'y' and y > 0.110:
        y = y2 - y1
        if y > 0:
            return 'down'
        else:
            return 'up'


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
a = []
fo = 0
fa = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
                if id == 12 or id == 8 or id == 16:
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    x, y = lm.x, lm.y
                    f = 0
                    if key(0x01) < 0:
                        f = 1
                        if len(a) == 0:
                            a.append(lm.x)
                            a.append(lm.y)
                        x1, y1 = lm.x, lm.y
                    if key(0x01) >= 0 and len(a) > 0:
                        print(round(a[0], 3), round(a[1], 3), '\n', round(x1, 3), round(y1, 3))
                        print(detect_side(a[0], a[1], x1, y1))
                        if detect_side(a[0], a[1], x1, y1) == 'left':
                            k.send('ctrl+windows+right')
                        elif detect_side(a[0], a[1], x1, y1) == 'right':
                            k.send('ctrl+windows+left')
                        elif detect_side(a[0], a[1], x1, y1) == 'down':
                            if fa:
                                k.send('windows+tab')
                                fa = 0
                            else:
                                k.send('windows+d')
                                fo = 1
                        elif detect_side(a[0], a[1], x1, y1) == 'up':
                            if fo:
                                k.send('windows+d')
                                fo = 0
                            else:
                                k.send('windows+tab')
                                fa = 1

                        a.clear()

                    cv2.circle(img, (cx, cy), 10, (240, 207, 137), cv2.FILLED)
            mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)

    cv2.imshow('Video', img)

    if cv2.waitKey(1) == ord('q'):
        break
