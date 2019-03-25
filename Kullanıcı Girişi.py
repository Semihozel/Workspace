print("********\n KULLANICI GİRİŞİ\n********")

kayıtlıad = "Semih"

kayıtlıparola = "12345"

kullanıcı_adı = input("Kullanıcı adını giriniz  ")

parola = input("Parolayı giriniz  ")

if (kullanıcı_adı == kayıtlıad and kayıtlıparola != parola):
    print("Parola yanlış")
elif (kullanıcı_adı != kayıtlıad and kayıtlıparola == parola):
    print("Kullanıcı adı yanlış ")
elif (kullanıcı_adı != kayıtlıad and kayıtlıparola != parola):
    print("Kullanıcı adı ve Parola hatalı giriş")
else:
    ("HOŞGELDİNİZ")