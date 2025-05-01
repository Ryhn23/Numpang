# Numpang - File Sharing Sementara

Aplikasi web sederhana untuk berbagi file secara sementara. File yang diupload akan otomatis terhapus setelah 30 menit.

## Fitur

- Upload file hingga 500MB
- Link download yang bisa dibagikan
- File otomatis terhapus setelah 30 menit
- Antarmuka modern dan responsif
- Drag & drop file

## Persyaratan

- Python 3.7 atau lebih baru
- pip (Python package manager)

## Instalasi

1. Clone repository ini
2. Buat virtual environment (opsional tapi direkomendasikan):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # atau
   venv\Scripts\activate  # Windows
   ```
3. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Aplikasi

1. Pastikan virtual environment aktif (jika menggunakan)
2. Jalankan aplikasi:
   ```bash
   python app.py
   ```
3. Buka browser dan akses `http://localhost:5000`

## Penggunaan

1. Buka aplikasi di browser
2. Drag & drop file atau klik area upload untuk memilih file
3. Tunggu hingga upload selesai
4. Salin link download yang diberikan
5. Bagikan link tersebut kepada orang yang ingin mengunduh file

## Catatan

- File akan otomatis terhapus setelah 30 menit
- Maksimal ukuran file adalah 500MB
- Semua jenis file diperbolehkan

## License
This project is licensed under the [MIT License](LICENSE).
