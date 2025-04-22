
from collections import deque

def slv():
    
    while True:
        word = input()
        if word == 'end':
            break
        if(main_algo(word)):
            print("<" + word + "> is acceptable.")
        else:
            print("<" + word + "> is not acceptable.")
        

def main_algo(word):
    mo = ['a', 'e', 'i', 'o', 'u']
    bag_mo = deque()
    bag_ja = deque()
    count_mo = 0
    for i in word:
        if i in mo:
            count_mo += 1
            if bag_ja: bag_ja.clear()     
            bag_mo.append(i)
            if len(bag_mo) == 2 and bag_mo[0] == bag_mo[1] and bag_mo[0] != 'e' and bag_mo[0] != 'o':
                return False
        else:
            if bag_mo: bag_mo.clear()
            bag_ja.append(i)
            if len(bag_ja) == 2 and bag_ja[0] == bag_ja[1]:
                return False
        if len(bag_ja) >= 3 or len(bag_mo) >= 3:
            return False
    if count_mo > 0: 
        return True
    else:
        return False

if __name__ == "__main__":
    slv()