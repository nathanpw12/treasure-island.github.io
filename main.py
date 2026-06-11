# ORIGINAL REPOSITORIE: https://github.com/nathanpw12/100-Days-of-Code-The-Complete-Python-Pro-Bootcamp/blob/master/Day%203/Treasure%20Island%20Project/task.py

print(r'''
*******************************************************************************
          ___________                                                  
          \__    ___/______   ____ _____    ________ _________   ____  
            |    |  \_  __ \_/ __ \\__  \  /  ___/  |  \_  __ \_/ __ \ 
 Find The   |    |   |  | \/\  ___/ / __ \_\___ \|  |  /|  | \/\  ___/   Game
            |____|   |__|    \___  >____  /____  >____/ |__|    \___  >
                                 \/     \/     \/                   \/ 

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;    (💎) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("     ♛ Welcome to Treasure Island ♛\n")
print(" ◆ Your mission is to find the treasure ◆\n")

position1 = input('''【 You're on the road, do you want to go 】 \n            ▶ Left or Right? ◀ \n↳ ''').lower().replace(
    " ", "")

# Left or Right
if position1 == 'right':

    position2 = input(
        '''【 You've found a river, do you want to 】 \n            ▶ Wait or Swim? ◀ \n↳ ''').lower().replace(" ", "")

    # Nível 2: Wait or Swim (Só acontece se escolher Right)
    if position2 == 'wait':
        print('\n🚪 While waiting, you notice colorful doors in the distance 🚪\n')
        position3 = input(
            '【 You approach and see 3 doors, which door do you want to open 】 \n            ▶ Red, Blue or Yellow? ◀ \n↳ ').lower().replace(
            " ", "")

        # Nível 3: As Portas (Só acontece se escolher Wait)
        if position3 == 'red':
            print('''\n        ☠︎︎ You were burned by fire ☠︎︎\n               ✖ Game Over ✖ ''')
        elif position3 == 'blue':
            print('''\n        ☠︎︎ You were devoured by beasts ☠︎\n               ✖ Game Over ✖ ''')
        elif position3 == 'yellow':
            print(r'''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
******************************************⠀⠀⠀⠀⠀⠀

       💎 You found the treasure! 💎

    ⠀⠀⠀⢠⡄⢠⣤⣤⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⣤⣤⡄⢠⡄⠀⠀⠀⠀
    ⠀⠀⠀⢸⡇⢸⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⡇⢸⡇⠀⠀⠀
    ⠀⠀⠀⣿⡇⢸⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⡇⢸⣿⠀⠀⠀
    ⠀⠀⢀⣿⡇⢸⣿⣿⠀⣿⣿⣿⠟⠛⠛⠛⠛⠻⣿⣿⣿⠀⣿⣿⡇⢸⣿⡀⠀⠀
    ⠀⠀⢈⡉⢁⣀⣉⣉⣀⣉⣉⣉⠀⣴⠖⠲⣦⠀⣉⣉⣉⣀⣉⣉⣀⡈⢉⡁⠀⠀
    ⠀⠀⢸⡇⢸⣿⣿⣿⣿⣿⣿⣿⠀⣿💎⣿⠀⣿⣿⣿⣿⣿⣿⣿⡇⢸⡇⠀⠀
    ⠀⠀⢸⡇⢸⣿⣿⣿⣿⣿⣿⣿⠀⣿⣧⣼⣿⠀⣿⣿⣿⣿⣿⣿⣿⡇⢸⡇⠀⠀
    ⠀⠀⢸⡇⢸⣿⣿⣿⣿⣿⣿⣿⣀⣉⣉⣉⣉⣀⣿⣿⣿⣿⣿⣿⣿⡇⢸⡇⠀⠀
    ⠀⠀⠘⠇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠸⠃⠀⠀
    ⠀⠀⢰⣄⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⣠⡆⠀⠀
    ⠀⠀⠘⠛⠃⠈⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠁⠘⠛⠃⠀⠀

         🎉 Congratulations!! 🎉

******************************************
⠀⠀
         ❤ 𝚃𝙷𝙰𝙽𝙺𝚂 𝙵𝙾𝚁 𝙿𝙻𝙰𝚈𝙸𝙽𝙶! ❤ 
          〘 𝗴𝗶𝘁𝗵𝘂𝗯 @𝗻𝗮𝘁𝗵𝗮𝗻𝗽𝘄𝟭𝟮 〙
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
 ''')
        else:
            print('''⚠ Invalid input, please try again ⚠︎\n''')

    elif position2 == 'swim':
        print('''\n        ☠︎︎ You were attacked by trout ☠︎︎\n              ✖ Game Over ✖ ''')
    else:
        print('''⚠ Invalid input, please try again ⚠︎\n''')

elif position1 == 'left':
    print('''\n        ☠︎︎ You fell into a hole ☠︎︎\n             ✖ Game Over ✖ ''')
else:
    print('''⚠ Invalid input, please try again ⚠︎\n''')
