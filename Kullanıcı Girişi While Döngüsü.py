print("KULANICI GİRİŞİ")

savename = "Semih"

savepassword = "12345"

turn = 3

while True:

    name = input("Kullanıcı adını girirniz : ")
    password = (input("Parolanızı girirniz : "))

    if (savename == name and savepassword != password):
        print("Parolanız yanlış tekrar deneyin....")
        turn -= 1
        print("Giriş hakkın",turn)

    elif (savename != name and savepassword == password):
        print("Kullanıcı adı yanlış tekrar deneyin....")
        turn -= 1
        print("Giriş hakkın", turn)

    elif (savename != name and savepassword != password):
        print("Kullanıcı adı ve parolanız yanlış tekrar deneyin....")
        turn -= 1
        print("Giriş hakkın", turn)

    else:
        print("Giriş yapılıyor")
        break

    if(turn == 0):
        print("Giriş hakkınız bitti")
        break

