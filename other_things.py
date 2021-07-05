#imports
import os
from colorama import Fore as F


# letras princiapis
def criador():
    clear()
    print(f''' {F.GREEN}    
 ___                              _ 
| _ \__ _ _______ __ _____ _ _ __| |
|  _/ _` (_-<_-< V  V / _ \ '_/ _` |
|_| \__,_/__/__/\_/\_/\___/_| \__,_|
|  \/  |__ _ _ _  __ _ __ _ ___ _ _ 
| |\/| / _` | ' \/ _` / _` / -_) '_|
|_|  |_\__,_|_||_\__,_\__, \___|_|  
                      |___/
      
''')



# limpar ecrã
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')