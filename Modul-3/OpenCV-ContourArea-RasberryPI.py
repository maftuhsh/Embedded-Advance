import cv2
import numpy as np

kamera = cv2.VideoCapture(0, cv2.CAP_V4L2)

if not kamera.isOpened():
    print("Kamera tidak bisa dibuka")
    exit()

subtractor = cv2.createBackgroundSubtractorMOG2()

try:
    while True:
        ret, frame = kamera.read()

        if not ret:
            print("Gagal membaca frame")
            break

        frame = cv2.resize(frame, (480, 360), interpolation=cv2.INTER_AREA)
        frame = cv2.flip(frame, 1)

        blur_frame = cv2.GaussianBlur(frame, (21, 21), 0)

        fg_mask = subtractor.apply(blur_frame, learningRate=0.001)

        # Bersihkan noise (PENTING)
        kernel = np.ones((5, 5), np.uint8)
        fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)
        fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_DILATE, kernel)

        # Cari kontur
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) < 5000:
                continue

            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Frame", frame)
        cv2.imshow("Foreground Mask", fg_mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    kamera.release()
    cv2.destroyAllWindows()
    print("Program dihentikan")