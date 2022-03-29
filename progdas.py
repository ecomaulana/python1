def garis():
    print("===============================")

def ascending(mylist):
    mylist = sorted(mylist)
    print(mylist)

def descending(mylist):
    mylist = sorted(mylist, reverse = True)
    print(mylist)

print("Masukan tiga buah nilai")

nilaiA = int(input("Masukkan nilai A : "))
nilaiB = int(input("Masukkan nilai B : "))
nilaiC = int(input("Masukkan nilai B : "))
angka = [nilaiA, nilaiB, nilaiC]
garis()

#fungsi rata-rata
def rata_rata(angka):
    return sum(angka)/len(angka)
print("""Urutan hasil ascending : """
      ,(ascending))

print("""Urutan hasil descending : """
      ,(descending(angka)))

print("Angka Terbesar : ",max(angka))

print("Angka Terkecil : ",min(angka))

print("Rata - rata nilai : ",rata_rata(angkan ))

