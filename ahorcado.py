import random
import re
import draw
import os

count = 0
started = True
selectedCharacter = ""
charPulse = []
charPulseStr = ""
finish = ""


def newGame():
    global count
    global started
    global myTip
    global charPulse
    global charPulseStr
    count = 0
    started = True
    myTip = []
    randomWords()
    charPulse = []
    charPulseStr = ""


def randomWords():
    global wordsChoice
    global myTip
    global finish
    words = open('D:\dictionary.txt').read().splitlines()
    wordsChoice = random.choice(words)
    wordsChoice = wordsChoice.upper()
    myTip = [" _ "]*len(wordsChoice)
    finish = "".join(myTip)


def welcome():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(draw.titulo)
    print("\nHola! este es un proyecto basado en el popular juego Ahorcado.")
    print("\nTu palabra tiene >> " + str(len(wordsChoice)) + " << letras.")


def graphGame():
    welcome()
    global charPulseStr
    print('''+----------------------------------------------------------+
    '''+"".join(myTip)+'''
+----------------------------------------------------------+''')
    print(draw.draw[count])
    print("+----------------------------------------------------------+")
    print("Letras pulsadas: "+charPulseStr)
    print("+----------------------------------------------------------+")


def comprobar(selectedCharacter):
    global count
    global charPulseStr
    global charPulse
    if wordsChoice.find(selectedCharacter) >= 0:
        for c in re.finditer(selectedCharacter, wordsChoice, re.IGNORECASE):
            myTip[c.start():c.end()] = list(c.group())
        charPulse.append(selectedCharacter)
        charPulseStr = ','.join(charPulse)
    else:
        for c in re.finditer(selectedCharacter, wordsChoice, re.IGNORECASE):
            myTip[c.start():c.end()] = list(c.group())
        charPulse.append(selectedCharacter)
        charPulseStr = ','.join(charPulse)
        count += 1


def check(selectedCharacter):
    global charPulse
    selectedCharacter = input("Pulsa una letra: ").upper()
    if len(selectedCharacter) != 1:
        print('Introduce una sola letra.')
        check(selectedCharacter)
    elif selectedCharacter in charPulse:
        print('Ya elegiste esa letra')
        check(selectedCharacter)
    elif selectedCharacter not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
        print('Tiene que ser una letra')
        check(selectedCharacter)
    else:
        comprobar(selectedCharacter)


while started == True:
    randomWords()
    welcome()
    graphGame()
    check(selectedCharacter)
    started = False

while count < 8:
    finish = "".join(myTip)
    if finish == wordsChoice:
        graphGame()
        print('\n¡Felicidades! acertaste la palabra.\n')
        continuar = input("Quieres continuar? Si/No \n").upper()
        if continuar.startswith('S'):
            newGame()
        else:
            break

    if count == 7:
        graphGame()
        print("\nPerdiste...")
        print("La palabra era "+wordsChoice+"\n")
        continuar = input("Quieres continuar? Si/No \n").upper()
        if continuar.startswith('S'):
            newGame()
        else:
            break
    welcome()
    graphGame()
    check(selectedCharacter)
    started = False
    print(finish)
