#bakiye sorgulama
#para yatirma
#para cekme

cc = "4609 5800 1055 0638"

bakiye = 1000

print("************************************")
print("                                    ")
print("         Bankaya Hosgeldiniz        ")
print("                                    ")
print("************************************")


ccsor = input("Lutfen Kart Numaranizi Giriniz")

if ccsor == cc:
    while True:
        islem = input("Hangi Islemi Yapmak Istediginizi Seciniz (Cikmak icin 'q' ya basiniz) \n \n1-Bakiye Sorgulama \n \n2-Para Yatirma \n \n3-Para Cekme \n")
        if islem == "1":
            print(bakiye)
        elif islem == "2":
            print("Mevcut Paraniz",bakiye)
            yat = int(input("Yatirmak Istediginiz Tutari Giriniz: \n \n"))
            bakiye += yat
            print("Mevcut Paraniz \n \n",bakiye)
        elif islem == "3":
          print("Mevcut Bakiyeniz {} \n \n".format(bakiye))
          cek = int(input("Cekmek Istediginiz Tutari Giriniz: \n"))
          if cek > bakiye:
            print("Yetersiz Bakiye \n")
            print("Cekmek Istediginiz Tutar Karttakinden Fazla Olamaz \n")
            print("Hesabinizda Su Anda Bulunan Bakiye {} \n".format(bakiye))
            continue
          else:
            bakiye -= cek
            print("Mevcut Kalan Bakiyeniz {}".format(bakiye))
        elif islem == "q":
          print("Cikis Yapiliyor...")
          break