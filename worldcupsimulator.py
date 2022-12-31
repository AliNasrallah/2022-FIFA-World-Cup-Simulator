import random

#FORMAT: [WCs, FIFA ranking, defense, attack]

groups = {'A':{'Qatar':[0,60,55,59], 'Ecuador':[0,41,65,65], 'Senegal':[0,19,77,82], 'Netherlands':[0,6,91,88]},
    'B':{'England':[1,5,87, 92],'IR Iran':[0,24,70,70], 'USA':[0,13,75,75], 'Wales':[0,28,70,76]},
    'C':{'Argentina':[1,2,87,90] , 'Saudi Arabia':[0,49,70,70], 'Mexico':[0,15,78,79], 'Poland':[0,22,67,78]},
    'D':{'France':[2,3,88,95], 'Australia':[0,27,64,68] , 'Denmark':[0,18,74,83], 'Tunisia':[0,30,68,70]},
    'E':{'Spain':[1,10,87,89], 'Costa Rica':[0,32,67,69], 'Germany':[4,14,87,87], 'Japan':[0,20,74,72]},
    'F':{'Belgium': [0,4,87,89], 'Canada':[0,53,65,70], 'Morocco':[0,11,80,85], 'Croatia':[0,7,87,86]},
    'G':{'Brazil':[5,1,90,96], 'Serbia':[0,29,75,79], 'Switzerland':[0,12,76,83], 'Cameroon':[0,33,65,70]},
    'H':{'Portugal':[0,9,90,89], 'Ghana':[0,58,70,65], 'Uruguay':[2,16,84,85], 'Korea Republic':[0,25,76,76]}
          }

print('==========================================================================================================\n========================================WORLD CUP 2022 GROUP STAGE========================================\n==========================================================================================================')

