# Parktikum Sistem Embedded Lanjut
# Nama : Maftuh Siroj Hamdani
# NIM : 2412050

import os
import platform
from datetime import datetime

print("====================================")
print(" PRAKTIKUM SISTEM EMBEDDED LANJUT ")
print("====================================")

print("Tanggal & Waktu :", datetime.now())
print("Sistem Operasi  :", platform.system(), platform.release())
print("Arsitektur      :", platform.machine())
print("Hostname        :", platform.node())
print("------------------------------------")
