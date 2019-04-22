b = int(input("sayı :"))

for a in range(1, b + 1):

    toplam = 0

    for i in range(1, a):

        if (a % i == 0):
            toplam += i

    if (toplam == a):
        print("{} mükemmel sayıdır".format(a))





