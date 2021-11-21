print('''
     _____            _____       ___     ____________
    |     | \     /  |     |    /     \        |
    |     |  \   /   |     |   |       |       |
    |_____|   \ /    |____/    |       |       |
    |          |     |    \    |       |       |
    |          |     |     |   |       |       |
    |          |     |_____|    \ ___ /        |

''')

start = input('''
Hey user, How many i help you?

type "start" to begin.
type "exit" to exit.

--> ''')
# -------------------------[start]-----------------------------
if start == 'start' or start == 'Start':    #<-- start condition
    print('''Game Mode on
options :-
    1. math (mt)
    2. text / string (st)
    3. shapes (sh)
    4. sample code  (sCode)
type < cmd >
''')

    state = 1
    while state == 1: #<-- while loop condition
        choice = input("=> ")

    # -------------------------[math]--------------------------
        if(choice == 'mt'):
            mathstate = 1
            print('''
options :-
    1. add
    2. sub
    3. multi
    4. div''')
            while mathstate == 1:
                choice = input("++> ")
                #______________________[add]___________________
                if(choice == 'add'):
                    x = int(input ("x => "))
                    y = int(input ("y => "))
                    print(f"{x} + {y} = {x + y}")

                #______________________[sub]___________________
                elif(choice == 'sub'):
                    x = int(input ("x => "))
                    y = int(input ("y => "))
                    print(f"{x} - {y} = {x - y}")
                #______________________[multi]_________________
                elif(choice == 'multi'):
                    x = int(input ("x => "))
                    y = int(input ("y => "))
                    print(f"{x} x {y} = {x * y}")
                #______________________[div]___________________
                elif(choice == 'div'):
                    x = int(input ("x => "))
                    y = int(input ("y => "))
                    print(f"{x} / {y} = {x / y}")

                #______________________[exit]___________________
                elif(choice == 'exit'): #<-- exit controllor
                    break
                else:
                    print("choice not found -_-")
        # -------------------------[start]-----------------------------
        elif(choice == 'st'):
            mathstate = 1
            print('''
options :-
    1. add
    2. sub
    3. multi
    4. div''')
            while mathstate == 1:
                choice = input("++> ")
                if(choice == '1'):
                    pass
                elif(choice == '2'):
                    pass
                elif(choice == '3'):
                    pass
                elif(choice == '4'):
                    pass
                elif(choice == 'exit'): #<-- exit controllor
                    break
                else:
                    print("choice not found -_-")
        # -------------------------[start]-----------------------------
        elif(choice == 'sh'):
            mathstate = 1
            print('''
options :-
    1. add
    2. sub
    3. multi
    4. div''')
            while mathstate == 1:
                choice = input("++> ")
                if(choice == '1'):
                    pass
                elif(choice == '2'):
                    pass
                elif(choice == '3'):
                    pass
                elif(choice == '4'):
                    pass
                elif(choice == 'exit'): #<-- exit controllor
                    break
                else:
                    print("choice not found -_-")

                    
        # -------------------------[start]-----------------------------
        elif(choice == 'sCode'):
            mathstate = 1
            print('''
options :-
    1. add
    2. sub
    3. multi
    4. div''')
            while mathstate == 1:
                choice = input("++> ")
                if(choice == '1'):
                    pass
                elif(choice == '2'):
                    pass
                elif(choice == '3'):
                    pass
                elif(choice == '4'):
                    pass
                elif(choice == 'exit'): #<-- exit controllor
                    break
                else:
                    print("choice not found -_-")

        # -------------------------[exit main]-------------------------
        elif(choice == 'exit'): #<-- exit controllor
            break
        else:
            print("choice not found -_-")
else:
    print("Good Bye !!!")
