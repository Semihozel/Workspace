print("SAYISAL ANALİZ DERS NOTU HESAPLAMA")

vize = int(input("Vize notunu giriniz: "))
quiz1 = int(input("1.Kısa sınav notunuz: "))
quiz2 = int(input("2.Kısa sınav notunuz:"))
quiz3 = int(input("3.Kısa sınav notunuz:"))
final = int(input("Final notunu giriniz"))

ortalama = (vize * 38.5/100) + (quiz1 * 5/100) + (quiz2 * 5/100) + (quiz3 * 5/100) + (final*45/100)

print("notunuz :",ortalama)

if (ortalama < 50 ):
    print("Notunuz : FF KALDINIZ")
elif (ortalama < 55 ):
    print("Notunuz : DD")
elif (ortalama < 60):
    print("Notunuz : DC")
elif (ortalama < 65):
    print("Notunuz : CC")
elif (ortalama < 70):
    print("Notunuz : CB")
elif (ortalama < 80):
    print("Notunuz : BB")
elif (ortalama < 85):
    print("Notunuz : BA")
else:
    print("Notunuz : AA")