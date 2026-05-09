Optimization with the Particle Swarm Optimization (PSO) Method
📌 Deskripsi

Proyek ini merupakan implementasi algoritma Particle Swarm Optimization (PSO) untuk menyelesaikan masalah optimasi dan perencanaan jalur (path planning).

PSO adalah metode optimasi berbasis populasi yang terinspirasi dari perilaku sosial sekumpulan burung atau ikan saat mencari makanan.

Algoritma ini bekerja dengan mencari solusi terbaik melalui pembaruan posisi dan kecepatan partikel di dalam ruang pencarian.

🚀 Fitur
Implementasi algoritma Particle Swarm Optimization menggunakan Python
Simulasi lingkungan dengan obstacle
Visualisasi pergerakan partikel
Optimasi jalur dari titik awal menuju tujuan
Parameter PSO yang dapat diatur:
Jumlah partikel
Inertia weight
Cognitive coefficient
Social coefficient
Jumlah iterasi
🧠 Cara Kerja PSO

Setiap partikel merepresentasikan sebuah kandidat solusi.

Partikel bergerak berdasarkan:

Pengalaman terbaiknya sendiri (Personal Best / pBest)
Solusi terbaik dari seluruh partikel (Global Best / gBest)

Rumus pembaruan kecepatan:
vi​(t+1)=wvi​(t)+c1​r1​(pBesti​−xi​(t))+c2​r2​(gBest−xi​(t))

Rumus pembaruan posisi:
xi​(t+1)=xi​(t)+vi​(t+1)

Keterangan:
w = inertia weight
c1 = koefisien kognitif
c2= koefisien sosial
r2= angka acak
xi= posisi partikel
vi= kecepatan partikel
