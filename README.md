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
- cPanel dengan akses SSH

## Deployment di cPanel

### 1. Setup Git di cPanel

1. Buka cPanel dan masuk ke "Git Version Control"
2. Klik "Create"
3. Isi form dengan:
   - Repository Name: numpang
   - Repository Path: pilih direktori website Anda
   - Clone URL: URL repository Git Anda
4. Klik "Create"

### 2. Setup Python di cPanel

1. Buka "Setup Python App" di cPanel
2. Klik "Create Application"
3. Isi form dengan:
   - Python Version: 3.9 atau lebih baru
   - Application Root: direktori website Anda
   - Application URL: domain/subdomain Anda
   - Application Startup File: passenger_wsgi.py
   - Application Entry point: application
4. Klik "Create"

### 3. Setup Environment

1. Copy `.env.example` ke `.env`:
   ```bash
   cp .env.example .env
   ```
2. Edit `.env` dan set SECRET_KEY dengan nilai yang aman

### 4. Setup Git Hooks

1. Buat file `post-receive` di folder `.git/hooks/`:
   ```bash
   cd .git/hooks/
   touch post-receive
   chmod +x post-receive
   ```

2. Isi file `post-receive` dengan:
   ```bash
   #!/bin/bash
   cd /path/to/your/website
   ./deploy.sh
   ```

### 5. Push ke Repository

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

## Struktur File

```
numpang/
├── .env                  # Environment variables (tidak di-commit)
├── .env.example         # Template environment variables
├── .gitignore          # Git ignore rules
├── .htaccess           # Apache configuration
├── app.py              # Main application
├── deploy.sh           # Deployment script
├── passenger_wsgi.py   # cPanel WSGI configuration
├── requirements.txt    # Python dependencies
├── uploads/            # Upload directory
└── templates/          # HTML templates
    ├── index.html
    └── success.html
```

## Troubleshooting

1. **Error 500**
   - Cek error log di cPanel
   - Pastikan semua dependencies terinstall
   - Pastikan permissions benar

2. **Upload Gagal**
   - Cek ukuran file (max 500MB)
   - Cek permissions folder uploads
   - Cek error log

3. **File Tidak Terhapus**
   - Cek permissions
   - Cek log file
   - Pastikan cron job berjalan

## License
This project is licensed under the [MIT License](LICENSE).
