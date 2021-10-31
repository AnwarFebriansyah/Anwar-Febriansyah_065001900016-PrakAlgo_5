print("---HITUNG GAJI HARIAN---")
jammasuk = input("Jam Masuk Kerja: ")
if 1<=int(jammasuk.split('.')[0])<=10:
    print("Selamat Pagi")
elif 11<=int(jammasuk.split('.')[0])<=14:
    print("Selamat Siang")
elif 15<=int(jammasuk.split('.')[0])<=18:
    print("Selamat Sore")
elif (19<=int(jammasuk.split('.')[0])<=24) or (int(jammasuk.split('.')[0])==0):
    print("Selamat Malam")
jamkeluar = input("Jam Keluar Kerja: ")
if 1<=int(jamkeluar.split('.')[0])<=10:
    print("Selamat Pagi")
elif 11<=int(jamkeluar.split('.')[0])<=14:
    print("Selamat Siang")
elif 15<=int(jamkeluar.split('.')[0])<=18:
    print("Selamat Sore")
elif (19<=int(jamkeluar.split('.')[0])<=24) or (int(jamkeluar.split('.')[0])==0):
    print("Selamat Malam")
print("---rincian gaji---")
waktukerja = int(jamkeluar.split('.')[0])-int(jammasuk.split('.')[0])
if int(jamkeluar.split('.')[0])-int(jammasuk.split('.')[0])<0:
    waktukerja-=1
print("Waktu Kerja\t: "+str(waktukerja)+" jam ( "+jammasuk+" sd "+jamkeluar+" )")
print("Gaji perhari\t: Rp 175.000")
waktukerja-=8
if waktukerja<0:
    waktukerja=0
lembur = waktukerja*15000
print("Lembur\t\t: Rp "+'{:,}'.format(lembur).replace(',', '.')+" ( "+str(waktukerja)+" jam x @ Rp 15.000)")
print("Total Gaji\t: Rp "+'{:,}'.format((lembur+175000)).replace(',', '.'))
