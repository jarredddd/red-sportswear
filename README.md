TUGAS 2 ----------------------------------------------------------------------------------------------------------------------------------------------

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

TUGAS 3 ----------------------------------------------------------------------------------------------------------------------------------------------

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

7. Berikut screenshot dari Postman : 
<img width="2559" height="1599" alt="Screenshot 2025-09-13 214615" src="https://github.com/user-attachments/assets/48174a49-0368-4da8-925b-eeefc7118d91" />
<img width="2559" height="1599" alt="Screenshot 2025-09-13 214627" src="https://github.com/user-attachments/assets/85abde67-9cfb-4a93-b1c5-9463f9cc2050" />
<img width="2559" height="1599" alt="Screenshot 2025-09-13 214732" src="https://github.com/user-attachments/assets/e7cc2699-b3ca-450b-a947-ffa3fc564db6" />
<img width="2538" height="1584" alt="Screenshot 2025-09-13 215059" src="https://github.com/user-attachments/assets/7655e24d-dc46-4159-9247-a5dfecbdc0fe" />

TUGAS 4 ----------------------------------------------------------------------------------------------------------------------------------------------

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya. Django AuthenticationForm adalah sebuah class bawaan Django yang berfungsi untuk menjalankan proses login. AuthenticationForm menerima 2 field input, yaitu username dan password dan akan membandingkan 2 field tersebut dengan data user yang ada di dalam database. Kelebihan dan kekurangan dari AuthenticationForm adalah : 
    a. Kelebihan : 
    Karena sudah bawaan dari Django, maka pengimplementasiannya cepat dan juga mudah, kita gausahnulis logic buat validasinya dari awal, tinggal pakai.
    AuthenticationForm juga punya basic untuk menjalankansistem login.
    b. Kekurangan : 
    Karena AuthenticationForm hanya menerima username, untuk keperluan login akun menggunakan email, kita harus memodifikasi AuthenticationForm. Penampilannya juga masih basic, sehingga diperlukan untuk menggunakan CSS agar penampilannya lebih menarik.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentifikasi itu adalah memverifikasi user, seperti saat login, user akan memasukkan username dan password. Lalu, sistem akan membandingkan input usernam dan password user dengan data user yang ada di database. Sedangkan otorisasi adalah menentukan hal-hal yang bisa dilakukan dan yang tidak bisa dilakukan oleh user. Django mengimplementasikan autentikasi dengan AuthenticationForm. Sedangkan untuk otorisasi, django mengimplementasikannya dengan decorator yang ada di views.py, yaitu '@login_required' yang berada di atas fungsi 'show_main' dan 'show_products'. Saat decorator tersebut ditaruh diatas kedua fungsi tersebut, maka halaman utama dan detail produk tidak bisa diakses oleh user yang sudah login.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
    a. Session
    Session mempunyai tingkat keamanan yang lebih tinggi karena penyimpanan datanya di server, bukan client-side. Penyimpanan datanya juga punya kapasitas yang mengikuti database server yang terkadang besar. Karena penyimpanan data di server, maka server mempunyai workload yang lebih berat, session juga mempunyai masa berlaku yang terbatas. Contohnya, Scele. Sesi user akan otomatis berhenti jika sudah lama tidak digunakan oleh user.

    b. Cookies
    Karena cookies menyimpan data secara client-side, maka cookies tidak terlalu membebani server. Cookies juga mempunyai masa berlaku yang sangat lama, tidak seperti session. Namun, karena cookies disimpan di browser, maka cookies rentan terhadap serangan pihak ketiga. Contohnya adalah penyerang dapat mencuri cookies ketika kita mengakses situs web yang tidak menggunakan https dengan wifi publik. Cookies juga mempunyai kapasitas yang terbatas, yaitu sekitar 4 kb / domain yang hanya bisa menyimpan data teks yang sedikit.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Tidak, penggunaaan cookies tidak aman secara default karena mempunyai risiko terhadap beberapa faktor : 
    1. Saat kita masuk ke website yang tidak menggunakan https dengan wifi publik, penyerang yang menggunakan wifi publik yang sama dapat mengambil isi dari cookies.
    2. Penyerang dapat memasukkan script (Javascript) yang dapat membaca isi cookies dan mengirimkannya ke server penyerang terhadap website yang keamanannya kurang
    3. Penyerang dapat menipu browser dari user yang sudah login untuk mengirimkan request palsu ke server (CSRF)