class PlayGame:

    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        #FORMAT: ([team1, goals], [team2, goals])
        self.matchfacts = ([team1[0], 0], [team2[0], 0])

    def __str__(self):
        posession_both = self.getposession()
        goals_both = self.getscore()
        return f'{self.team1[0]} VS {self.team2[0]}\n{self.team1[0]}: {goals_both[0]}    {self.team2[0]}: {goals_both[1]}\nPOSESSION:\n{self.team1[0]}: {posession_both[0]}%   {self.team2[0]}: {posession_both[1]}%\n\n'

    def getposession(self):

        quality1 = self.team1[1][2]+self.team1[1][3]-self.team1[1][1]
        quality2 = self.team2[1][2]+self.team2[1][3]-self.team2[1][1]
        if self.team1[1][0]>0:
            quality1+=10
        if self.team2[1][0]>0:
            quality2+=10

        if quality1<quality2 and random.randint(0,100) < 10:
            quality1+=20

        if quality2<quality1 and random.randint(0,100) < 10:
            quality2+=20

        random1 = random.randint((quality1/2)//1, quality1)
        random2 = random.randint((quality2/2)//1, quality2)

        posession1 = ((random1/(random1+random2))*100)//1
        posession2= 100-posession1

        if posession1-posession2 > 30:
            posession2+=10
            posession1-=10
        elif posession2-posession1 >30:
            posession1+=10
            posession2-=10
     
        return (posession1, posession2)

    def getscore(self):
        goals1 = 0
        goals2 = 0
        quality1 = (self.team1[1][3]-(self.team2[1][2])/4)*(self.getposession()[0]/100)
        quality2 = (self.team2[1][3]-(self.team1[1][2])/4)*(self.getposession()[1]/100)

        if self.team1[1][0]>0:
            quality1+=30
        if self.team2[1][0]>0:
            quality2+=30
        if self.team1[1][1]<11:
            quality1+=10
        if self.team2[1][1]<11:
            quality2+=10

        for i in range(45):
            bound1 = 1500
            bound2 = 1500
            random1 = random.randint(0,bound1)
            random2 = random.randint(0,bound2)
            if random1<quality1:
                goals1 +=1
                bound1 +=10000
                self.matchfacts[0][1]+=1
            if random2<quality2:
                goals2 +=1
                bound2 +=10000
                self.matchfacts[1][1]+=1
        return (goals1, goals2)
    def getwinner(self):
        if self.matchfacts[0][1]>self.matchfacts[1][1]:
            winner = self.matchfacts[0][0]
        elif self.matchfacts[1][1]> self.matchfacts[0][1]:
            winner = self.matchfacts[1][0]
        return winner

        

def getlargest(teamlist, standings):
    largest = teamlist[0]
    for i in teamlist:
        if standings[i][7] > standings[largest][7]:
            largest = i
        elif standings[i][7] == standings[largest][7]:
             if standings[i][6] > standings[largest][6]:
                largest = i
             elif standings[i][6] == standings[largest][6]:
                if standings[i][4] > standings[largest][4]:
                    largest = i
    return largest

def playpenalties(battle):
    
    result1 = []
    result2 = []
    rounds = 1
    rounds1 =0
    rounds2 = 0
    scored1 = 0
    scored2 = 0
    while rounds <=5:
        if scored1 + (5-rounds1) < scored2 or scored2 + (5-rounds2) < scored1:
            break
        elif random.random() < 0.5:
             result1.append('x')
             rounds1 +=1
        else:
             result1.append('O')
             scored1 +=1
             rounds1 +=1
        
            
       
        if scored2 + (5-rounds2) < scored1 or scored1 + (5-rounds1) < scored2:
            break     
        elif random.random() < 0.5:
            result2.append('x')
            rounds2 +=1
        else:
            result2.append('O')
            scored2 +=1
            rounds2 +=1
        rounds +=1
        
        
    if scored1>scored2:

        statement = f'{battle[0][0]} WINS ON PENALTIES'
        winner = battle[0][0]

    elif scored2>scored1:

        statement = f'{battle[1][0]} WINS ON PENALTIES'
        winner = battle[1][0]

    else:
        while scored1 == scored2:
            if random.random() < 0.5:
                result1.append('x')
                
            else:
                result1.append('O')
                scored1 +=1
                
            if random.random() < 0.5:
                result2.append('x')
                
            else:
                result2.append('O')
                scored2 +=1
                
        if scored1>scored2:

            statement = f'{battle[0][0]} WINS ON PENALTIES'
            winner = battle[0][0]

        elif scored2>scored1:
            winner = battle[1][0]

            statement = f'{battle[1][0]} WINS ON PENALTIES'

    return (' '.join(result1) + '\t  ' + ' '.join(result2) + '\n' + statement.upper() + '\n\n\n', winner)

def playknockout(battle):
    game = PlayGame(battle[0], battle[1])
    print(game)
    if game.matchfacts[0][1] == game.matchfacts[1][1]:
        penalties = playpenalties(battle)
        print(penalties[0]+'\n___________________________________________________')
        winner = penalties[1]

    else:
        winner = game.getwinner()

        
        print('\n___________________________________________________')

    return winner
    

round1 = []
round2 = []
round3 = []
round4 = []
round5 = []
round6 = []
round7 = []
round8 = []

for group in groups.values():
    groupteams = []
    for groupletter in groups.keys():
        if groups[groupletter] == group:
            groupname = groupletter
    for team in group.items():
        groupteams.append(team)
    team1 = groupteams[0]
    team2 = groupteams[1]
    team3 = groupteams[2]
    team4 = groupteams[3]
    game1 = PlayGame(team1, team2)
    game2 = PlayGame(team1, team3)
    game3 = PlayGame(team1, team4)
    game4 = PlayGame(team2, team3)
    game5 = PlayGame(team2, team4)
    game6 = PlayGame(team3, team4)
    print(f'\n\n\n\n\n\n============================================GROUP {groupname}============================================')
    print(game1)
    print(game2)
    print(game3)
    print(game4)
    print(game5)
    print(game6)
    
    #FORMAT: [standing, wins, losses, draws, GF, GA, GD, PTS]
    standings = {team1[0]:[0, 0, 0, 0, 0, 0, 0, 0], team2[0]:[0, 0, 0, 0, 0, 0, 0, 0], team3[0]:[0, 0, 0, 0, 0, 0, 0, 0], team4[0]:[0, 0, 0, 0, 0, 0, 0, 0]}

    gamelist = [game1, game2, game3, game4, game5, game6]
    for nation in groupteams:
        for scoreboard in gamelist:
            if nation[0] in scoreboard.matchfacts[0]:
                standings[nation[0]][4]+= scoreboard.matchfacts[0][1]
                standings[nation[0]][5]+= scoreboard.matchfacts[1][1]
                if scoreboard.matchfacts[0][1]>scoreboard.matchfacts[1][1]:
                    standings[nation[0]][1]+=1
                    standings[nation[0]][7]+=3
                elif scoreboard.matchfacts[0][1]==scoreboard.matchfacts[1][1]:
                    standings[nation[0]][3]+=1
                    standings[nation[0]][7]+=1
                else:
                    standings[nation[0]][2]+=1
            elif nation[0] in scoreboard.matchfacts[1]:
                standings[nation[0]][4]+=scoreboard.matchfacts[1][1]
                standings[nation[0]][5]+=scoreboard.matchfacts[0][1]
                if scoreboard.matchfacts[1][1]>scoreboard.matchfacts[0][1]:
                    standings[nation[0]][1]+=1
                    standings[nation[0]][7]+=3
                elif scoreboard.matchfacts[1][1]==scoreboard.matchfacts[0][1]:
                    standings[nation[0]][3]+=1
                    standings[nation[0]][7]+=1
                else:
                    standings[nation[0]][2]+=1
        
        standings[nation[0]][6] = standings[nation[0]][4] - standings[nation[0]][5]


   
    
    
    teamlist = [team1[0],team2[0],team3[0],team4[0]]
    table = []
    first = getlargest(teamlist, standings)
    teamlist.pop(teamlist.index(first))
    second = getlargest(teamlist, standings)
    teamlist.pop(teamlist.index(second))
    third = getlargest(teamlist, standings)
    teamlist.pop(teamlist.index(third))
    fourth = teamlist[0]

    if groupname == 'A':
        round1.append((first, groups[groupname][first]))
        round5.append((second, groups[groupname][second]))
         
    elif groupname == 'B':
        round1.append((second, groups[groupname][second]))
        round5.append((first, groups[groupname][first]))

    elif groupname == 'C':
        round2.append((first, groups[groupname][first]))
        round6.append((second, groups[groupname][second]))
        
    elif groupname == 'D':
        round2.append((second, groups[groupname][second]))
        round6.append((first, groups[groupname][first]))
        
    elif groupname == 'E':
        round3.append((first, groups[groupname][first]))
        round7.append((second, groups[groupname][second]))
        
    elif groupname == 'F':
        round3.append((second, groups[groupname][second]))
        round7.append((first, groups[groupname][first]))

    elif groupname == 'G':
        round4.append((first, groups[groupname][first]))
        round8.append((second, groups[groupname][second]))
        
    else:
        round4.append((second, groups[groupname][second]))
        round8.append((first, groups[groupname][first]))
        

                
    print(f'GROUP {groupname} STANDINGS:\n\n1: {first}   W:{standings[first][1]}  L:{standings[first][2]}  D:{standings[first][3]}  GF:{standings[first][4]}  GA:{standings[first][5]}  GD:{standings[first][6]}  PTS:{standings[first][7]}  \n\n2: {second}   W:{standings[second][1]}  L:{standings[second][2]}  D:{standings[second][3]}  GF:{standings[second][4]}  GA:{standings[second][5]}  GD:{standings[second][6]}  PTS:{standings[second][7]} \n\n3: {third}   W:{standings[third][1]}  L:{standings[third][2]}  D:{standings[third][3]}  GF:{standings[third][4]}  GA:{standings[third][5]}  GD:{standings[third][6]}  PTS:{standings[third][7]} \n\n4: {fourth}   W:{standings[fourth][1]}  L:{standings[fourth][2]}  D:{standings[fourth][3]}  GF:{standings[fourth][4]}  GA:{standings[fourth][5]}  GD:{standings[fourth][6]}  PTS:{standings[fourth][7]} ')
    print('_______________________________________________________________________________________________________________')

print('\n\n\n=====================================================================================\n=====================================ROUND OF 16=====================================\n=====================================================================================\n\n')


round_16 = [round1, round2, round3, round4, round5, round6, round7, round8]
quarter1 = []
quarter2 = []
quarter3 = []
quarter4 = []


for battle in round_16:
    winner = playknockout(battle)
    for letter in groups.keys():
        if winner in groups[letter].keys():
            if battle == round1 or battle == round2:
                quarter1.append((winner, groups[letter][winner]))
            elif battle == round3 or battle == round4:
                quarter2.append((winner, groups[letter][winner]))
            elif battle == round5 or battle == round6:
                quarter3.append((winner, groups[letter][winner]))
            else:
                quarter4.append((winner, groups[letter][winner]))

print('\n\n\n=======================================================================================\n=====================================QUARTERFINALS=====================================\n=======================================================================================\n\n')

quarterfinals = [quarter1, quarter2, quarter3, quarter4]

semi1 = []
semi2 = []

final = []
for quarterfinal_match in quarterfinals:
    winner = playknockout(quarterfinal_match)
    for letter in groups.keys():
        if winner in groups[letter].keys(): 
            if quarterfinal_match == quarter1 or quarterfinal_match == quarter2:
                semi1.append((winner, groups[letter][winner]))
            else:
                semi2.append((winner, groups[letter][winner]))

semifinals = [semi1, semi2]
        
print('\n\n\n====================================================================================\n=====================================SEMIFINALS=====================================\n====================================================================================\n\n')


for semifinal_match in semifinals:
    winner = playknockout(semifinal_match)
    for letter in groups.keys():
        if winner in groups[letter].keys(): 
            final.append((winner, groups[letter][winner]))


print('\n\n\n===================================================================================\n=======================================FINAL=======================================\n===================================================================================\n\n')



winner = playknockout(final)


print(f'==========================================================================================\n========================{winner} has won the 2022 FIFA World Cup!========================\n==========================================================================================')










        
    




        

                
                
            
            
            

    
        

    




    


  
    
        
        




    
   
    

    
