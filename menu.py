merah="33[31;1m"
def menu ():
 print merah+"----- MENU -----"
 print merah+"1. KASIR"
 print merah+"2. KALKULATOR"
 print merah+"----------------"
 pilih = input("Pilih menu : ")
 if pilih == 1:
  kasir()
 elif pilih == 2:
  kalkulator()
 else:
  exit
 tanya()
  
def kasir ():
 print "----- KASIR -----"
 aqua = 3000
 roti = 1000
 barang = raw_input("Nama Barang : ")
 print "Harga Barang : ",aqua
 barang = raw_input("Nama Barang : ")
 print "Harga Barang : ",roti
 total = (aqua+roti)*90/100
 print "Total bayar setelah diskon 10% : ",total
 tanya()

def kalkulator ():
 print "--- KALKULATOR ---"
 print "1. (+) 3. (*)"
 print "2. (-) 4. (/)"
 print "------------------"
 operasi = input("Pilih operasi : ")
 a = input("a : ")
 b = input("b : ")
 if operasi == 1:
  print "Hasil = ",a+b
 elif operasi == 2:
  print "Hasil = ",a-b
 elif operasi == 3:
  print "Hasil = ",a*b
 elif operasi == 4:
  print "Hasil = ",a/b
 else:
  print "ERROR"
 tanya()
 
def tanya ():
 tanya = raw_input("Kembali ke menu (y/t)? ")
 if tanya == "y":
  menu()
 elif tanya == "t":
  exit
 else:
  print "Salah input"

menu()
