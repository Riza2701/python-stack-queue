#Percobaaan 4: Tumpukan Barang di Sebuah Gudang (Stack)
stack = []

def tambah(stack, data):
    stack.append(data)
    print(f"{data[0]} berhasil ditambahkan ke dalam stack.")
    
def hapus_buku_terakhir(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada barang yang dapat dihapus.")
    else:
        buku_terakhir = stack.pop()
        print(f"{buku_terakhir} berhasil dihapus dari stack.")
        
def tampilkan_buku_teratas(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada barang yang dapat ditampilkan.")
    else:
        buku_teratas = stack[-1]
        print(f"Barang teratas di dalam stack adalah {buku_teratas}.")
        
while True:
    print("\nGudang saat ini:", stack)
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Hapus Buku Terakhir")
    print("3. Tampilkan Buku Teratas")
    print("4. Keluar")
        
    pilihan = input("Masukkan Pilihan Anda (1/2/3/4): ")
        
    if pilihan == "1":
        buku_baru = input("Masukkan nama buku yang akan ditambahkan:")
        penulis = input("Masukkan penulis buku yang akan ditambahkan:")
        tambah(stack, [buku_baru, penulis])
    elif pilihan == "2":
        hapus_buku_terakhir(stack)
    elif pilihan == "3":
        tampilkan_buku_teratas(stack)
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silahkan masukkan pilihan yang benar.")