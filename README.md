1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

```
1) Setup venv untuk tugas 2 dengan perintah 'python -m venv .venv'
2) Buat file requirements.txt dan masukkan library yang ingin diinstall di venv dan buat file .gitignore
3) Buat projek django baru dengan perintah 'django-admin startproject gotoko .'
4) Buat aplikasi baru bernama main dengan perintah 'python manage.py startapp main'
5) Tambahkan main ke dalam variabel INSTALLED_APPS di settings.py di dalam direktori 'gotoko'
6) Buat model Product yang berisi atribut 'name, price, description, category, stock, created_at' di file models.py dalam direktori main
7) Buat migrasi model dan aplikasikan migrasi ke dalam basis data lokal dengan perintah 'python manage.py makemigrations' lalu 'python manage.py migrate'
8) Pada views.py dalam direktori main, tambahkan function untuk yang akan mereturn request, main.html, dan context
9) Buat folder bernama templates dalam direktori main dan buat main.html yang menampilkan nama toko, nama, dan kelas
10) Konfigurasi routing url pada direktori main dengan membuat file urls.py dan tambahkan kode yang diperlukan
11) Konfigurasi routing url pada direktori gotoko dengan menambahkan 'path('', include('main.urls'))'
12) Jalankan program dengan perintah 'python manage.py runserver'
```

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

```
Client HTTP Request (Browser) ----> URLs (urls.py) ----> Django Views (views.py) ----> Django Models (models.py) <----> Database
                                   |
                                   v
                            Django Templates (HTML)
                                   |
                                   v
Back to Client   <----   Response (HTML Content)

Django merupakan framework yang menggunakan struktur MVT atau Model-Views-Template. Model merupakan sebuah objek yang mendefinisikan entitas pada database beserta konfigurasiny, lalu Views berperan sebagai logika utama dari aplikasi yang akan melakukan pemrosesan terhadap permintaan yang masuk, dan Template berperan sebagai tampilan yang akan dikembalikan kepada pengguna.
Dalam django, MVT ini saling berhubungan. Pertama, client mengirimkan HTTP Request dan permintaan yang masuk ke dalam server django akan diproses melalui URLS untuk diteruskan ke VIEWS yang sudah kita buat untuk memproses permintaan tersebut. Jika terdapat proses yang memerlukan penggunaan database, VIEWS akan memanggil query ke MODELS dan database akan mengembalikan hasil query tersebut ke VIEWS. Setelah permintaan telah selesai diproses, hasil proses tersebut akan dipetakan ke dalam HTML yang sudah dibuat sedemikian rupa sebelum akhirnya dikembalikan ke pengguna sebagai Response.
```

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

```
   Git merupakan version control system yang berfungsi untuk mengelola perubahan kode pada code base pengembangan perangkat lunak. Selain melakukan version control, git juga dapat digunakan untuk melakukan kolaborasi dalam project yang sama dengan developer lain.
```

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

```
   Menurut saya, karena django merupakan framework yang populer di kalangan developer dan django memiliki dokumentasi yang lengkap dan jelas. Selain itu, django merupakan All-in-One Framework, artinya django menyediakan semua yang dibutuhkan untuk membangun aplikasi web, termasuk ORM, sistem template, dan autentikasi pengguna.
```

5. Mengapa model pada Django disebut sebagai ORM?

```
ORM atau Object Relational Mapping adalah teknik untuk memetakan basis data relasional ke model objek. Django ORM merupakan suatu cara membuat SQL untuk melakukan query, manipulasi basis data, dan mendapatkan sebuah hasil dengan menggunakan bahasa pemrograman Python. Django disebut sebagai ORM karena dapat melakukan pemetaan tabel ke dalam basis data dan melakukan manipulasi data, seperti Create, Read, Update, Delete dalam basis data menggunakan metode objek tanpa harus menulis SQL.
```
