import cv2

kamera = cv2.VideoCapture(0)

# Cek apakah kamera berhasil dibuka
if not kamera.isOpened():
    print("Kamera tidak bisa dibuka")
    exit()

try:
    while True:
        status, frame = kamera.read()

        # Cek apakah frame berhasil dibaca
        if not status:
            print("Gagal membaca frame")
            break

        # Resize frame
        frame = cv2.resize(frame, (480, 360), interpolation=cv2.INTER_AREA)

        # Flip horizontal
        frame = cv2.flip(frame, 1)

        # Tampilkan
        cv2.imshow('frame', frame)

        # Tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    kamera.release()
    cv2.destroyAllWindows()
    print("Program dihentikan")
