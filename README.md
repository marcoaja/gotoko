1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

```
- Pertama, setup venv untuk tugas 2 dengan perintah 'python -m venv .venv'
- Kedua, buat file requirements.txt dan masukkan library yang ingin diinstall di venv dan buat file .gitignore
- Ketiga, buat projek django baru dengan perintah 'django-admin startproject gotoko .'
- Keempat, buat aplikasi baru bernama main dengan perintah 'python manage.py startapp main'
- Kelima, tambahkan main ke dalam variabel INSTALLED_APPS di settings.py di dalam direktori 'gotoko'
- Keenam, buat model Product yang berisi atribut 'name, price, description, category, stock, created_at' di file models.py dalam direktori main
- Ketujuh, buat migrasi model dan aplikasikan migrasi ke dalam basis data lokal dengan perintah 'python manage.py makemigrations' lalu 'python manage.py migrate'
- Kedelapan, pada views.py dalam direktori main, tambahkan function untuk yang akan mereturn request, main.html, dan context
- Kesembilan, buat folder bernama templates dalam direktori main dan buat main.html yang menampilkan nama toko, nama, dan kelas
- Kesepuluh, konfigurasi routing url pada direktori main dengan membuat file urls.py dan tambahkan kode yang diperlukan
- Kesebelas, konfigurasi routing url pada direktori gotoko dengan menambahkan 'path('', include('main.urls'))'
- Keduabelas, jalankan program dengan perintah 'python manage.py runserver'
```

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

```
...
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
...
```
