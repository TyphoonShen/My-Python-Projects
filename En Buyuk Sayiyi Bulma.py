x=int(input("1. sayiyi giriniz"))
y=int(input("2. sayiyi giriniz"))
z=int(input("3. sayiyi giriniz"))

if x>=y and x>=z:
  print(x,"en buyuk sayi")
elif y>=x and y>=z:
  print(y,"en buyuk sayi")
elif z>=x and z>=y:
  print(z,"en buyuk sayi")