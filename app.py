from flask import Flask, render_template, request
import random

app = Flask(__name__)

pesan_default = [
    "Makan patty itu",
    "Berdansalah bersama patrick",
    "Wedus kentir Wedus kentir",
    "Selamat datang di indomaret",
    "555 angka keberuntungan kamu hari ini",
    "8888 adalah angel number hari ini",
    "1111 adalah angel number hari ini",
    "9999 adalah angel number hari ini",
    "akan beruntung hari ini",
    "Happy birthday"
]

@app.route('/')
def index():
    random_message = random.choice(pesan_default)
    return render_template('index.html', random_message=random_message)

@app.route('/get_message', methods=['GET'])
def get_message():
    nama = request.args.get('nama_get')
    if not nama:
        return "Nama tidak ditemukan"
    else:
        pesan = random.choice(pesan_default)
        return render_template('hasil_get.html', nama_get=nama, pesan_get=pesan)

@app.route('/post_message', methods=['POST'])
def post_message():
    nama = request.form.get('nama_post')
    if not nama:
        return "Nama tidak ditemukan"
    else:
        return render_template('hasil_post.html', nama_post=nama, pesan_post=f"Selamat datang, {nama}, berhasil masuk ke Puja Kerang Ajaib")

if __name__ == '__main__':
    app.run(debug=True)
