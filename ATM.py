print("...SEM BANKA HOŞGELDİNİZ...")

print("1.BAKİYE SORGULAMA\n"
      "2.PARA YATIRMA\n"
      "3.PARA ÇEKME\n"
      ""
      "   (çıkmak için q tuşuna basınız)   ")

bakiye = 1000
while True:

    islem = (input("Yapmak istediğiniz işlem nedir: "))

    if (islem == "q"):
        print("Çıkış yapılıyor.....")
        break

    elif (islem == "1"):
        print("Bakiyeniz {} TL dir".format(bakiye))

    elif (islem == "2"):

        miktar = int(input("Yatırmak istediğiniz tutar: "))

        bakiye += miktar

        print("Bakiyeniz {} TL dir".format(bakiye))

    elif (islem == "3"):

        miktar = int(input("Çekmek istediğiniz tutar: "))

        if (miktar > bakiye):

            print("Paran yok")
            print("Bakiyeniz {} TL dir".format(bakiye))
            continue

        bakiye -= miktar
        print("Bakiyeniz {} TL dir".format(bakiye))

    else:

        print("Lütfen geçerli bir işlem girirniz")
        





