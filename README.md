# Motion Planning

## Pengertian Motion Planning
Motion Planning adalah proses menentukan jalur atau lintasan yang harus dilalui oleh robot, kendaraan otomatis, atau agen bergerak lainnya dari titik awal menuju tujuan dengan aman dan efisien.

Dalam bidang robotika dan kendaraan otonom seperti AGV (Automated Guided Vehicle), motion planning sangat penting agar robot dapat:
- Menghindari rintangan (obstacle avoidance)
- Menentukan jalur tercepat
- Bergerak dengan aman
- Mengoptimalkan waktu dan energi

---

# Tujuan Motion Planning
Tujuan utama motion planning adalah:

1. Menentukan lintasan terbaik dari posisi awal ke tujuan
2. Menghindari tabrakan dengan objek lain
3. Menghasilkan gerakan yang halus dan efisien
4. Menyesuaikan pergerakan dengan kondisi lingkungan

---

# Komponen Motion Planning

## 1. Start Position
Posisi awal robot atau kendaraan.

## 2. Goal Position
Tujuan akhir yang ingin dicapai.

## 3. Environment Mapping
Peta lingkungan yang berisi:
- Dinding
- Obstacle
- Jalur
- Area aman

## 4. Path Planning Algorithm
Algoritma yang digunakan untuk mencari jalur terbaik.

## 5. Motion Controller
Bagian yang mengontrol gerakan robot agar mengikuti jalur yang telah dibuat.

---

# Jenis-Jenis Motion Planning

## 1. Global Planning
Perencanaan jalur berdasarkan peta lengkap lingkungan.

### Contoh algoritma:
- A*
- Dijkstra
- BFS
- DFS

### Kelebihan:
- Jalur optimal
- Cocok untuk lingkungan statis

### Kekurangan:
- Kurang fleksibel terhadap obstacle dinamis

---

## 2. Local Planning
Perencanaan gerakan secara real-time berdasarkan sensor.

### Contoh:
- Dynamic Window Approach (DWA)
- Potential Field
- Vector Field Histogram (VFH)

### Kelebihan:
- Responsif terhadap perubahan lingkungan

### Kekurangan:
- Bisa terjebak local minima

---

# Algoritma Motion Planning Populer

## A* Algorithm
Algoritma pencarian jalur yang menggunakan:
- Cost dari start
- Heuristic menuju goal

### Kelebihan:
- Cepat
- Optimal
- Banyak digunakan pada AGV dan robot

---

## Dijkstra Algorithm
Mencari jalur terpendek ke semua node.

### Kelebihan:
- Akurat
- Stabil

### Kekurangan:
- Lebih lambat dibanding A*

---

## Rapidly-exploring Random Tree (RRT)
Algoritma berbasis sampling untuk ruang kompleks.

### Digunakan pada:
- Robot manipulator
- Robot bergerak
- Drone

---

# Motion Planning pada AGV

Pada AGV, motion planning digunakan untuk:
- Menentukan jalur otomatis
- Menghindari tabrakan
- Navigasi gudang
- Optimasi distribusi barang

## Contoh Sistem AGV
Sensor yang digunakan:
- LiDAR
- Ultrasonic
- Kamera
- RFID

Controller:
- ESP32
- STM32
- Jetson Nano
- Raspberry Pi

Software:
- ROS / ROS2
- Gazebo
- RViz

---

# Flow Motion Planning

```text
Start
  ↓
Baca Sensor
  ↓
Deteksi Obstacle
  ↓
Hitung Jalur
  ↓
Generate Path
  ↓
Kontrol Motor
  ↓
Menuju Goal
