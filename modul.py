stok = [
    {"nama" : "Sirion", "stok": 12},
    {"nama" : "Pajero", "stok": 28},
    {"nama" : "Fortuner", "stok": 11},
    {"nama" : "BMW E36", "stok": 3}

]

def add_barang():
    input_nama = input("Masukkan nama barang : ").title()
    input_stok = int(input("Masukkan stok barang : "))
    item = {'nama' : input_nama, 'stok' : input_stok}
    stok.append(item)
    print("==== Data berhasil ditambahkan ====")
    return '\n'

def edit_barang():
    number = 1
    if stok:
        print("==== Data barang ====")
        for i in stok:
            print(f"{number}. {i['nama']} , Stok : {i['stok']}")
            number += 1
        print("============================")
        index = int(input("Ubah data ke : "))
        index -= 1
        if 0 <= index < len(stok):
            input_nama = input("Masukkan nama barang : ").title()
            input_stok = int(input("Masukkan stok barang : "))
            data_change = {'nama' : input_nama, 'stok' : input_stok}
            stok[index] = data_change
            print("==== Data berhasil diperbarui ====")
        else:
            print("Indeks tidak valid.")
    else:
        print("==== Data barang kosong ====")
    return '\n'

def delete_barang():
    number = 1
    if stok: 
        print("==== Data barang ====")
        for i in stok:
            print(f"{number}. {i['nama']} , Stok : {i['stok']}")
            number += 1
        print("============================")
        index = int(input("Hapus data ke : "))
        index -= 1
        if 0 <= index < len(stok):
            del stok[index]
            print("==== Data berhasil dihapus ====")
        else:
            print("Indeks tidak valid.")
    else:
        print("==== Data barang kosong ====")
    return '\n'

def search_barang():
    data_input = input("Cari nama barang : ").title()
    number = 1
    stock = []
    for i in stok:
        if data_input in i['nama']:
            stock.append(i)
    if stock:
        for i in stock:
            print(f"{number}. {i['nama']} , Stok : {i['stok']}")
            number += 1
    else:
        print("==== Data barang tidak ditemukan ====")
    return '\n'

def list_barang():
    number = 1
    if stok:
        print("--- Data barang ---")
        for i in stok:
            print(f"{number}. {i['nama']} , Stok : {i['stok']}")
            number += 1
    else:
        print("==== Data barang kosong ====")
    return '\n'

def total_barang():
    print(f"Jumlah data tersimpan : {len(stok)}")
    return '\n'
