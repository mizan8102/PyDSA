# import the opencv library
import cv2
import mediapipe as mp
import time

vid = cv2.VideoCapture(0)

# hands
myHands = mp.solutions.hands
hands = myHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = vid.read()
    # color my hands
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, myHands.HAND_CONNECTIONS)

    # show my hands
    cv2.imshow('frame', img)
    cv2.waitKey(1)
