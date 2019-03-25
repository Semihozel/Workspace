print(".....Geometrik Şekil Bulma.....")

islem = input("Dörtgen mi Üçgen mi ? :")

if (islem == "Dörtgen" or islem == "dörtgen"):
    print("Lütfen kenarları sırayla giriniz")

    a = int(input("1.kenar"))
    b = int(input("2.kenar"))
    c = int(input("3.kenar"))
    d = int(input("4.kenar"))

    if (a == b and a == c and a==d):
        print("bu bir karedir")

    elif (a == c and b == d):
        print("bu bir dikdörtgendir")

    else:
        print("bu bir dörtgendir")

elif (islem == "Üçgen" or islem == "üçgen"):
    print("Lütfen kenarları sırayla giriniz")

    a = int(input("1.kenar"))
    b = int(input("2.kenar"))
    c = int(input("3.kenar"))

    if ( abs(a+b)>c and abs(a+c>b and abs(b+c)>a)):

        if (a == b and a == c):
            print("bu bir eşkenar üçgendir")

        elif ((a==b and a!=c) or (b==c and b!=a) or (a==c and a!=b)):
            print("bu bir ikizkenar üçgendir")

        else:
            print("bu bir çeşitkenar üçgendir")

    else:
        print("üçgen belirtmiyor")
else:
    print("geçersiz işlem")


