import cv2

kamera = cv2.VideoCapture(0, cv2.CAP_V4L2)

if not kamera.isOpened():
    print("Kamera tidak bisa dibuka")
    exit()

# Definisi ROI (kanan setengah layar)
start = (240, 0)
end = (480, 360)

try:
    while True:
        status, frame = kamera.read()

        if not status:
            print("Gagal membaca frame")
            break

        frame = cv2.resize(frame, (480, 360), interpolation=cv2.INTER_AREA)
        frame = cv2.flip(frame, 1)

        # Ambil ROI
        ROI = frame[start[1]:end[1], start[0]:end[0]]

        # Visualisasi area ROI di frame utama
        cv2.rectangle(frame, start, end, (0, 255, 0), 2)

        cv2.imshow('Frame', frame)
        cv2.imshow('ROI', ROI)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:  # ESC
            break

finally:
    kamera.release()
    cv2.destroyAllWindows()
    print("Program dihentikan")