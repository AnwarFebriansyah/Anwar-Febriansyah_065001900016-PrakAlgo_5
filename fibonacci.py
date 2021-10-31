print("---DERET FIBONACCI---")
n = int(input("Masukan jumlah bilangan: "))
a = int(input("Masukan bilangan pertama: "))
b = int(input("Masukan bilangan kedua: "))
n-=2
print(a)
print(b)
while n>0:
    temp=a+b
    a=b
    b=temp
    print(b)
    n-=1
