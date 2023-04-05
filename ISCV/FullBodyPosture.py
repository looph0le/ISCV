import cv2
import mediapipe as mp
import time

def main(vcam=0, presults=False):
    mpDraw = mp.solutions.drawing_utils
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()

    cap = cv2.VideoCapture(vcam)
    pTime = 0

    while True:
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = pose.process(imgRGB)

        if(presults == True):
            print(result.pose_landmarks)

        if result.pose_landmarks:
            mpDraw.draw_landmarks(img, result.pose_landmarks, mpPose.POSE_CONNECTIONS)

        cv2.imshow("Image", img)
        cv2.waitKey(1)
