import msvcrt
import random

steps = 20
way = 0

food = "*"
food_energy = random.randint(15, 20)

spike = "X"
spike_damage = 3

def display(level, x, y):
    part1 = level[:y]
    part2 = level[y]
    part3 = level[y+1:]
    for str in part1:
        print(str)
    print(part2[:x] + "@" + part2[x+1:])
    for str in part3:
        print(str)
       

level1 = ["█████████████████████████",
          "█       █       █       █",
          "█ ████ ████ ███ ███ ███ █",
          "█             █       █ █",
          "███ ███ █ ███ █ █ █████ █",
          "█     ███   █   █       █",
          "███ █ █   █ ███ █ █ ███ █",
          "█   █   █ █     █ █     █",
          "█ ███ █ █    ██   ███ ███",
          "█   █ █ ███     █       █",
          "███   █   ██ ████ █ ███ █",
          "█   █   █         █     █",
          "█████████████████████████",]


def add_food(level, x, y, food):
    max_x = len(level[0])-1
    max_y = len(level)-1
    a = True
    while a:
        food_x = random.randint(1, max_x)
        food_y = random.randint(1, max_y)
        if level[food_y][food_x] == " ":
            if food_x != x and food_y != y:
                level[food_y] = level[food_y][:food_x] + food + level[food_y][food_x+1:]
                a = False

def first_add_food(level, x, y, food):
    max_x = x + 5
    max_y = y + 5
    a = True
    while a:
        food_x = random.randint(1, max_x)
        food_y = random.randint(1, max_y)
        if level[food_y][food_x] == " ":
            if food_x != x and food_y != y:
                level[food_y] = level[food_y][:food_x] + food + level[food_y][food_x+1:]
                a = False

def add_spike(level, x, y, spike):
    if random.randint(0,1) == 1:
        max_x = len(level[0])-1
        max_y = len(level)-1
        a = True
        while a:
            spike_x = random.randint(1, max_x)
            spike_y = random.randint(1, max_y)
            if level[spike_y][spike_x] == " ":
                if spike_x != x and spike_y != y:
                    level[spike_y] = level[spike_y][:spike_x] + spike + level[spike_y][spike_x+1:]
                    a = False


def instruction(food, spike):
    print("Welcome")
    print("You have limited quantity of steps")
    print("Gather " + food + " to get more steps")
    print("Walking through " + spike + " will take more steps")
    print("W, S, A, D - are for moving")
    print("Q - can be used to see this instruction again")
    print("X - ends this game")
    
def gameover(way):
    print("GAME OVER")
    print("Thank you for playing")
    print("You have made " + str(way) + " steps")
    print("Press anything to quit")
    if msvcrt.getch():
        print("")

def event_food(steps, way, x, y, level):
    steps += food_energy
    way +=1
    add_food(level, x, y, food)
    add_spike(level, x, y, spike)    
    return steps, way

def clear_screen():
    print("\n"*40)
    

def motion(level, x, y, steps, way, food, spike):
    trigger = True
    while trigger:       
        clear_screen()
        display(level, x, y)
        print("Steps: " + str(steps))
        print("Way: " + str(way))

        if steps >=1:
        
            key = msvcrt.getch() 
            try:
                if ord(key) == 119:  #W
                    if level[y-1][x] == food:
                        level[y-1] = level[y-1][:x] + " " + level[y-1][x+1:]
                        y-=1
                        steps, way = event_food(steps, way, x, y, level)
                        
                    elif level[y-1][x] == spike:
                        y-=1
                        steps -= spike_damage
                        way +=1
                    elif level[y-1][x] != "█":
                        y-=1
                        steps -= 1
                        way +=1
                
                if ord(key) == 115:  #S
                    if level[y+1][x] == food:
                        level[y+1] = level[y+1][:x] + " " + level[y+1][x+1:]
                        y+=1
                        steps, way = event_food(steps, way, x, y, level)
                    elif level[y+1][x] == spike:
                        y+=1
                        steps -= spike_damage
                        way +=1
                    elif level[y+1][x] != "█":
                        y+=1
                        steps -= 1
                        way +=1
                
                if ord(key) == 97:  #A
                    if level[y][x-1] == food:
                        level[y] = level[y][:x-1] + " " + level[y][x:]
                        x-=1
                        steps, way = event_food(steps, way, x, y, level)
                    elif level[y][x-1] == spike:
                        x-=1
                        steps -= spike_damage
                        way +=1
                    elif level[y][x-1] != "█":
                        x-=1
                        steps -= 1
                        way +=1
                
                if ord(key) == 100:  #D
                    if level[y][x+1] == food:
                        level[y] = level[y][:x+1] + " " + level[y][x+2:]
                        x+=1
                        steps, way = event_food(steps, way, x, y, level)
                    elif level[y][x+1] == spike:
                        x+=1
                        steps -= spike_damage
                        way +=1
                    elif level[y][x+1] != "█":
                        x+=1
                        steps -= 1
                        way +=1
                
                if ord(key) == 113:  #Q
                    clear_screen()
                    instruction()                
                    print("Press anything to return")
                    if msvcrt.getch():
                        pass
                if ord(key) == 120:  #X
                    break
            except:
                pass
        else:
            trigger = False
            gameover(way)

        
clear_screen()
instruction(food, spike)
print("Press anything to continue")
if msvcrt.getch():
    print("")
first_add_food(level1, 1, 1, food)
#add_spike(level1, 1, 1, spike)
motion(level1, 1, 1, steps, way, food, spike)
