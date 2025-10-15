import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def hitung_jarak():
    GPIO.output(TRIG, False)
    time.sleep(0.5)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        waktu_mulai = time.time()

    while GPIO.input(ECHO) == 1:
        waktu_akhir = time.time()

    durasi = waktu_akhir - waktu_mulai

    jarak = durasi * 17150
    jarak = round(jarak, 2)

    return jarak

try:
    while True:
        jarak = hitung_jarak()
        print(f"Jarak: {jarak} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Menghentikan program")
    GPIO.cleanup()
