# Algoritma Dijkstra

## 📌 Pengertian
Algoritma **Dijkstra** adalah algoritma pencarian jalur terpendek (shortest path) dari satu titik ke titik lainnya dalam sebuah graf dengan bobot (weight) non-negatif.

Algoritma ini ditemukan oleh Edsger W. Dijkstra dan banyak digunakan dalam berbagai aplikasi seperti navigasi dan jaringan.

---

## ⚙️ Prinsip Dasar
Dijkstra bekerja dengan cara mengeksplorasi node secara bertahap, dimulai dari titik awal, dan selalu memilih node dengan jarak terpendek yang belum dikunjungi.

---

## 🔄 Cara Kerja
1. Tentukan node awal
2. Beri jarak awal:
   - Node awal = 0
   - Node lain = tak hingga (∞)
3. Pilih node dengan jarak terkecil
4. Perbarui jarak ke semua tetangganya
5. Tandai node sebagai telah dikunjungi
6. Ulangi hingga semua node diproses atau tujuan ditemukan

---

## 🧠 Konsep Utama
- **Graph** → kumpulan node dan edge
- **Weight** → nilai biaya antar node
- **Shortest Path** → jalur dengan total biaya minimum

---

## 🚀 Kelebihan
- Menjamin jalur terpendek
- Mudah dipahami dan diimplementasikan
- Cocok untuk berbagai jenis graf

---

## ⚠️ Kekurangan
- Tidak bisa digunakan untuk bobot negatif
- Kurang efisien dibanding A* untuk pencarian dengan tujuan spesifik

---

## 📚 Contoh Penggunaan
- Navigasi GPS 🗺️
- Jaringan komputer 🌐
- Sistem transportasi 🚆

---

## 📚 Kesimpulan
Algoritma Dijkstra adalah metode yang efektif dan andal untuk menemukan jalur terpendek dalam graf dengan bobot non-negatif.

---

## 👨‍💻 Author
[Nama Kamu]
