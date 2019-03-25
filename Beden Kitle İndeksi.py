print("BEDEN KİTLE İNDEKSİ HESAPLAMA")

boy = float(input("boyunuzu giriniz (m)"))
kilo = float(input("kilonuzu giriniz (kg)"))

bki = kilo/(boy*boy)

print("Besin Kitle İndeksiniz = {}".format(bki))

if (bki<18.5):
    print("Zayıfsınız")

elif (18.5<bki<25):
    print("normalsiniz")

elif (25<bki<30):
    print("Fazla kilolusunuz")

elif (bki>30):
    print("Obezsiniz dikkat etmelisiniz")
