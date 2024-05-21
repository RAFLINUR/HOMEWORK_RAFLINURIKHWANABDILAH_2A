import modul as mod
print("Selamat datang di program manajemen stock barang!")
print("Pilihan :")
print("1. Tambah data barang")
print("2. Edit data")
print("3. Hapus data barang")
print("4. Cari data")
print("5. Tampilkan data barang")
print("6. Tampilkan jumlah data")
print("7. Keluar")
print('\n')

while True:
    pilihan = int(input("Masukkan pilihan : "))
    print("============================")
    if pilihan == 1:
        mod.add_barang()
    elif pilihan == 2:
        mod.edit_barang()
    elif pilihan == 3:
        mod.delete_barang()
    elif pilihan == 4:
        mod.search_barang()
    elif pilihan == 5:
        mod.list_barang()
    elif pilihan == 6:
        mod.total_barang()
    elif pilihan == 7:
        exit()