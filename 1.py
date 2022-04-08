import pandas as pd

amountc=[]
amountid=[]
import random
import csv
import numpy as np
RESULT=[]
tabl=[]
z="ку"
PRICE=0
summ=0
summa=0
newdata=[]
def Enter(sp,z):
    print("Введите кол-во стратегий ",z)
    amount=int(input())
    for i in range(0,amount):
        print("Введите название", i+1 ,"стратегии ",z)
        c=input()
        sp.append(c)
    return sp
def Dataform(amountColoums,amountID,):
    data=[]
    for i in range(len(amountColoums)):
        rdata=[]
        for j in range(len(amountID)):
            print("Введите"" элемент строки",i+1,"столбца",j+1)
            f=int(input())
            rdata.append(f)
        data.append(rdata)
    return data
def randEnter(sp,z):

    amount=random.randint(2,3)
    for i in range(0,amount):
        sp.append("вариант")
    return sp

def randomDataform(amountColoums,amountID,):
    data=[]
    for i in range(len(amountColoums)):
        rdata=[]
        for j in range(len(amountID)):
            f=random.randint(1,100)
            rdata.append(f)
        data.append(rdata)
    return data
def csvDAta (filename):
    headers = []
    data=[]
    with open(filename,encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
        return(data)
data=0
col=0
id=0
from func import Enter,Dataform,randomDataform,csvDAta

a1="учителя"
a2="учиника"

variant =int(input("введите 1 для ввода с клавиатуры\n введите 2 для генерации  "))
if variant == 1:
        col=Enter(amountc,a1)
        id=Enter(amountid,a2)
        students=[]
        data=Dataform(col,id)

elif variant ==2:
        col = Enter(amountc, a1)
        id = Enter(amountid, a2)
        data=randomDataform(col,id)
#print(prisoners_dilemma)
#print(equilibria)
frame = pd.DataFrame(data=data, columns=col, index=id)
df=frame
df1=frame
variant_prepoda=(df1.min(axis=1))#*100/3)
variant_studenta=(df.max())#*100/4)
variant_prepoda1=variant_prepoda.max()
variant_studenta1=variant_studenta.min()
var_p=str(variant_prepoda.loc[variant_prepoda == variant_prepoda1].index)
var_s=str(variant_studenta.loc[variant_studenta == variant_studenta1].index)
var_prep=var_p.split("'")[1]
var_stud=var_s.split("'")[1]
print(frame)

print("Лучший выбор для," ,a1,"- (стратегия)",var_stud)
print("при выборе этого вырианта шанс сдачи студентом:",variant_prepoda1,"цена игры(вес)")
print("Лучший выбор дял студента -  (стратегия)",var_prep)
print("при выборе этого вырианта шанс сдачи студентом:",variant_studenta1," цена игры(вес)")
if variant_prepoda1 == variant_studenta1:
        print("цена игры = ",variant_studenta1)
else:
        print("цена игры находится в промежутке ", variant_prepoda1,"<= y <= ",variant_studenta1)
        for i in range(len(col)):
            c = data[i]
            k= c[i]
            newdata.append(k)
        result=np.linalg.solve(data, newdata)
        for i in range(len(col)):
            c = data[i]
            for h in  c:
                summ=summ+h
                itog=summ*result[i]
            RESULT.append(itog)

        for i in range(len(RESULT)):
            if RESULT[i] < 0:
                RESULT[i]=0
            else:
                summa=summa+RESULT[i]

        for i in range(len(result)):

            if RESULT[i] != 0:
                m=RESULT[i]/summa*100
                tabl.append(m)
            else:
                tabl.append(RESULT[i])
        case=data[0]



        print(" вероятность выбора смешанных решений ученика",tabl)






        print(" вероятность выбора смешанных решений ученика",tabl)