Django tidak menyimpan data sesi seperti username di dalam cookie, tapi hanya menyimpan sessionid (key) yang dapat digunakan untuk mengambil data sesi dari database kalo dibutuhkan. Setiap permintaan seperti POST punya token CSRF untuk setiap sesi pengguna. Token itu juga di render menggunakan tag csrf_token yang ada di 'login.html', 'register.html', dan 'add_products.html' serta disimpen di cookie. Django akan membandingkan token dari form dengan token yang ada di cookie, kalo beda permintaan akan ditolak. Di file 'settings.py', ada variabel 'SECRET_KEY' yang gunanya untuk memverifikasi apakah nilai cookie udah diubah sama pihak selain Django.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya. -> Hal tsb saya lakukan dgn membuat template html yang berfungsi buat ngatur gimana user menggunakan 3 fitur tsb. Saya juga menambah 3 fungsi baru di 'views.py' buat ngatur logic dari ketiga fitur tsb. Saya juga melakukan routing di 'urls.py' 
    - Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal. -> Saya melakukannya dengan membuat 2 akun user, lalu untuk setiap akun, saya menambahkan masing-masing 3 produk di 2 akun tersebut.
    - Menghubungkan model Product dengan User. -> Hal tsb saya lakukan dengan mengubah 'models.py' sedemikian rupa agar user terhubung dengan objek produk (many-to-one). Di file 'views.py', saya menambahkan beberapa line kode di fungsi 'add_products.py' yang berfungsi ketika saya membuat objek produk, akan menampilkan user yang menambahkan produk tersebut. Saya menambahkan logika untuk mem-filter produk dengan user yang menambahkanya, tidak lupa menambah kode di 'main.html' agar user bisa menggunakan logika filtering tsb. Saat kita melihat detail dari produk tsb, 'products.html' akan menampilkan siapa yang menambahkan produk tsb. 
    - Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi. -> Pertama, dalam fungsi 'login_user' di file 'views.py', saya set cookie baru bernama last_login yang menyimpan kapan terakhir kali user login. Lalu, saya mengakses cookie tsb pada fungsi 'show_main' dengan melakukan .get(). Untuk mengakses username, saya mengganti 1 baris kode di fungsi 'show_main' yang mengakses variabel username dari objek user.


    TUGAS 5 --------------------------------------------------------------------------------------------------------------------------------


