## Implementasi Logika Fuzzy Mamdani - Praktikum KB Pertemuan 3

Repository ini berisi hasil pengerjaan tugas praktikum **Kecerdasan Buatan (KB)** pertemuan 3, yang fokus pada implementasi **Logika Fuzzy metode Mamdani** menggunakan Python.

Dalam proyek ini, terdapat dua studi kasus utama:
1. Optimasi stok pada toko hewan  
2. Penilaian tingkat kepuasan pelayanan masyarakat  

---

## 📁 Struktur Repositori :
```
├── kasus_1_petshop.py
├── kasus_2_pelayanan.py
└── README.md
```

---

## 🐾 Studi Kasus 1: Udin Pet Shop

Studi kasus ini bertujuan untuk menentukan jumlah stok makanan hewan yang optimal. Sistem dirancang agar dapat menghindari kondisi kelebihan stok (*overstock*) maupun kekurangan stok.

### Variabel dan Himpunan Fuzzy

#### Input (Antecedents)
- **Barang Terjual**: 0 – 100 (Rendah, Sedang, Tinggi)  
- **Permintaan**: 0 – 300 (Rendah, Sedang, Tinggi)  
- **Harga Per Item**: 0 – 100.000 (Murah, Sedang, Mahal)  
- **Profit**: 0 – 4.000.000 (Rendah, Sedang, Banyak)  

#### Output (Consequent)
- **Stok Makanan**: 0 – 1000 (Sedang, Banyak)  

### Aturan Fuzzy (Rules)

Beberapa aturan yang digunakan antara lain:
- Jika **Barang Terjual tinggi**, **Permintaan tinggi**, **Harga murah**, dan **Profit tinggi**, maka **Stok = Banyak**
- Jika **Barang Terjual rendah**, **Permintaan rendah**, **Harga sedang**, dan **Profit sedang**, maka **Stok = Sedang**

Aturan-aturan ini digunakan untuk membantu sistem dalam mengambil keputusan terkait jumlah stok.

---

## 🏢 Studi Kasus 2: Pelayanan Masyarakat

Studi kasus ini bertujuan untuk mengevaluasi tingkat kepuasan masyarakat terhadap pelayanan publik secara lebih objektif menggunakan pendekatan fuzzy.

### Variabel dan Himpunan Fuzzy

#### Input (Antecedents)
- **Kejelasan Informasi**: 0 – 100 (Tidak Memuaskan, Cukup, Memuaskan)  
- **Kejelasan Persyaratan**: 0 – 100 (Tidak Memuaskan, Cukup, Memuaskan)  
- **Kemampuan Petugas**: 0 – 100 (Tidak Memuaskan, Cukup, Memuaskan)  
- **Ketersediaan Sarana & Prasarana**: 0 – 100 (Tidak Memuaskan, Cukup, Memuaskan)  

#### Output (Consequent)
- **Kepuasan Pelayanan**: 0 – 400  
  (Tidak Memuaskan, Kurang, Cukup, Memuaskan, Sangat Memuaskan)

### Aturan Fuzzy (Rules)

Sistem menggunakan sekitar 13 aturan inferensi yang mengombinasikan seluruh variabel input untuk menghasilkan tingkat kepuasan akhir.

---

## 🛠️ Prasyarat

Sebelum menjalankan program, pastikan sudah tersedia:
- Python 3.x  
- Library yang dibutuhkan:
  - numpy  
  - scikit-fuzzy  
  - matplotlib  

### Instalasi
```bash
pip install numpy scikit-fuzzy matplotlib
```

---

## 🚀 Cara Menjalankan

Gunakan terminal atau command prompt untuk menjalankan program:

```bash
python kasus_1_petshop.py
python kasus_2_pelayanan.py
```

---

## 📊 Output Program

Program akan menghasilkan:
- Nilai hasil defuzzifikasi sebagai output utama  
- (Opsional) visualisasi grafik fungsi keanggotaan  

---

## ⚠️ Catatan

- Pastikan semua library sudah terinstall dengan benar  
- Periksa kembali aturan fuzzy jika hasil tidak sesuai ekspektasi  
- Gunakan rentang variabel yang konsisten dengan definisi fungsi keanggotaan  

---
