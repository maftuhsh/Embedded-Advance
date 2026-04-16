import cv2
import numpy as np

kamera = cv2.VideoCapture(0, cv2.CAP_V4L2)

if not kamera.isOpened():
    print("Kamera tidak bisa dibuka")
    exit()

# Background subtractor (lebih umum & ringan)
subtractor = cv2.createBackgroundSubtractorMOG2()

try:
    while True:
        status, frame = kamera.read()

        if not status:
            print("Gagal membaca frame")
            break

        frame = cv2.resize(frame, (480, 360), interpolation=cv2.INTER_AREA)
        frame = cv2.flip(frame, 1)

        blur_fr = cv2.GaussianBlur(frame, (21, 21), 0)

        fg_mask = subtractor.apply(blur_fr)

        cv2.imshow('frame', frame)
        cv2.imshow('subs', fg_mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    kamera.release()
    cv2.destroyAllWindows()
    print("Program dihentikan")
