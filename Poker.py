import random
from collections import Counter
from Decorators import zeitmessung

@zeitmessung
def main():
        
    karten = []
    kartenAnzahl = 52

    @zeitmessung
    def kartenziehung():
        for i in range(kartenAnzahl):
            karten.append(i)
            return karten
        
    karten = kartenziehung()

    anzZiehungen = 5
    zeihungen = 100000
        


    def zahl_ermitteln(karten):
        mWerte = []
        for i in range(0, 5):
            mWerte.append(karten[i] % 13)
        mWerte.sort()
        count = Counter(mWerte)
        return count

    def paar(karten):
        count = zahl_ermitteln(karten)
        if count.most_common()[0][1] == 2:
            dict['paar'] += 1
            return True
        return False



    def drilling(karten):
        count = zahl_ermitteln(karten)
        if count.most_common()[0][1] == 3:
            dict['drilling'] += 1
            return True
        return False



    def vierling(karten):
        mWerte = []
        for i in range(1, 6):
            mWerte.append(karten[i - 1] % 13)
        mWerte.sort()
        count = Counter(mWerte)

        if count.most_common()[0][1] == 4:
            dict['vierling'] += 1
            return True
        return False



    def zwei_paare(karten):
        count = zahl_ermitteln(karten)
        if count.most_common()[0][1] == 2 and count.most_common()[1][1] == 2:
            dict['zwei_paare'] += 1
            return True
        
        return False



    def flush(karten):
        for i in range(1, 5):
            if karten[i - 1] // 13 != karten[i] // 13:
                return False

        dict['flush'] += 1
        return True



    def straight(karten):
        mWerte = []
        for i in range(0, 5):
            mWerte.append(karten[i] % 13)
        mWerte.sort()

        for i in range(1, 5):
            if mWerte[i - 1] + 1 != mWerte[i]:
                return False
        dict['straight'] += 1
        return True



    def straight_flush(karten):
        karten.sort()
        for i in range(1, 5):
            if karten[i - 1] // 13 != karten[i] // 13 or karten[i - 1] + 1 != karten[i]:
                return False

        dict['straight_flush'] += 1
        return True



    def royal_flush(karten):
        karten.sort()
        verglWert = [0, 9, 10, 11, 12]
        
        for i in range(1, 5):
            if karten[i - 1] // 13 != karten[i] // 13 or karten[i - 1] % 13 != verglWert[i - 1]:
                return False

        dict['royal_flush'] += 1
        return True



    def full_house(karten):
        count = zahl_ermitteln(karten)

        if count.most_common()[0][1] == 3 and count.most_common()[1][1] == 2:
            dict['full_house'] += 1
            return True
        
        return False



    def high_card():
        #dict['high_card'] +=1
        return False    
        
        
        
        
    dict = {'royal_flush': 0,'straight_flush': 0,'vierling': 0,'full_house': 0,'flush': 0,
                            'straight': 0,'drilling': 0,'zwei_paare': 0,'paar': 0,'high_card': 0}
        
        
    for i in range(zeihungen):
        hand = random.sample(range(0, kartenAnzahl), 5)
        #karten = kartenziehung()
        #random.shuffle(karten)
        #hand = karten[:5]
        """
        if paar(hand):
            dict['paar'] += 1
        if zwei_paare(hand):
            dict['zwei_paare'] += 1
            dict['paar'] -= 1
        if drilling(hand):
            dict['drilling'] += 1
        if full_house(hand):
            dict['full_house'] += 1
            dict['drilling'] += 1
            dict['paar'] += 1
        if straight(hand):
            dict['straight'] += 1
        if flush(hand):
            dict['flush'] += 1
        if straight_flush(hand):
            dict['straight_flush'] += 1
        if vierling(hand):
            dict['vierling'] += 1
        if royal_flush(hand):
            dict['royal_flush'] += 1
            """
        if royal_flush(hand) != True:
         if straight_flush(hand) != True:
          if vierling(hand) != True:
           if full_house(hand) != True:
            if flush(hand) != True:
             if straight(hand) != True:
              if drilling(hand) != True:
               if zwei_paare(hand) != True:
                if paar(hand) != True:
                 high_card()
                
    dict['high_card'] = 100000 - sum(dict.values())
    print(sum(dict.values()))

    for i in dict:
        dict[i] = (dict[i]*100)/100000


    #Wikipedia Werte:
    #0.000154, 0.00139, 0.02401, 0.1441, 0.1965, 0.3925, 2.1128, 4.7539, 42.2569, 50.1177


    for i in dict:
        print(f"{dict[i]} : {i}")
        
        
        
        
        
if __name__ == "__main__":
    main()