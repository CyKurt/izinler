k=input("Kullanızı izinleri: ")
g=input("Grup izinleri: ")
d=input("Diğerlerinin izinleri: ")
a1=0
a2=0
a3=0
def izinler(a1,a2,a3):
    for x in k:
        if x=="r":
            a1+=4
        if x=="w":
            a1+=2
        if x=="x":
            a1+=1
    for x in g:
        if x=="r":
            a2+=4
        if x=="w":
            a2+=2
        if x=="x":
            a2+=1
    for x in d:
        if x=="r":
            a3+=4
        if x=="w":
            a3+=2
        if x=="x":
            a3+=1
    print(a1,a2,a3)

izinler(a1,a2,a3)