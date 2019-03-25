print("MÜKEMMEL SAYI BULMA")

a = int(input("sayı : "))

toplam = 0

for i in range(1, a):

    if (a % i == 0):
        print("{} nın bölenleri".format(i))

        toplam += i

print("bölenlerin toplamı", toplam)

if (toplam == a):
    print("{} mükemmel bir sayıdır".format(a))



else:
    print("mükemmel sayı değildir")


