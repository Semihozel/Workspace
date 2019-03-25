print("DENKLEM KÖKÜ BULMA")

print("Denklem = ax^2+bx+c")

print("Lütfen kökünü bulmak istediğiniz denklemin değerlerini giriniz.")

a = int(input("a:"))
b = int(input("b:"))
c = int(input("C:"))

delta = b**2 - 4*a*c

x1 = (-b + (delta**0.5))/(2*a)
x2 = (-b - (delta**0.5))/(2*a)

print(" Birinci kök:{}\n İkinci kök:{}".format(x1,x2))

