import random
import sys
import matplotlib.pyplot as pyplt


liste = []
for i in range(45):
    liste.append(i)
    
def lotto(aufrufe, liste):
    max = 44 - aufrufe
    index = random.randint(0, max)
        
    zufallszahl = liste[index]
    liste[index] = liste[max]
    liste[max] = zufallszahl
    
    #python tauschzeile einarbeiten
    
    return zufallszahl

dict2 = {"Zahl":"Gezählte Anzahl der Zahl die zahlt"}

def dict_innit():
    for i in range(45):
        dict2[i] = 0

dict_innit()
print(dict2)


for i in range(1000000):
    for i in range(8):
        zufallszahl = lotto(i, liste)
        dict2[zufallszahl] = dict2[zufallszahl] + 1

print(dict2)


#Balkendiagramm
positionen = []
hoehe = []
for i in range(45):
    hoehe.append(dict2[i])
    positionen.append(i+1)
    
pyplt.bar(positionen, hoehe, align = "center")
pyplt.title("Lotto-Statistik")
pyplt.show()


