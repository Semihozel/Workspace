print("Öğrenci Kaydetme Programı")

ad = input("Öğrenci adını giriniz")
soyad = input("Öğrenci soyadını giriniz")
no = input("Öğrencinin numarasını giriniz")
bolum = input("Okuduğu bölümü giriniz")

bılgıler = [ad,soyad,no,bolum]

print("Bilgiler kaydediliyor...")

print("Öğrencinin adı:{}\nÖğrencinin soyadı:{}\nÖğrenci no:{}\nOkuduğu bölüm:{}".format(bılgıler[0],bılgıler[1],bılgıler[2],bılgıler[3]))

print("Öğrenci kaydı tamamlandı...")