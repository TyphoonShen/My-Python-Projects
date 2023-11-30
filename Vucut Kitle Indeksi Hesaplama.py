boy = float(input("Lutfen Boyunuzu Metre Cinsinden Giriniz: "))
kilo = int(input("Lutfen Kilonuzu Giriniz: "))

bmi = kilo/(boy*boy)

if bmi <= 18.5:
    print("bmi = ",bmi,"Zayif")
elif 18.5 < bmi < 24.9: #ikinci yol  bmi > 18.5 and bmi <24.9
    print("bmi = ",bmi,"Normal")
elif 25 < bmi <29.9:
    print("bmi = ",bmi,"Kilolu")
elif 30 < bmi < 34.9:
    print("bmi = ",bmi,"Sisman(Obezite sinifi 1)")
elif 35 < bmi < 39.9:
    print("bmi = ",bmi,"Asiri Sisman(Obezite sinifi 2)")
elif bmi > 40:
    print("bmi = ",bmi,"Asiri asiri sisman(Obezite sinifi 3")