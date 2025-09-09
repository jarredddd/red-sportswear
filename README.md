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