
##latihan no 1
print("\n Nomer 1")
# A
data = ["motor","mobil","sepeda","bus"]
print(f"nama kendaraan sebelum ditambah = \n{data}")
data.append ("truk")
print(f"nama kendaraan setelah ditambah = \n{data}")
# B
data.insert (1,"becak")
print(f"data ada becak = \n{data}")
# C
data.pop()
print(f"hapus data paling belakang = \n{data}")
# D
data [3] = "skuter"
print(f"data setelah diganti skuter = \n{data}")
# E
jumlah_data = len(data)
print(f"jumlah total semua data = \n{jumlah_data}")

print("\n Nomer 2")
##No 2
# A

angka = [75,80,90,75,85,100,65]
print(f"data skor = \n{angka}")
index_100 = angka.index (100)
print(f"skor 100 ada di index = \n{index_100}")

# B
jumlah_skor_75 = angka.count(75)
print(f"siswa yang dapat skor 75 ada \n{jumlah_skor_75}")

# C 
print(f"skor sebelum diurutkan = \n{angka}")
angka.sort()
print(f"skor setelah diurutkan = \n{angka}")

# D
angka.reverse()
print(f"skor dari terbesar ke terkecil = \n{angka}")

# No 3
print("\n Nomer 3")
menu = ["Nasi Goreng","Mie Ayam"]
print(f"menu utama = \n{menu}")

menu_tambahan = ["Kerupuk","Es Teh"]
print(f"menu tambahan = \n{menu_tambahan}")
menu.extend(menu_tambahan)
print(f"semua menu = \n{menu}")

# NO 4 
# A
print("\n Nomer 4")
data_barang =[["buku",5000],["pensil",2000],["penggaris",3000]]
harga_pensil = data_barang[1][1]
print(f"harga pensil = Rp.{harga_pensil}")

# B

for nama, harga in data_barang:
    print(f"nama barang  = {nama}")
    print(f"harga barang = Rp. {harga}")
