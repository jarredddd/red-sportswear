TUGAS 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Membuat sebuah proyek Django baru. -> Pertama, saya buat direktori baru dan mengaktifkan virtual environment. Setelah itu, saya menginstall beberapa dependencies. Lalu, saya membuat file .env.prod yang berisikan kredensial yang diberikan lewat e-mail dan membuat file .env yang berisikan 'Production=False'. Dan yang terakhir, saya menambah dan mengubah isi dari file settings.py yang berada di dalam folder 'red_sportswear' 

- Membuat aplikasi dengan nama main pada proyek tersebut. -> Pertama, saya mengaktifkan virtual environment lalu menjalankan command 'python manage.py startapp main' yang membuat direktori baru yang bernama 'main'. Kedua, saya mendaftarkan direktori main itu di file 'settings.py' dengan menambah string "main" di variabel 'INSTALLED_APPS'.

- Proses routing terbagi menjadi dua, yaitu :
Saya membuat file 'urls.py' di dalam folder 'main' dan mengisi file tersebut seperti yang tertera di tutorial.
Saya juga memodifikasi file 'urls.py' yang terletak di folder utama untuk mengarahkan semua request (untuk konteks tugas ini, berarti request path aplikasi main) ke file 'urls.py' yang dimiliki oleh aplikasi main.

- Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut. -> Saya mengisi file 'models.py' dengan menambah class yang bernama Product yang memiliki atribut-atribut wajib berikut : 
    - name (CharField), untuk menyimpan nama produk
    - price (IntegerField), untuk menyimpan harga produk
    - description (TextField), untuk menyimpan deskripsi dari produk
    - thumbnail (URLField), untuk menyimpan url dari gambar produk
    - category (CharField), untuk menyimpan kategori produk
    - is_featured (BooleanField), untuk menyimpan status apakah produk tersebut unggulan atau tidak
 
 Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu. -> Saya lakukan dengan membuat fungsi show_main yang akan mengirim data dari file 'views.py' ke template html (main.html)
 
 Setelah melakukan semua hal diatas, saya melakukan push ke repositori GitHub dan di deploy juga di PWS agar proyek saya bisa dilihat oleh orang lain.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
https://www.canva.com/design/DAGyf23R2gQ/pyGD0nDHIO8a9uqFaUmX_w/view?utm_content=DAGyf23R2gQ&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hf4db3a8bf9


3. Jelaskan peran settings.py dalam proyek Django!
    File tersebut berperan untuk menyimpan semua pengaturan proyek Django, antara lain : 
    - Mengatur domain/IP yang dapat mengakses server
    - Mengkonfigurasi database yang digunakan (PostgreSQL, SQLite, dan lain-lain)
    - Daftar aplikasi Django yang aktif digunakan (dalam konteks tugas ini adalah folder 'main')
    - Validasi password
    - Mengatur bahasa dan zona waktu yang digunakan

4. Bagaimana cara kerja migrasi database di Django?
    - Django baca perubahan di file 'models.py'
    - Django buat file migrasi yang berisikan perintah Python yang mewakilkan perintah SQL
    - Django baca semua file migrasi yang belum diterapkan
    - Django eksekusi perintah SQL ke database
    - Django catat status migrasi yang udah dijalankan

5. Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    - Punya semua hal yang dibutuhkan untuk membuat aplikasi web
    - Menggunakan bahasa pemrograman python, dimana bahasa tersebut cocok untuk pemula
    - Dokumentasi yang lengkap
    
6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    Sejauh ini tidak ada, sudah membantu saya untuk mengerjakan tutorial dengan baik.

TUGAS 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena data delivery memungkinkan platform untuk mendapatkan update data secara real-time, seperti notifikasi, chat, dan lain-lain. Data delivery juga memungkinkan kemampuan berbagai sistem untuk berinteraksi dan bekerja sama secara efektif dengan menggunakan format yang konsisten. Dalam konteks platform, sistem-sistem tersebut adalah aplikasi web, mobile, dan API dari pihak ketiga.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?|
Menurut saya, JSON lebih baik dikarenakan ukuran filenya ringan, sehingga lebih cepat dibaca. Browser juga dapat langsung membaca dan mengolah file JSON tanpa library tambahan karena sudah bawaan di Javascript. Karena alasan tersebut juga, JSON lebih populer dibandingkan XML.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi dari method is_valid() adalah untuk memvalidasi form yang diisi oleh user, seperti apakah semua field sudah diisi, field yang wajib tidak kosong, dan validasi-validasi custom. Fungsi tersebut akan mereturn True jika semua data valid dan menyimpannya, lalu mereturn False jika tidak dan memberikan error. Kita membutuhkan method tersebut untuk mencegah data yang tidak valid masuk ke database.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita membutuhkan csrf_token karena dapat melindungi aplikasi dari serangan yang memanfaatkan sesi user yang sudah terautentikasi untuk mengirimkan request berbahaya ke server tanpa sepengetahuan user itu sendiri.
Jika tidak menggunakan csrf_token, penyerang dapat membuat form palsu di website lain -> lalu user mengisi form tersebut -> request tersebut dikirim ke server kita (misal : transfer uang). Hal tersebut terjadi karena server tidak bisa membedakan request tersebut muncul dari aplikasi asli atau dari website palsu yang berbahaya. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID. -> Saya lakukan dengan membuat 4 fungsi baru tersebut di file 'views.py'. Intinya fungsi-fungsi tersebut mereturn data dalam format XML dan JSON.
    - Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1. -> Saya lakukan dengan menambah path fungsi-fungsi dari 'views.py' dalam variabel 'urlpatterns' di file 'urls.py'.
    - Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek. -> Saya lakukan dengan : 
        1. Membuat fungsi 'add_products' di file 'views.py' yang akan mengarahkan ke file 'add_products.html' serta menambah path di 'urls.py' yang mengarah ke fungsi tersebut
        2. Membuat fungsi 'show_products' di file 'views.py' yang akan mengarahkan ke file 'products_detail.html' serta menambah path di 'urls.py' yang mengarah ke fungsi tersebut.
        3. Menambah kode di file 'main.html' dengan tombol-tombol yang bisa mengarahkan ke page tambah produk dan lihat detail produk
    - Membuat halaman form untuk menambahkan objek model pada app sebelumnya. -> Saya lakukan dengan membuat file 'forms.py' yang berisikan field apa saja yang akan ditampilkan di form. Lalu, saya mengisi file 'add_products' agar saya dapat mengsubmit form tersebut.
    - Membuat halaman yang menampilkan detail dari setiap data objek model. -> Saya lakukan dengan menambah kode di file 'products_detail' yang akan menampilkan data-data dari objek Produk yang ditambahkan oleh user itu sendiri, seperti nama, kategori, jumlah views, tanggal penambahan produk, dan lain-lain.

6. Asdos sudah sangat membantu saya dalam mengerjakan tutorial 2

