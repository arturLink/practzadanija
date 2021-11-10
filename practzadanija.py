#p=0
#for i in range(15): #i=0,1,2,3...
#    A=0
#    while type(A)!=float:
#        try:
#            A=float(input("Sissesta"+str(i+1)+"arv"))
#        except ValueError:
#            print("Oi")
#    if A==round(A):
#        p+=1
#        print(str(A)+" On täisarv")
#    else:
#        print(str(A)+" Ei ole täisarv")
#print(str(p)+"Täisarvud")

    #task7

from random import *

#A=randint(10,100)
#B=randint(100,1000)
#print("A= "+str(A))
#print("B= "+str(B))
#K=int(input("K: "))
#for i in range(A,B+1):
#    if i%K==0: print(i)

    #task6 nf
#N=randint(1,10)
#for i in range(N):
#    Arv=int(input("Sissestage arv"))
#    if Arv=0:
#        p+=1
#    elif Arv=1:
#        n+=1
#print("whatever1")
#print("whatever2")
#print("whatever3")

    #task 2 nf
#A=input("Sissesta arv")
#while int(A)<=1:
#        try:
#            A=int(input("Sissesta"))
    #task 3
#korrutis=1
#for i in range(8):
#    A=float(input("Arv: "))
#    if A>0:
#        korrutis*=A
#print(korrutis)

    #task 9
#p=1.03
#S=int(input("Sissesta summa: "))
#N=int(input("Mitu aastat: "))
#for aasta in range(1,N+1):
#    S*=p
#    print(aasta,"aasta pärast tulemus on ",round(S,2))

    #task 13
#k=0
#summa=0
#for i in range(100,1001):
#    if i %7==0:
#        print(i)
#        k+=1
#        summa+=i
#print("summa",summa)
#print("kogus",k)

    #task 15
#for rjady in range(10):
#    for stroka in range(10):
#        print(stroka,end=" ")
#    print()

    #task 16
#for rjady in range(1,10):
#    for stroka in range(1,10):
#        if rjady==stroka:
#            print(stroka,end=" ")
#        else:        
#            print("0",end=" ")
#    print()

    #task 29
#for rjady in range(1,10):
#    for stroka in range(1,10):
#        if rjady==stroka:
#            print("x",end=" ")
#        elif stroka==1:
#            print("x",end=" ")
#        elif rjady==9:
#            print("x",end=" ")
#        else:        
#            print("0",end=" ")
#    print()

    #FOR practice
#loom=input("kupi slona! ")
#while loom.title()!="Slon":
#    loom=input("Vse govorjat "+loom+"! A ti kupi!")
#print("Molodets!")

    #Task 28
A
print("Guess the number between 1 and 10")
int(input("Number: "))