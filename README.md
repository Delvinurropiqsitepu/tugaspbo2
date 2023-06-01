Penjelasan code:
Kode tersebut adalah implementasi dari beberapa kelas yang berhubungan dengan entitas Mahasiswa, Jurusan, dan Universitas. Berikut adalah penjelasan dari setiap kelas dan metode yang ada dalam kode tersebut:

1. Kelas Mahasiswa:
   - Kelas ini memiliki metode __init__() yang digunakan sebagai metode inisialisasi untuk menginisialisasi objek Mahasiswa. Metode ini menerima tiga parameter: nama, nim, dan jurusan. Setelah menerima parameter tersebut, nilai-nilai tersebut disimpan dalam atribut-atribut objek Mahasiswa.
   - Kelas ini juga memiliki metode tampilkan_info() yang digunakan untuk menampilkan informasi mahasiswa seperti nama, nim, dan nama jurusan.

2. Kelas Jurusan:
   - Kelas ini memiliki metode __init__() yang digunakan sebagai metode inisialisasi untuk menginisialisasi objek Jurusan. Metode ini menerima satu parameter yaitu nama_jurusan. Setelah menerima parameter tersebut, nilai tersebut disimpan dalam atribut NamaJurusan dan DaftarMahasiswa diatur sebagai daftar kosong.
   - Kelas ini juga memiliki metode tambah_mahasiswa() yang digunakan untuk menambahkan objek Mahasiswa ke daftar mahasiswa dalam jurusan.
   - Kelas ini juga memiliki metode tampilkan_daftar_mahasiswa() yang digunakan untuk menampilkan daftar mahasiswa yang terdaftar dalam jurusan.

3. Kelas Universitas:
   - Kelas ini memiliki metode __init__() yang digunakan sebagai metode inisialisasi untuk menginisialisasi objek Universitas. Metode ini menerima satu parameter yaitu nama_universitas. Setelah menerima parameter tersebut, nilai tersebut disimpan dalam atribut NamaUniversitas dan DaftarJurusan diatur sebagai daftar kosong.
   - Kelas ini juga memiliki metode tambah_jurusan() yang digunakan untuk menambahkan objek Jurusan ke daftar jurusan dalam universitas.
   - Kelas ini juga memiliki metode tampilkan_daftar_jurusan() yang digunakan untuk menampilkan daftar jurusan yang ada dalam universitas.

Pada bagian akhir kode, terdapat beberapa langkah eksekusi untuk membuat objek-objek dan memanggil metode-metode yang ada dalam kelas-kelas tersebut:
- Membuat objek Universitas dengan nama "XYZ University".
- Membuat objek Jurusan dengan nama "Teknik Informatika" dan menambahkannya ke dalam Universitas XYZ.
- Membuat objek Mahasiswa dengan input dari pengguna, kemudian menambahkannya ke Jurusan Teknik Informatika.
- Menampilkan daftar jurusan yang ada di Universitas XYZ.
- Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ.

dan menghasilkan output sebagai berikut:
output:
========================================================> 
Masukkan nama mahasiswa: Delvi nur ropiq sitepu
Masukkan NIM mahasiswa: G1A022005
========================================================>
Masukkan nama mahasiswa: DAVI
Masukkan NIM mahasiswa: G1A022001
========================================================>
Daftar Jurusan di Universitas XYZ University
- Nama Jurusan: Teknik Informatika
Daftar Mahasiswa di Jurusan Teknik Informatika
- Nama: Delvi nur ropiq sitepu
  NIM: G1A022005
- Nama: DAVI
  NIM: G1A022001
PS D:\PSDA4\SDA-N>