1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Berikut ini urutannya dari yang paling atas : 
    - !important | Contoh penggunaan : 
    p {color: red !important;}
    - Inline style, yaitu menerapkan CSS langsung pada elemen HTML | Contoh penggunaan : 
    <p style="color: red">blablabla</p>
    - ID Selector, yaitu selector yang gunakan ID unik dari sebuah elemen, ID nya ditandai dengan # | Contoh penggunaan : 
    #intro {color: red;}
    - Class, pseudo-class, dan attribute selector
        Class menargetkan elemen dengan atribut class yang diawali dengan "." -> .btn {...}
        Pseudo-class menargetkan elemen dalam keadaan tertentu seperti :hover dan :focus -> :hover {...}
        Attribute selector menargetkan elemen berdasarkan atribut dan nilainya -> [type="text"] {...}
    - Type selector dan pseudo-element selector
        Type selector menargetkan semua elemen dari tipe tertentu seperti p, h1, div -> p {color: red}
        Pseudo element selector menargetkan bagian tertentu dari suatu elemen -> p::first-line {font_weight: bold;}

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design merupakan konsep yang sangat penting karena dapat memastikan aplikasi web dapat berfungsi dengan baik di berbagai perangkat seperti mempunyai ukuran screen yang berbeda. Website sekarang umumnya sudah menggunakan responsive design seperti Youtube, Google, dan lain-lain. Untuk website yang belum menggunakan responsive design, contohnya adalah SIAKNG yang belum menyesuaikan ukuran tampilan web untuk smartphone.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin merupakan ruang yang kosong disekitar border, border merupakan garis tepian yang membungkus konten dan paddingnya, sedangkan padding merupakan ruang kosong di dalam elemen (antara konten dan border). Dalam file css, buat .nama_kelas yang berisikan properti margin, border, dan padding. Contoh : 
.nama_kelas {
    padding:...px
    border:...px
    margin:...px
}

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flex box adalah model tata letak yang digunakan untuk mengatur item dalam 1 dimensi, baris (horizontal) dan kolom (vertikal). Biasanya flex box digunakan untuk buat navigation bar dan menyusun item secara sejajar dalam 1 sumbu, berderet atau bertumpuk.
Sebenernya grid layout mirip sama flex box, bedanya grid layout itu mengatur secara 2 dimensi, jadi bisa sekaligus. Grid layout biasanya dipake buat halaman web (header, sidebar, konten, footer).

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
    - Implementasikan fungsi untuk menghapus dan mengedit product. -> Saya buat fungsi 'edit_product' dan 'delete_product' di file 'views.py'. Lalu, di 'urls.py', saya mengimport kedua fungsi tersebut dan menambah path. Setelah itu, saya menambahkan 1 file html, yaitu 'edit_product' yang berfungsi untuk mengarahkan ke url untuk edit produk.
    - Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut -> Untuk halaman login, register, tambah product, edit product, dan detail product, saya menambah elemen seperti tombol-tombol dan kotak untuk menginput variabel yang interaktif. Di detail produk, saya berusaha untuk membuat layout seperti di Tokopedia dan juga menambah 2 tombol, yaitu masukkan keranjang dan beli sekarang untuk sekedar menambah estetika walaupun tombol tsb belum ada aksi yang di assign.
    Untuk halaman produk, saya menambahkan alamat yang mengarahkan ke folder static yang berisikan foto yang akan ditampilkan saat tidak ada produk sama sekali di 'main.html'.
    Saya menambahkan file 'card_product.html' yang akan menampilkan semua produk yang ada. Pertama, saya membuat 'article' yang menyelimuti 'division' yang menyimpan foto dari produk dan juga satu tombol. Lalu, saya membuat 'division' lagi diluar 'article' yang menampung nama produk dan juga harga dari produk.
    Dalam 'card_product', saya membuat 2 tombol edit dan delete dengan menambah 'division' dalam 'article' yang berisikan 'anchor'.
    Untuk membuat navigation bar, saya menambah file baru yaitu 'navbar.html'. File tsb berisikan opsi-opsi tampilan untuk device smartphone dan juga desktop. Agar aplikasi dapat milih mana navbar yang akan ditampilkan, dalam file 'base.html' ada 1 line kode yaitu :
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /> yang berfungsi untuk menyesuaikan dengan lebar layar device.


TUGAS 6
1. Apa perbedaan antara synchronous request dan asynchronous request?
Synchronous request itu adalah saat browser minta sesuatu (contoh : mengklik link), browser akan di lock dan menampilkan layar loading sampai server memberikan halaman baru secara utuh. 1 halaman akan di reload. Untuk synchronous request, browser bisa mengirim permintaan ke server di background tanpa harus reload seluruh halaman. User tetap bisa berinteraksi dengan bagian lain dari website sambil menunggu respons dari server.

2. Bagaimana AJAX bekerja di Django (alur request–response)?
User minta sesuatu (Browser) - Javascript jalan - Django respons (server) - Javascript terima dan ubah tampilan (Browser)

3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
    - Respons lebih cepat : Karena server hanya mengirim data kecil (JSON) dan bukan seluruh halaman HTML, CSS, dan JavaScript lagi.\
    - UX yang lebih mulus : Karena user tidak usah melakukan reload halaman setiap lakukan aksi.
    - Ngurangin load server : Server gausah perlu repot-repot load ulang seluruh halaman HTML setiap saat. Cukup proses logika dan kirim data.
    - 
4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
    - CSRF Token dalam header request
    - Menggunakan HTTPS
    - Lakukan validasi di server side
    - Pakai decorator Django (@login_required)

5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
    - Halaman web lebih responsive : Saat user mengklik sesuatu dan langsung melihat hasilnya tanpa menunggu halaman reload.
    - Alur yang tidak terputus: User tidak kehilangan konteks. Misalnya, saat mengisi form panjang dan ada validasi username via AJAX, user tidak perlu meninggalkan halaman form hanya untuk tahu username-nya sudah dipakai.
    - Memungkinkan fitur kompleks, contoh  : fitur map yang bisa di geser dan di zoom di Google Maps