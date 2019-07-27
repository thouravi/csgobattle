import random

players = {
#Team Liquid
1 : {"name":"Stewie2k","rating": "105"},
2 : {"name":"twistzz","rating": "114"},
3 : {"name":"nitr0","rating": "102"},
4 : {"name":"NAF","rating": "109"},
5 : {"name":"EliGE","rating": "108"},
#Vitality
6 : {"name":"NBK-","rating": "104"},
7 : {"name":"RpK","rating": "098"},
8 : {"name":"apEX","rating": "105"},
9 : {"name":"ALEX","rating": "101"},
10 : {"name":"ZywOo","rating": "137"},
}

n = []

for j in players:
    n.append(j)

for i in players:
    if len(n) > 1:
        print("\n")
        print("Round ", i)
        a = random.choice(n)
        b = random.choice(n)
        if a != b:
            if players[a]['rating'] > players[b]['rating']:
                print(players[a]['name'],"wins against",players[b]['name'],"in a 1v1 with", int(players[a]['rating'])-int(players[b]['rating']), "HP.")
                n.remove(b)
            else:
                print(players[b]['name'],"wins against",players[a]['name'],"in a 1v1 with", int(players[b]['rating'])-int(players[a]['rating']), "HP.")
                n.remove(a)
        else:
            a = random.choice(n)
            b = random.choice(n)
            if a != b:
                if players[a]['rating'] > players[b]['rating']:
                    print(players[a]['name'],"wins against",players[b]['name'],"in a 1v1 with", int(players[a]['rating'])-int(players[b]['rating']), "HP.")
                    n.remove(b)
                else:
                    print(players[b]['name'],"wins against",players[a]['name'],"in a 1v1 with", int(players[b]['rating'])-int(players[a]['rating']), "HP.")
                    n.remove(a)
    else:
        print("\n")
        for s in n:
            print("Winner of the battle is:", players[s]['name'])
    
