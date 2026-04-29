# Rapidly-Exploring Random Trees (RRT*)

## 📌 Pengertian
**RRT\*** (Rapidly-Exploring Random Trees Star) adalah algoritma *motion planning* berbasis sampling yang digunakan untuk menemukan jalur dari titik awal ke tujuan dalam ruang yang kompleks.

RRT* merupakan pengembangan dari algoritma RRT yang memiliki keunggulan dalam menghasilkan jalur yang optimal (optimal path).

---

## ⚙️ Prinsip Dasar
RRT* membangun pohon (tree) secara bertahap dengan menambahkan node baru dari hasil sampling acak di ruang bebas (*free space*), lalu menghubungkannya ke node terdekat.

Berbeda dengan RRT, RRT* melakukan proses tambahan yang disebut **rewiring** untuk memperbaiki jalur agar lebih optimal.

---

## 🔄 Cara Kerja
1. Tentukan titik awal (start) dan tujuan (goal)
2. Sampling titik acak di ruang bebas
3. Temukan node terdekat dalam tree
4. Buat node baru menuju arah sampel
5. Lakukan **collision checking**
6. Pilih parent terbaik berdasarkan biaya minimum
7. Lakukan **rewiring** untuk optimasi jalur
8. Ulangi hingga mencapai goal

---

## 🧠 Konsep Utama
- **Sampling** → pengambilan titik acak
- **Tree Structure** → struktur pohon, bukan graf penuh
- **Rewiring** → memperbaiki jalur agar lebih optimal
- **Cost Function** → menghitung biaya dari start ke node

---

## 🚀 Kelebihan
- Menghasilkan jalur optimal (asymptotically optimal)
- Cocok untuk ruang kompleks dan berdimensi tinggi
- Lebih baik dari RRT dalam kualitas jalur

---

## ⚠️ Kekurangan
- Lebih lambat dibanding RRT biasa
- Membutuhkan komputasi lebih besar
- Sensitif terhadap parameter (sampling, radius, dll)

---

## 📚 Contoh Penggunaan
- Robot navigasi 🤖
- Kendaraan otonom 🚗
- Perencanaan jalur drone 🚁

---

## 📚 Kesimpulan
RRT* adalah algoritma motion planning yang powerful karena mampu menemukan jalur optimal di lingkungan kompleks, meskipun membutuhkan waktu komputasi lebih tinggi dibanding versi RRT biasa.

---

## 👨‍💻 Author
[wirdana]
