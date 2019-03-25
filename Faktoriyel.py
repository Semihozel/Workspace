print("......Faktoriyel Bulma Programı......")

print("çıkmak için q ya basınız")
print("Faktoriyelini bulmak istediğiniz sayıyı giriniz")
while True:

    sayı = input("Sayı: ")

    if ( sayı == "q"):
        print("Çıkış yapılıyor.....")
        break


    sayı = int(sayı)

    faktoriyel = 1

    for i in range(1,sayı+1):

        faktoriyel *= i

    print(faktoriyel)




