# Probabilistic Roadmap (PRM) Planning

## 📌 Pengertian
**Probabilistic Roadmap (PRM)** adalah algoritma perencanaan jalur (*motion planning*) berbasis sampling yang digunakan untuk menemukan jalur dari titik awal ke tujuan dalam ruang konfigurasi (configuration space).

PRM banyak digunakan dalam robotika, terutama untuk sistem dengan ruang gerak yang kompleks.

---

## ⚙️ Prinsip Dasar
PRM bekerja dengan cara membuat peta (roadmap) dari node-node acak yang diambil dari ruang bebas (free space), kemudian menghubungkannya untuk membentuk graf.

Proses ini terdiri dari dua tahap utama:
1. **Learning Phase** → membangun roadmap
2. **Query Phase** → mencari jalur dari start ke goal

---

## 🔄 Cara Kerja

### 1. Learning Phase
- Sampling titik secara acak di ruang bebas
- Menyimpan titik sebagai node
- Menghubungkan node yang berdekatan jika tidak terhalang (collision-free)

### 2. Query Phase
- Menambahkan node start dan goal ke roadmap
- Menghubungkannya ke node terdekat
- Menggunakan algoritma pencarian (misalnya Dijkstra atau A*) untuk menemukan jalur

---

## 🧠 Konsep Utama
- **Sampling** → pengambilan titik secara acak
- **Collision Checking** → memastikan jalur tidak melewati rintangan
- **Graph (Roadmap)** → representasi jalur dalam bentuk node dan edge
- **Configuration Space (C-space)** → ruang semua kemungkinan posisi robot

---

## 🚀 Kelebihan
- Efisien untuk ruang berdimensi tinggi
- Cocok untuk lingkungan kompleks
- Roadmap bisa digunakan berulang kali

---

## ⚠️ Kekurangan
- Tidak optimal (jalur belum tentu paling pendek)
- Bergantung pada jumlah sampling
- Kurang cocok untuk lingkungan dinamis

---

## 📚 Contoh Penggunaan
- Robot manipulator 🤖
- Perencanaan jalur drone 🚁
- Simulasi gerakan robot

---

## 📚 Kesimpulan
PRM adalah algoritma yang efektif untuk motion planning di ruang kompleks dengan pendekatan berbasis probabilistik, meskipun tidak selalu menghasilkan jalur optimal.

---

## 👨‍💻 Author
[wirdana]
