#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

face = []
color = ["Red", "Green", "Blue", "Yellow"]
sp_card = ["Skip", "Draw2", "Draw4","Reverse"]
deck = []

for i in range(0,13):
    face.append(str(i))


for j in range(4):
    face.append(sp_card[j])

for k in range(4):
    for l in range(13):
        card = (face[l] + "\t " + color[k])
        deck.append(card)

random.shuffle(deck)

for m in range(52):
    print(f' Card:{deck[m]}')
class WildCard:
    def __init__(self):
        self.is_draw_4 = False        
    def __str__(self):
        if self.is_draw_4 == False:
            return "Wild"
        else:
            return "Wild draw 4"
    __repr__ = __str__

class SkipCard:
    def __init__(self,c):
        self.color = c
    def __str__(self):
        return self.color + "Skip"
    __repr__ = __str__
class ReversCard:
    def __init__(self,card):
        self.color = c
    def __str__(self):
        return self.color + "Reverse"
    
for i in range(4):
    card = WildCard()
    deck.append(card)


