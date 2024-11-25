# API Layanan Jasa

Sebuah API RESTful berbasis FastAPI untuk mengelola pemesanan layanan, termasuk layanan pijat, kebersihan rumah, dan pertamanan. API ini menyediakan fitur autentikasi, daftar layanan, dan kemampuan manajemen.

## Fitur Utama

- Autentikasi berbasis JWT
- Daftar layanan dengan opsi filter
- Manajemen penyedia layanan
- Penjadwalan ketersediaan
- Kontrol akses berbasis peran (Pengguna/Admin)
- Dokumentasi API interaktif (Swagger UI)

## Memulai

### Persyaratan Sistem

- Python 3.8 atau lebih tinggi
- pip (Pengelola paket Python)

### Instalasi

1. Clone repositori:

```bash
git clone https://github.com/Farisiii/api_tst.git
cd service-booking-api
```

2. Instal dependensi:

```bash
pip install -r requirements.txt
```

3. Jalankan server:

```bash
uvicorn main:app --reload
```

Server akan berjalan di `http://localhost:8000`

## Dokumentasi API

Dokumentasi API tersedia melalui Swagger UI di `http://localhost:8000/docs`. Berikut cara penggunaannya:

### Cara Mengakses Swagger UI

1. Jalankan server dan buka `http://localhost:8000/docs` di browser Anda
2. Anda akan melihat antarmuka dokumentasi Swagger yang interaktif

### Langkah-langkah Autentikasi

Sebelum menguji endpoint yang dilindungi, Anda perlu melakukan autentikasi:

1. Temukan bagian "authentication"
2. Daftar pengguna baru:

   - Klik POST `/register`
   - Klik "Try it out"
   - Isi email dan password pada request body:

   ```json
   {
     "email": "pengguna@contoh.com",
     "password": "passwordkuat123"
   }
   ```

   - Klik "Execute"

3. Login untuk mendapatkan token akses:

   - Klik POST `/login`
   - Klik "Try it out"
   - Gunakan kredensial yang sama
   - Jalankan request
   - Salin `access_token` dari respons

4. Autorisasi di Swagger UI:
   - Klik tombol "Authorize" di bagian atas halaman
   - Masukkan token dengan format: `Bearer token_anda`
   - Klik "Authorize"
   - Tutup dialog autorisasi

Sekarang Anda bisa menguji semua endpoint yang dilindungi!

### Cara Menguji Endpoint

Setelah autentikasi, Anda dapat menguji berbagai endpoint:

1. Melihat Daftar Layanan:

   - GET `/services`
   - Mendukung parameter query opsional:
     - `service_type`: Filter berdasarkan jenis layanan (contoh: "Massage")
     - `date`: Filter berdasarkan tanggal (format YYYY-MM-DD)

2. Melihat Layanan Spesifik:

   - GET `/services/{service_id}`
   - Memerlukan ID layanan di path
   - Mendukung filter tanggal opsional

3. Menambah Layanan Baru (Khusus Admin):
   - POST `/services`
   - Memerlukan autentikasi admin
   - Sertakan detail layanan di request body

### Data Contoh

API dilengkapi dengan data contoh termasuk:

Tipe layanan (type):

- Massage
- Housekeeping
- Gardening

Tanggal yang tersedia (date):

- 2023-05-01
- 2023-05-02
- 2023-05-03

### Akun Default

Untuk keperluan pengujian, Anda dapat menggunakan akun yang sudah dikonfigurasi:

- Pengguna Biasa:
  - Email: `example@email.com`
  - Password: `password123`
- Pengguna Admin:
  - Email: `admin@email.com`
  - Password: `admin123`

## Penanganan Error

API memberikan pesan error yang jelas untuk berbagai skenario:

- 400: Bad Request (input tidak valid)
- 401: Unauthorized (token tidak valid/kadaluarsa)
- 403: Forbidden (hak akses tidak cukup)
- 404: Not Found (resource tidak ditemukan)

## Catatan Keamanan

- Semua endpoint (kecuali login dan register) memerlukan autentikasi
- Endpoint khusus admin memerlukan peran admin
- Token JWT kadaluarsa setelah 24 jam

## Dokumentasi Alternatif

Selain Swagger UI, Anda juga bisa mengakses dokumentasi API dalam format ReDoc di `http://localhost:8000/redoc`

## Catatan Pengembangan

- API menggunakan validasi request otomatis FastAPI
- Semua model didefinisikan menggunakan Pydantic untuk keamanan tipe data
- JWT digunakan untuk autentikasi yang aman
- Implementasi saat ini menggunakan penyimpanan dalam memori

## Dukungan

Untuk pertanyaan atau masalah, silakan buka issue di repositori atau hubungi tim pengembang.
