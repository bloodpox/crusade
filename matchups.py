
import random

defenders = ['D-Braden','D-Kyle','D-Kyler','D-Stephen']
invaders = ['I-Jacob','I-Steven','I-Keller','I-Brock']
raiders = ['R-Tyler','R-Noah','R-Aidan','R-Bruce']

league = [defenders, raiders, invaders]

week1=[]
week2=[]
week3=[]
week4=[]
week5=[]
week6=[]
week7=[]
week8=[]

f = open('week1.txt','r')
for x in f.readlines():
    week1.append(x, end='')
f.close()

matches = []

while len(matches) < 6:
    faction1 = random.choice(league)
    league.remove(faction1)
    faction2 = random.choice(league)
    league.remove(faction2)
    faction3 = random.choice(league)
    league.remove(faction3)
    


    if faction1:
        i=0
        while i < 2:
            team1 = random.choice(faction1)
            team2 = random.choice(faction2)
            matches.append(team1+' v. '+team2)
            faction1.remove(team1)
            faction2.remove(team2)
            i=i+1

    if faction2:
        i=0
        while i < 2:
            team1 = random.choice(faction2)
            team2 = random.choice(faction3)
            matches.append(team1+' v. '+team2)
            faction2.remove(team1)
            faction3.remove(team2)
            i=i+1

    if faction3:
        i=0
        while i < 2:
            team3 = random.choice(faction3)
            team4 = random.choice(faction1)
            matches.append(team3+' v. '+team4)
            faction1.remove(team4)
            faction3.remove(team3)
            i=i+1

print(matches)
input()
weekly_matches = open("THIS WEEK.txt", "w")
for match in matches:
    weekly_matches.write(match+"\n")
weekly_matches.close()
    

        
