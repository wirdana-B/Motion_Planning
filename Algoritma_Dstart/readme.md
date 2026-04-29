# Algoritma D* (D-Star)

## 📌 Pengertian
Algoritma **D\*** (Dynamic A-Star) adalah algoritma pencarian jalur yang digunakan untuk menemukan rute terpendek dalam lingkungan yang dapat berubah. D* sering digunakan pada robot yang bergerak di lingkungan nyata dan dinamis.

---

## ⚙️ Prinsip Dasar
D* merupakan pengembangan dari algoritma A*, dengan kemampuan untuk memperbarui jalur secara efisien ketika terjadi perubahan pada peta atau lingkungan.

Algoritma ini memungkinkan robot untuk:
- Menemukan jalur awal
- Menyesuaikan jalur jika ada hambatan baru

---

## 🔄 Cara Kerja
1. Tentukan titik awal dan tujuan
2. Hitung jalur terbaik seperti A*
3. Saat lingkungan berubah (misalnya ada rintangan baru):
   - Perbarui informasi peta
   - Hitung ulang jalur tanpa mengulang dari awal
4. Lanjutkan hingga mencapai tujuan

---

## 🧠 Konsep Utama
- **Replanning** → menghitung ulang jalur secara efisien
- **Dynamic Environment** → lingkungan bisa berubah
- **Cost Update** → memperbarui biaya jalur saat ada perubahan

---

## 🚀 Kelebihan
- Cocok untuk lingkungan dinamis
- Tidak perlu menghitung ulang dari awal
- Efisien untuk robot navigasi

---

## ⚠️ Kekurangan
- Lebih kompleks dibanding A*
- Implementasi lebih sulit

---

## 📚 Contoh Penggunaan
- Robot navigasi 🤖
- Kendaraan otonom 🚗
- Sistem eksplorasi

---

## 📚 Kesimpulan
Algoritma D* sangat efektif untuk pencarian jalur di lingkungan yang berubah-ubah karena mampu melakukan penyesuaian secara cepat dan efisien.

---

## 👨‍💻 Author
[Wirdana]
