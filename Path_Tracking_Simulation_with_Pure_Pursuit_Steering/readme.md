# 🚗 Path Tracking Simulation with Pure Pursuit Steering

## 📌 Deskripsi
Project ini merupakan simulasi *path tracking* pada robot/vehicle menggunakan metode kontrol **Pure Pursuit Steering**. Metode ini digunakan untuk membuat robot dapat mengikuti jalur (trajectory) secara halus dan stabil dengan cara menghitung titik target (lookahead point) di depan posisi saat ini.

:contentReference[oaicite:0]{index=0} adalah algoritma berbasis geometri yang banyak digunakan pada robot otonom, AGV (Automated Guided Vehicle), dan kendaraan self-driving.

---

## 🎯 Tujuan Project
- Mensimulasikan pergerakan robot mengikuti jalur yang telah ditentukan
- Mengimplementasikan algoritma Pure Pursuit untuk kontrol steering
- Menganalisis performa tracking terhadap berbagai bentuk path (lurus, kurva, zig-zag)

---

## ⚙️ Konsep Dasar

### 1. Path Tracking
Proses dimana robot mengikuti jalur yang sudah didefinisikan sebelumnya.

### 2. Lookahead Point
Titik target di depan robot yang digunakan sebagai referensi arah gerak.

### 3. Steering Control
Mengatur arah pergerakan robot menuju lookahead point.

---

## 🔄 Cara Kerja Algoritma Pure Pursuit

1. Tentukan jalur (path) berupa kumpulan titik koordinat
2. Tentukan jarak lookahead
3. Cari titik target di depan robot pada jarak tersebut
4. Hitung sudut heading menuju target
5. Konversi sudut menjadi steering command
6. Update posisi robot
7. Ulangi sampai target tercapai

---

## 📊 Rumus Utama

Sudut steering dihitung dengan:
