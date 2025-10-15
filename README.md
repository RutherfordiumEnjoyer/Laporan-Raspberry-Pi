# Laporan Internet of Things - Raspberry Pi

## Anggota Kelompok

| No | Nama                   | NRP         |
|----|------------------------|-------------|
| 1  | Hanif Mawla Faizi | 5027241064  |
| 2  | Mohammad Abyan Ranuaji     | 5027241106 |

## Alat yang dibutuhkan
- Raspberry Pi Kit
- HC-SR04
- Kabel Female to Female

## Langkah-langkah
1. Sambungkan pin seperti berikut:

    - Sambungkan pin VCC dari HC-SR04 ke pin 2 (5V)
    - Sambungkan pin GND dari HC-SR04 ke pin 6 (GND)
    - Sambung pin Trig dari HC-SR04 ke pin GPIO 23 (Pin 16)
    - Sambungkan pin Echo dari HC-SR04 ke pin GPIO 24 (Pin 18)

Sehingga tampilan dari Raspberry Pi kit seperti berikut:

<img width="867" height="1156" alt="Image" src="https://github.com/user-attachments/assets/61fc2d3e-b912-4ff7-8138-e76175dbc4b2" />

2. Setup 
    - Buka terminal yang berada di dalam OS Raspberry Pi
    - Simpan file yang berada di repository ini menggunakan "nano" seperti foto berikut:

      <img width="817" height="578" alt="Image" src="https://github.com/user-attachments/assets/f9d54a89-f47b-4d5f-aa9b-25880b0a6849" />


3. Menjalankan kode dan melihat hasil akhir
    - Run kode menggunakan python3:
    ```
    python3 raspberrypi.py
    ```

    Hasil yang diharapkan adalah sebagai berikut:
    
     <img width="640" height="800" alt="Image" src="https://github.com/user-attachments/assets/e3665cfa-ba61-4c4e-ba9a-3e68b3c525ba" />


Dengan ini, kita sudah berhasil menjalankan sensor HC-SR04 menggunakan Raspberry Pi.
