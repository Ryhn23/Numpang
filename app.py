import os
import uuid
import logging
from datetime import datetime, timedelta
from flask import Flask, render_template, request, send_file, url_for, flash, redirect, abort
from werkzeug.utils import secure_filename
import shutil
from werkzeug.middleware.proxy_fix import ProxyFix

# Setup logging
logging.basicConfig(
    filename='numpang.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Konfigurasi
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
MAX_CONTENT_LENGTH = 500 * 1024 * 1024  # 500MB
FILE_EXPIRY = 30  # menit

# Buat folder uploads jika belum ada
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config.update(
    UPLOAD_FOLDER=UPLOAD_FOLDER,
    MAX_CONTENT_LENGTH=MAX_CONTENT_LENGTH,
    SECRET_KEY=os.environ.get('SECRET_KEY', os.urandom(24)),
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    PERMANENT_SESSION_LIFETIME=timedelta(minutes=30)
)

def cleanup_expired_files():
    try:
        current_time = datetime.now()
        for filename in os.listdir(app.config['UPLOAD_FOLDER']):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if os.path.isfile(file_path):
                file_time = datetime.fromtimestamp(os.path.getctime(file_path))
                if current_time - file_time > timedelta(minutes=FILE_EXPIRY):
                    os.remove(file_path)
                    logging.info(f"Deleted expired file: {filename}")
    except Exception as e:
        logging.error(f"Error in cleanup: {str(e)}")

@app.before_request
def before_request():
    cleanup_expired_files()

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Tidak ada file yang dipilih')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('Tidak ada file yang dipilih')
            return redirect(request.url)
        
        try:
            # Generate unique filename
            original_filename = secure_filename(file.filename)
            unique_filename = f"{uuid.uuid4()}_{original_filename}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            
            # Simpan file
            file.save(file_path)
            logging.info(f"File uploaded: {original_filename}")
            
            # Generate download URL
            download_url = url_for('download_file', filename=unique_filename, _external=True)
            
            return render_template('success.html', 
                                download_url=download_url, 
                                filename=original_filename)
        except Exception as e:
            logging.error(f"Upload error: {str(e)}")
            flash('Terjadi kesalahan saat mengupload file')
            return redirect(request.url)
    
    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(file_path):
            return send_file(
                file_path,
                as_attachment=True,
                download_name=filename.split('_', 1)[1] if '_' in filename else filename
            )
        logging.warning(f"File not found: {filename}")
        abort(404)
    except Exception as e:
        logging.error(f"Download error: {str(e)}")
        abort(500)

@app.errorhandler(404)
def not_found_error(error):
    return "File tidak ditemukan atau sudah expired", 404

@app.errorhandler(500)
def internal_error(error):
    return "Terjadi kesalahan pada server", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 