## TUGAS 2

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

## TUGAS 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

```
Dalam pengembangan sebuah platform, dibutuhkan untuk mengirimkan data yang bisa berupa HTML, XML, atau JSON dari satu stack ke stack lainnya. Tujuannya agar sebuah platform menjadi dinamis dan responsif terhadap interaksi pengguna. Hal ini juga memungkinkan kita untuk memisahkan business logic yang biasanya ditulis dalam views.py dengan tampilan web yang biasanya ditulis dalam direktori templates. Dengan data delivery ini, halaman web akan dapat terupdate otomatis sesuai dengan data yang diubah atau diterima tanpa perlu mengganti struktur HTML secara manual setiap kali ada perubahan data. Oleh karena itu, agar frontend dan backend dapat terhubung dengan baik, diperlukan data delivery dalma pengimplementasian sebuah platform.
```

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

```
Menurut saya lebih baik JSON, karena JSON lebih efisien dan mudah dibaca dengan formatnya seperti "key":"value". Selain itu, JSON dapat menangani sturktur data yang kompleks, seperti objek, array, nested objek atau array, dan nilai primitif, sedangkan XML tidak bisa menangani struktur data yang kompleks, seperti objek atau array. JSON lebih populer dibandingkan XML karena memiliki format yang lebih mudah dibaca dan parsing data di JSON lebih mudah dan cepat. Selain itu juga, JSON dapat menangani struktur data yang kompleks dan banyak bahasa yang memiliki function untuk melakukan parsing terhadap file JSON, seperti dalam bahasa javascript yang memiliki function JSON.parse() dan JSON.stringify().
```

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

```
Dalam Django, method is_valid() pada form Django memiliki fungsi penting dalam proses validasi data yang user masukkan ke dalam form. Method ini digunakan untuk memeriksa apakah data yang dikirimkan melalui form sesuai dengan aturan dan kriteria validasi yang telah ditetapkan pada form tersebut.
Contohnya, validasi field types, apakah input yang dimasukkan adalah integer untuk IntegerField. Jika semua validasi sukses dan semua sesuai, method is_valid() akan mereturn nilai True. Sebaliknya, jika input pada form tidak valid, method ini akan mereturn nilai False.
Kita membutuhkan method ini untuk melakukan verifikasi untuk setiap data yang diinput apakah valid atau tidak. Hal ini berguna untuk mencegah kesalahan dalam penyimpanan data ke database. Selain itu, method ini dibutuhkan untuk menjaga keamanan dengan mencegah input yang berbahaya seperti metode SQL Injection atau XSS.
```

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

```
Dalam Django, csrf_token merupakan mekanisme keamanan yang digunakan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Penyerang dapat mengirimkan link dalam form email, sms, or chat. Penyerang dapat melakukan hal-hal yang  merugikan kepada seseorang yang sudah terdaftar dalam suatu webiste.
Mengapa kita membutuhkan csrf_token saat membuat form di Django?
Pada setiap form yang memerlukan autentikasi pengguna, seperti form login atau register, atau form lain yang melakukan perubahan pada database, Django membuat sebuah token csrf unik untuk setiap sesinya. Token ini terdapat dalam form HTML dan diverifikasi pada server setiap kali user mengirimkan form. Jika token yang dikirimkan user tidak cocok dengan token yang disimpan di server, request user akan ditolak. Jadi, Kita butuh csrf_token untuk melindungi web dari serangan CSRF yang dapat merugikan user.
Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django?
Jika kita tidak menambahkan csrf_token pada form Django, website kita akan menjadi rentan terhadap serangan CSRF di mana penyerang dapat mengirimkan request yang berbahaya ke server.
Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Tanpa token CSRF, penyerang dapat dengan mudah mengirimkan HTTP request dengan identitas user yang valid menggunakan skrip atau elemen HTML tersembunyi. Tanpa token_crsf server tidak dapat membedakan antara permintaan yang sah dari user yang terdaftar dan permintaan palsu yang dibuat oleh penyerang.
```

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

