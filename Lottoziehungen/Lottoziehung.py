import random


def zahlZiehen(aufrufe):
    
    list = []
    
    for i in range(45):
        list.append(i)
        
    count = 0
    max = len(list) -1
    for i in range(aufrufe):
        
        index = random.randrange(len(list)-count)
        print(list[index])
        zahl = list[index]
        list[index] = list[max]
        list[max] = zahl
        
        count = count + 1
    
zahlZiehen(45)
