#import
import os
from colorama import Fore as F
import time
#import ao ficheiro "other_things.py"
from other_things import *

#cores
roxo = F.MAGENTA
reset = F.RESET
red = F.RED
verde = F.GREEN





#escolhas
def menu():
    print(roxo + f'''
    ===================================
    | {reset}1. REGISTAR NOVA PASSWORD {roxo}      |
    | {reset}2. VER PASSWORD {roxo}                |
    | {reset}3. SAIR{roxo}                         |
    ===================================''')

#encriptar as passwords
def encrypt(info, shift):
    mudar = ""
    for i in range(len(info)):
        char = info[i]
        if (char.isupper()):
            mudar += chr((ord(char) + shift -65) % 26 + 65)
        elif (char.islower()):
            mudar += chr((ord(char) + shift - 97) % 26 + 97)
        elif (char.isdigit()):
            number = (int(char) + shift) % 10
            mudar += str(number)
        else:
            mudar  += char
    return mudar

#dar decrypt as passwords
def decrypt(info, shift):
    voltar = ""
    for i in range(len(info)):
        char = info[i]
        if (char.isupper()):
            voltar += chr((ord(char) - shift -65) % 26 + 65)
        elif (char.islower()):
            voltar += chr((ord(char) - shift - 97) % 26 + 97)
        elif (char.isdigit()):
            number = (int(char) - shift) % 10
            voltar += str(number)
        else:
            voltar  += char
    return voltar




#escolher o que querem fazer
clear()
criador()
menu()
x =input(reset + '[' + roxo + 'PWD' + reset + ']' + '~: ' )
if x == '1':
    criador()
    #Adicionar password
    print(roxo + f'''
    ===================================
    | {reset}Site / Programa{roxo}                 |
    ===================================  ''')
    programa = input(reset + '[' + roxo + 'PWD' + reset + ']' + '~: ' )
    print(roxo + f'''
    ===================================
    | {reset}Username do programa{roxo}            |
    ===================================  ''')
    username = input(reset + '[' + roxo + 'PWD' + reset + ']' + '~: ' )
    print(roxo + f'''
    ===================================
    | {reset}Password do Programa{roxo}            |
    ===================================  ''')
    password = input(reset + '[' + roxo + 'PWD' + reset + ']' + '~: ' )
    shift = 6
    f = open('Passwords.txt', 'a')
    f.write(encrypt(programa, shift) + "|" + encrypt(username, shift) + "|" + encrypt(password, shift) + "\n")
    f.close()
    print(roxo + f'''
    ===================================
    | {reset}Password Guardada com {verde} Sucesso!{roxo}            |
    ===================================  ''')
elif x == '2':
    f = open('Passwords.txt', 'r')
    print('Programa:\t\tUsername:\t\tPassword:')
    for a in f:
        shift = 6
        info = a.split("|")
        print(decrypt(info[0], shift) + "\t\t" + decrypt(info[1], shift) + "\t\t" + decrypt(info[2], shift))
        time.sleep(10)
elif x == '3':
    quit()
else:
    print(red + 'Escolha errada')
    time.sleep(3)
    menu()








    
    


