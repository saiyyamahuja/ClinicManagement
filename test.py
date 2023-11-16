l=input("List: ")
l=l.split(",")
l=list(map(int,l))
n=int(input(""))
a=True
b=list()

for i in range(len(l)):
    if l[i]==n:
        b.append(n)

for i in b:
    l.remove(i)
print(l)