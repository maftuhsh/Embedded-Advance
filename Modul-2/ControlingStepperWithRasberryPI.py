from gpiozero import DigitalOutputDevice
from time import sleep

# Konfigurasi GPIO (BCM)
pins = [4, 17, 27, 22]
motors = [DigitalOutputDevice(pin) for pin in pins]

# Half-step sequence
seq = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

def putar(derajat):
    """Putar motor berdasarkan derajat"""
    
    steps = int(derajat * 512 / 360)

    for _ in range(abs(steps)):
        urutan = seq if derajat > 0 else list(reversed(seq))

        for halfstep in urutan:
            for pin, state in zip(motors, halfstep):
                pin.value = state
            sleep(0.001)

    # Matikan motor setelah selesai
    for pin in motors:
        pin.off()

# Program utama
try:
    sudut = float(input("Masukkan sudut: "))
    putar(sudut)
except ValueError:
    print("Input tidak valid, masukkan angka.")
