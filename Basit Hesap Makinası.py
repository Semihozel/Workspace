print("""BASİT HESAP MAKİNESİ""")

print("1.TOPLAMA\n2.ÇIKARMA\n3.ÇARPMA\n4.BÖLME")

a = int(input("1.sayıyı giriniz"))
b = int(input("2.sayıyı giriniz"))

islem = input("Yapacağınız işlemi seçiniz")

if   (islem == "1" ):
      print("{} ile {}nin toplamı = {}".format(a,b,a+b))
elif (islem == "2" ):
      print("{} ile {}nin farkı = {}".format(a, b, a - b))
elif (islem == "3" ):
      print("{} ile {}nin çarpımı = {}".format(a, b, a * b))
elif (islem == "4"):
      print("{} nın {} e bölümü = {}".format(a, b, a / b))
else:
      print("Lütfen geçerli bir işlem girinzi")