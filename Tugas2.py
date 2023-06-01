class Mahasiswa:
    #Metode insialisasi untuk menginisialisasi objek sebagai parameter
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)

class Jurusan:
    # menginisialisasi daftar mahasiswa dalam jurusan 
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = [] 

    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)#metode yang di gunakan untuk menambahkan objek mahasiswa ke daftar mahasisawa dalam jurusan 

    def tampilkan_daftar_mahasiswa(self):
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            print("- Nama:", mahasiswa.nama)
            print("  NIM:", mahasiswa.nim)#metode manmpilkan daftar mahasiswa yang terdaftar dalan jurusan 


class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []#di gunakan untuk menginialisasi kan objek universitas sebagai parameter 

    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print("- Nama Jurusan:", jurusan.NamaJurusan)


# Membuat objek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")

# Membuat objek Jurusan dengan nama "Teknik Informatika" dan menambahkannya ke dalam Universitas XYZ
jurusan_ti = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_ti)
print ("========================================================> ")
# Membuat objek Mahasiswa dengan input dari pengguna
nama_mahasiswa = input("Masukkan nama mahasiswa: ")
nim_mahasiswa = input("Masukkan NIM mahasiswa: ")
mahasiswa_1 = Mahasiswa(nama_mahasiswa, nim_mahasiswa, jurusan_ti)
jurusan_ti.tambah_mahasiswa(mahasiswa_1)
print ("========================================================>")
nama_mahasiswa = input("Masukkan nama mahasiswa: ")
nim_mahasiswa = input("Masukkan NIM mahasiswa: ")
mahasiswa_2= Mahasiswa(nama_mahasiswa, nim_mahasiswa, jurusan_ti)
jurusan_ti.tambah_mahasiswa(mahasiswa_2)
print ("========================================================>")
# Menampilkan daftar jurusan yang ada di Universitas XYZ
universitas_xyz.tampilkan_daftar_jurusan()

# Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
jurusan_ti.tampilkan_daftar_mahasiswa()
