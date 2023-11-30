# FAKTORIYEL BULMA

faktoriyel = 1

sayi = int(input("Lutfen Bir Sayi Giriniz"))

if sayi > 0:
    while True:
        faktoriyel *= sayi
        sayi -= 1
        if sayi == 1:
            print(faktoriyel)
elif sayi == 0:
    print("0 Sayisinin Faktoriyeli Her Zaman 1'dir")
elif sayi < 0:
    print("Eksi Sayilarin Faktoriyeli Olmaz")