```
1) Buat direktori templates pada root folder dan buat file base.html di dalamnya. File base.html ini berfungsi untuk template dasar sebagai kerangka umum untuk halaman web lain.
2) Tambahkan direktori templates yang sudah dibuat tadi ke dalam variabel TEMPLATES pada file settings.py.
3) Sebelum membuat input form, tambahkan primary key pada model Product yang dibuat sebelumnya dengan menggunakan UUID pada file models.py. Lalu, lakukan migrasi model dengan 'makemigrations' dan 'migrate'.
4) Untuk membuat form input data, buat file forms.py pada direktori main. Form dibuat dengan menggunakan model Product dan memiliki fields "name", "price", "description", "category", "stock".
5) Buat function create_product_entry pada files views.py. Fungsi ini berfungsi untuk menampilkan input form sesuai dengan fields yang ditentukan sebelumnya dan jika form valid dan request berupa POST, maka form akan disimpan dan akan melakukan redirect ke halaman utama.
6) Pada variabel context, tambahkan satu key bernama 'products' dengan value berupa semua product yang ada di dalam data base. Ini berfungsi untuk mengirimkan data-data produk ke file html agar bisa ditampilkan pada halaman web
7) Pada file urls.py, tambahkan path URL atau endpoint untuk halaman web add product.
8) Buat file html pada direktori main/templates untuk tampilan input form add product.
9) Pada main.html di direktori yang sama seperti no 8, tambahkan kode html yang akan menampilkan semua product yang sudah ditambahkan ke database.
10) Pada direktori main dan file views.py, tambahkan function untuk melihat product yang sudah ditambahkan ke database dalam format JSON, XML, JSON by ID, dan XML by ID.
11) Tambahkan endpoint untuk memanggil fungsi untuk melihat product dalam format json dan xml yang sudah dibuat sebelumnya.
```

# POSTMAN

### XML

![XML](image-tugas3/xml.png)

### JSON

![JSON](image-tugas3/json.png)

### XML by ID

![XMLbyID](image-tugas3/xmlbyid.png)

### JSON by ID

![JSONbyID](image-tugas3/jsonbyid.png)

## TUGAS 4

1. Apa perbedaan antara HttpResponseRedirect() dan redirect()

```
Dalam django, HttpResponseRedirect() dan redirect() seringkali digunakan untuk mengarahkan pengguna ke URL berbeda. HttpResponseRedirect() merupakan class django yang digunakan untuk mereturn respon HTTP dengan status code 302 (Found). HttpResponseRedirect() argument pertamanya perlu diisi dengan suatu path yang ingin dikunjungi. Contohnya HttpResponseRedirect('/products/').
redirect() merupakan function pada django yang akan mereturn HttpResponseDirect. Tidak hanya dapat menerima argumen URL, fungsi redirect() dapat menerima beberapa jenis argumen lain, seperti nama view dan sebuah model. Contoh redirect('/products/'), redirect('create_product'), dan redirect(productObject).
Jadi, perbedaan HttpResponseRedirect() dan redirect() adalah HttpResponseRedirect() hanya menerima argumen berupa URL, sedangkan redirect() dapat menerima argumen yang lebih beragam yang membuat redirect lebih praktis untuk digunakan.
```

2. Jelaskan cara kerja penghubungan model MoodEntry dengan User!

```
Pengubungan model MoodEntry dengna User dilakukan agar user yang sedang login atau terotorisasi hanya dapat melihat mood entries miliknya saja. Penghubungan dilakukan dengan menambahkan atribut ForeignKey yang mana key ini akan merujuk ke satu User. Penambahan key ini merupakan suatu relationship one to many atau many to one dimana satu orang user dapat memiliki banyak mood entry atau banyak mood entry dapat dimiliki oleh satu orang user.
Setelah itu, tambahkan kode di fungsi create_product_entry pada file views.py yang bertujuan untuk menyimpan objek yang telah dibuat dari form ke dalam database dimana objek tersebut hanya dimiliki oleh user yang sedang terotorisasi atau login. Selanjutnya ubah function show_main pada views.py dengan mengubah variabel product_entries yang sebelumnya akan mengambil semua object mood yang ada di dalam database menjadi product_entries = Product.objects.filter(user=request.user), dimana mood entries akan disaring dan hanya akan mengambil product entry yang dimiliki oleh user yang sedang login. Setelah itu, lakukan migrasi model dengan makemigrations, lalu aplikasikan migrasi ke database dengan migrate.
```

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

```
Authentication adalah sebuah proses verifikasi terhadap identitas seseorang berdasarkan data yang tersimpan di database. Ketika seseorang login, web django akan memverifikasi apakah username dan password yang diinput oleh pengguna tersebut cocok dengan data yang disimpan dalam database. Apabila cocok, pengguna berhasil terautentikasi dan valid, lalu django akan membuat session login tersebut yang biasanya disimpan sebagai cookie pada perangkat pengguna. Session ini akan memberitahu siapa pengguna yang sedang login.
Authorization merupakan proses untuk memeriksa hak askes pengguna setelah pengguna berhasil terautentikasi. Django dapat menentukan fitur atau halaman web apa saja yang dapat diakses. Contohnya pengguna yang tidak memiliki role admin tidak bisa mengakses halaman edit product, tetapi pengguna dengan role admin dapat menggunakan fitur edit product.

Berikut merupakan contoh implementasi authentication dalam Django.
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

Kode di atas merupakan fungsi login user yang akan melakukan autentikasi kepada user yang akan login. Pada kode tersebut terdapat line 'form = AuthenticationForm(data=request.POST)'.
AuthenticationForm adalah form bawaan Django yang melakukan validasi terhadap input untuk proses login, termasuk memeriksa apakah username dan password yang diinput benar atau tidak.

Berikut merupakan contoh implementasi authorization dalam Django.
@login_required(login_url='/login')
def show_main(request):
    ...

Kode di atas merupakan fungsi show_main yang menampilkan menu utama dan terdapat decorator @login_required yang bertujuan agar fungsi tersebut dapat diakses hanya jika user sudah melakukan login dan autentikasinya berhasil. Decorator login_required disediakan oleh django dengan mengimportnya dari django.contrib.auth.decorators. Line @login_required(login_url='/login') akan mengembalikan user ke halaman login apabila user belum terautentikasi. Apabila user terautentikasi, user akan terotorisasi untuk mengakses halaman utaman pada fungsi show_main.
```

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

