# Algoritma A* (A-Star)

## 📌 Pengertian
Algoritma **A\*** (A-Star) adalah algoritma pencarian jalur (pathfinding) yang digunakan untuk menemukan rute terpendek dari titik awal ke tujuan. Algoritma ini menggabungkan keunggulan dari *Dijkstra* dan *Greedy Best-First Search*.

---

## ⚙️ Prinsip Dasar
A* menggunakan fungsi evaluasi:
f(n) = g(n) + h(n)

Keterangan:
- `g(n)` = biaya dari titik awal ke node saat ini
- `h(n)` = estimasi biaya dari node ke tujuan (heuristic)
- `f(n)` = total biaya

---

## 🔄 Cara Kerja
1. Mulai dari node awal
2. Simpan node yang akan diperiksa (open list)
3. Pilih node dengan nilai `f(n)` terkecil
4. Periksa tetangga node tersebut
5. Ulangi sampai tujuan ditemukan

---

## 🧠 Heuristic
Heuristic adalah perkiraan jarak ke tujuan, contohnya:
- Manhattan Distance
- Euclidean Distance

---

## 🚀 Kelebihan
- Menemukan jalur terpendek
- Lebih efisien dibanding beberapa algoritma lain

---

## ⚠️ Kekurangan
- Membutuhkan memori cukup besar
- Performa tergantung kualitas heuristic

---

## 📚 Kesimpulan
Algoritma A* adalah solusi efektif untuk masalah pencarian jalur karena mampu menyeimbangkan antara kecepatan dan akurasi.

---

## 👨‍💻 Author
[wirdana]