```
Django mengingat pengguna yang telah login dengan menggunakan session dan cookies. Ketika pengguna login, Django membuat session di server yang akan menghubungkan data pengguna dengan sesi tersebut. Setiap session ini menyimpan informasi session ID yang unik.
Setelah berhasil login, Django akan membuat sebuah cookie dan akan disimpan di dalam komputer user/client. Cookie ini berisi session ID yang digunakan untuk menghubungkan pengguna dengan session yang ada di server. Session ID dapat dianggap sebagai suatu token (barisan karakter) untuk mengenali session yang unik pada aplikasi web tertentu.
Salah satu kegunaan cookies yang lain adalah menyimpan preferensi pengguna. Cookies dapat digunakan untuk menyimpan informasi tentang pengaturan pengguna seperti bahasa, tema, atau preferensi tampilan. Hal ini dapat membuat user experience menjadi lebih baik.
Tidak semua cookies aman digunakan karena cookies yang dikirim melalui koneksi HTTP tidak terenkripsi, sehingga data yang disimpan dalam cookies rentan dicuri oleh orang lain. Oleh karena itu, sebaiknya pastikan cookies dikirim dalam koneksi HTTPS yang terenkripsi.
```

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

```
> Buat Fitur Registrasi
1) Import UserCreationForm dari django.contrib.auth.forms dan buat fungsi register di views.py yang akan memanggil UserCreationForm untuk membuat form registrasi.
2) Buat file register.html dalam templates pada direktori main untuk menyimpan halaman registrasi.
3) Tambahkan path URL di urls.py yang akan mengarahkan user ke  halaman register saat user mengklik tombol register di halaman login atau saat user mengunjungi endpoint /register.
> Buat Fitur Login
4) Import AuthenticationForm dari django.contrib.auth.forms dan buat fungsi login_user di views.py yang akan memeriksa input user. Jika input valid, program akan memanggil fungsi login untuk memverifikasi username dan password, lalu membuat session baru untuk user yang berhasil login.
5) Buat file login.html dalam templates dalam direktori main untuk menyimpan halaman login.
6) Tambahkan path URL ke urls.py yang mengarahkan ke halaman login.
> Buat Fitur Logout
7) Import logout dari django.contrib.auth dan buat fungsi logout untuk menghapus session pengguna yang sedang login dengan mengirim request logout ke server.
8) Buat tombol logout di main.html agar pengguna dapat keluar dari aplikasi.
9) Tambahkan path URL untuk logout di urls.py agar pengguna dapat menggunakan fungsi logout.
> Restriktsi akses halaman main
10) Import login_required dari django.contrib.auth.decorators dan tambahkan dekorator @login_required tepat sebelum function show_main. User akan diarahkan ke halaman login ketika pertama kali membuka halaman web dan ketika user belum terautentikasi, halaman utama akan direstriksi samapai user terautentikasi.
> Buat cookies dan gunakan data dari cookies
11) Import HttpResponseRedirect dari django.http dan reverse dari django.urls dan tambahkan kondisi akan akan mengecek apakah form valid dengan method .is_valid() pada fungsi login_user.
12) Jika form valid, user akan diarahkan ke halaman main dan buat cookies yang berisi last login user.
13) Ambil data last login dari cookies dan masukkan ke dalam context agar bisa ditampilkan pada halaman web.
14) Pada fungsi logout_user, tambahkan kode agar ketika user logout, user akan diarahkan ke halaman login dan cookies yang berisi last login dihapus.
15) Tampilkan data last login pada halaman main
> Hubungkan model Product dengan User
16) Import User dari django.contrib.auth.models dan buat ForeignKey dalam class ProductEntry pada models.py. ForeignKey ini berguna untuk menghubungkan product entry dengan user melalui sebuah relationship.
17) Pada views.py tambahkan kode ini ke fungsi create_product_entry yang bertujuan untuk menyimpan data dari product yang dibuat oleh user dan disimpan ke dalam database.
18) Ubah product_entries pada fungsi show_main, sehingga objek product yang ditampilkan pada halaman utama hanya milik user yang login saja.
19) Buat satu user sebelum melakukan migration ke database
20) Simpan perubahan model dengan python manage.py makemigrations dan aplikasikan model ke dalam database dengan python manage.py migrate.
```
