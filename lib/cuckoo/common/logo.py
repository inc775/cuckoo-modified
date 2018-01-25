# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import sys
import random

from lib.cuckoo.common.colors import color, yellow
from lib.cuckoo.common.constants import CUCKOO_VERSION

def logo():
    """Cuckoo asciiarts.
    @return: asciiarts array.
    """
    logos = []

    logos.append("""
                                 _|                            
     _|_|_|  _|    _|    _|_|_|  _|  _|      _|_|      _|_|    
   _|        _|    _|  _|        _|_|      _|    _|  _|    _|  
   _|        _|    _|  _|        _|  _|    _|    _|  _|    _|  
     _|_|_|    _|_|_|    _|_|_|  _|    _|    _|_|      _|_|""")

    logos.append("""
                      __                  
  .----..--.--..----.|  |--..-----..-----.
  |  __||  |  ||  __||    < |  _  ||  _  |
  |____||_____||____||__|__||_____||_____|""")

    logos.append("""
                          .:                 
                          ::                 
    .-.     ,  :   .-.    ;;.-.  .-.   .-.   
   ;       ;   ;  ;       ;; .' ;   ;';   ;' 
   `;;;;'.'`..:;._`;;;;'_.'`  `.`;;'  `;;'""")

    logos.append("""
  eeee e   e eeee e   e  eeeee eeeee 
  8  8 8   8 8  8 8   8  8  88 8  88 
  8e   8e  8 8e   8eee8e 8   8 8   8 
  88   88  8 88   88   8 8   8 8   8 
  88e8 88ee8 88e8 88   8 8eee8 8eee8""")

    logos.append("""
  _____________________________________/\/\_______________________________
  ___/\/\/\/\__/\/\__/\/\____/\/\/\/\__/\/\__/\/\____/\/\/\______/\/\/\___
  _/\/\________/\/\__/\/\__/\/\________/\/\/\/\____/\/\__/\/\__/\/\__/\/\_
  _/\/\________/\/\__/\/\__/\/\________/\/\/\/\____/\/\__/\/\__/\/\__/\/\_
  ___/\/\/\/\____/\/\/\/\____/\/\/\/\__/\/\__/\/\____/\/\/\______/\/\/\___
  ________________________________________________________________________""")

    logos.append("""
   _______ _     _ _______ _     _  _____   _____ 
   |       |     | |       |____/  |     | |     |
   |_____  |_____| |_____  |    \\_ |_____| |_____|""")

    logos.append("""
                     _ 
    ____ _   _  ____| |  _ ___   ___
   / ___) | | |/ ___) |_/ ) _ \ / _ \\
  ( (___| |_| ( (___|  _ ( |_| | |_| |
   \\____)____/ \\____)_| \\_)___/ \\___/""")

    logos.append("""
   ______   __  __   ______   ___   ___   ______   ______      
  /_____/\\ /_/\\/_/\\ /_____/\\ /___/\\/__/\\ /_____/\\ /_____/\\     
  \\:::__\\/ \\:\\ \\:\\ \\\\:::__\\/ \\::.\\ \\\\ \\ \\\\:::_ \\ \\\\:::_ \\ \\    
   \\:\\ \\  __\\:\\ \\:\\ \\\\:\\ \\  __\\:: \\/_) \\ \\\\:\\ \\ \\ \\\\:\\ \\ \\ \\   
    \\:\\ \\/_/\\\\:\\ \\:\\ \\\\:\\ \\/_/\\\\:. __  ( ( \\:\\ \\ \\ \\\\:\\ \\ \\ \\  
     \\:\\_\\ \\ \\\\:\\_\\:\\ \\\\:\\_\\ \\ \\\\: \\ )  \\ \\ \\:\\_\\ \\ \\\\:\\_\\ \\ \\ 
      \\_____\\/ \\_____\\/ \\_____\\/ \\__\\/\\__\\/  \\_____\\/ \\_____\\/""")

    logos.append("""
    sSSs   .S       S.     sSSs   .S    S.     sSSs_sSSs      sSSs_sSSs    
   d%%SP  .SS       SS.   d%%SP  .SS    SS.   d%%SP~YS%%b    d%%SP~YS%%b   
  d%S'    S%S       S%S  d%S'    S%S    S&S  d%S'     `S%b  d%S'     `S%b  
  S%S     S%S       S%S  S%S     S%S    d*S  S%S       S%S  S%S       S%S  
  S&S     S&S       S&S  S&S     S&S   .S*S  S&S       S&S  S&S       S&S  
  S&S     S&S       S&S  S&S     S&S_sdSSS   S&S       S&S  S&S       S&S  
  S&S     S&S       S&S  S&S     S&S~YSSY%b  S&S       S&S  S&S       S&S  
  S&S     S&S       S&S  S&S     S&S    `S%  S&S       S&S  S&S       S&S  
  S*b     S*b       d*S  S*b     S*S     S%  S*b       d*S  S*b       d*S  
  S*S.    S*S.     .S*S  S*S.    S*S     S&  S*S.     .S*S  S*S.     .S*S  
   SSSbs   SSSbs_sdSSS    SSSbs  S*S     S&   SSSbs_sdSSS    SSSbs_sdSSS   
    YSSP    YSSP~YSSY      YSSP  S*S     SS    YSSP~YSSY      YSSP~YSSY    
                                 SP                                        
                                 Y""")

    logos.append("""
           _______                   _____                    _____          
          /::\\    \\                 /\\    \\                  /\\    \\         
         /::::\\    \\               /::\\____\\                /::\\    \\        
        /::::::\\    \\             /::::|   |               /::::\\    \\       
       /::::::::\\    \\           /:::::|   |              /::::::\\    \\      
      /:::/~~\\:::\\    \\         /::::::|   |             /:::/\\:::\\    \\     
     /:::/    \\:::\\    \\       /:::/|::|   |            /:::/  \\:::\\    \\    
    /:::/    / \\:::\\    \\     /:::/ |::|   |           /:::/    \\:::\\    \\   
   /:::/____/   \\:::\\____\\   /:::/  |::|___|______    /:::/    / \\:::\\    \\  
  |:::|    |     |:::|    | /:::/   |::::::::\\    \\  /:::/    /   \\:::\\ ___\\ 
  |:::|____|     |:::|    |/:::/    |:::::::::\\____\\/:::/____/  ___\\:::|    |
   \\:::\\    \\   /:::/    / \\::/    / ~~~~~/:::/    /\\:::\\    \\ /\\  /:::|____|
    \\:::\\    \\ /:::/    /   \\/____/      /:::/    /  \\:::\\    /::\\ \\::/    / 
     \\:::\\    /:::/    /                /:::/    /    \\:::\\   \\:::\\ \\/____/  
      \\:::\\__/:::/    /                /:::/    /      \\:::\\   \\:::\\____\\    
       \\::::::::/    /                /:::/    /        \\:::\\  /:::/    /    
        \\::::::/    /                /:::/    /          \\:::\\/:::/    /     
         \\::::/    /                /:::/    /            \\::::::/    /      
          \\::/____/                /:::/    /              \\::::/    /       
           ~~                      \\::/    /                \\::/____/        
                                    \\/____/                                  
                                                       it's Cuckoo!""")

    logos.append("""
            _       _                   _             _              _            _       
          /\\ \\     /\\_\\               /\\ \\           /\\_\\           /\\ \\         /\\ \\     
         /  \\ \\   / / /         _    /  \\ \\         / / /  _       /  \\ \\       /  \\ \\    
        / /\\ \\ \\  \\ \\ \\__      /\\_\\ / /\\ \\ \\       / / /  /\\_\\    / /\\ \\ \\     / /\\ \\ \\   
       / / /\\ \\ \\  \\ \\___\\    / / // / /\\ \\ \\     / / /__/ / /   / / /\\ \\ \\   / / /\\ \\ \\  
      / / /  \\ \\_\\  \\__  /   / / // / /  \\ \\_\\   / /\\_____/ /   / / /  \\ \\_\\ / / /  \\ \\_\\ 
     / / /    \\/_/  / / /   / / // / /    \\/_/  / /\\_______/   / / /   / / // / /   / / / 
    / / /          / / /   / / // / /          / / /\\ \\ \\     / / /   / / // / /   / / /  
   / / /________  / / /___/ / // / /________  / / /  \\ \\ \\   / / /___/ / // / /___/ / /   
  / / /_________\\/ / /____\\/ // / /_________\\/ / /    \\ \\ \\ / / /____\\/ // / /____\\/ /    
  \\/____________/\\/_________/ \\/____________/\\/_/      \\_\\_\\\\/_________/ \\/_________/""")

    logos.append("""
                               ),-.     /
  Cuckoo Sandbox              <(a  `---',' 
     no chance for malwares!  ( `-, ._> )
                               ) _>.___/
                                   _/""")

    logos.append("""
  .-----------------.
  | Cuckoo Sandbox? |
  |     OH NOES!    |\\  '-.__.-'   
  '-----------------' \\  /oo |--.--,--,--.
                         \\_.-'._i__i__i_.'
                               \"\"\"\"\"\"\"\"\"""")

    logos.append("""
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || | _____  _____ | || |     ______   | || |  ___  ____   | || |     ____     | || |     ____     | |
| |   .' ___  |  | || ||_   _||_   _|| || |   .' ___  |  | || | |_  ||_  _|  | || |   .'    `.   | || |   .'    `.   | |
| |  / .'   \_|  | || |  | |    | |  | || |  / .'   \_|  | || |   | |_/ /    | || |  /  .--.  \  | || |  /  .--.  \  | |
| |  | |         | || |  | '    ' |  | || |  | |         | || |   |  __'.    | || |  | |    | |  | || |  | |    | |  | |
| |  \ `.___.'\  | || |   \ `--' /   | || |  \ `.___.'\  | || |  _| |  \ \_  | || |  \  `--'  /  | || |  \  `--'  /  | |
| |   `._____.'  | || |    `.__.'    | || |   `._____.'  | || | |____||____| | || |   `.____.'   | || |   `.____.'   | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
 .-----------------. .----------------.  .----------------.  .----------------.  .----------------.                     
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |                    
| | ____  _____  | || |  ____  ____  | || |     ____     | || | _____  _____ | || |      __      | |                    
| ||_   \|_   _| | || | |_  _||_  _| | || |   .'    `.   | || ||_   _||_   _|| || |     /  \     | |                    
| |  |   \ | |   | || |   \ \  / /   | || |  /  .--.  \  | || |  | | /\ | |  | || |    / /\ \    | |                    
| |  | |\ \| |   | || |    \ \/ /    | || |  | |    | |  | || |  | |/  \| |  | || |   / ____ \   | |                    
| | _| |_\   |_  | || |    _|  |_    | || |  \  `--'  /  | || |  |   /\   |  | || | _/ /    \ \_ | |                    
| ||_____|\____| | || |   |______|   | || |   `.____.'   | || |  |__/  \__|  | || ||____|  |____|| |                    
| |              | || |              | || |              | || |              | || |              | |                    
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |                    
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'                     """)

    logos.append("""
8 8888     ,o888888o.  `8.`888b                 ,8' .8.          8 888888888o   8 8888888888   8 8888           d888888o.  
           8 8888  . 8888     `88. `8.`888b               ,8' .888.         8 8888    `88. 8 8888         8 8888         .`8888:' `88.
           8 8888 ,8 8888       `8b `8.`888b             ,8' :88888.        8 8888     `88 8 8888         8 8888         8.`8888.   Y8
           8 8888 88 8888        `8b `8.`888b     .b    ,8' . `88888.       8 8888     ,88 8 8888         8 8888         `8.`8888.    
           8 8888 88 8888         88  `8.`888b    88b  ,8' .8. `88888.      8 8888.   ,88' 8 888888888888 8 8888          `8.`8888.   
           8 8888 88 8888         88   `8.`888b .`888b,8' .8`8. `88888.     8 8888888888   8 8888         8 8888           `8.`8888.  
88.        8 8888 88 8888        ,8P    `8.`888b8.`8888' .8' `8. `88888.    8 8888    `88. 8 8888         8 8888            `8.`8888. 
`88.       8 888' `8 8888       ,8P      `8.`888`8.`88' .8'   `8. `88888.   8 8888      88 8 8888         8 8888        8b   `8.`8888.
  `88o.    8 88'   ` 8888     ,88'        `8.`8' `8,`' .888888888. `88888.  8 8888    ,88' 8 8888         8 8888        `8b.  ;8.`8888
    `Y888888 '        `8888888P'           `8.`   `8' .8'       `8. `88888. 8 888888888P   8 888888888888 8 888888888888 `Y8888P ,88P'
                                                                                                                                      
    ,o888888o.    8 8888      88     ,o888888o.    8 8888     ,88'  ,o888888o.         ,o888888o.                                     
   8888     `88.  8 8888      88    8888     `88.  8 8888    ,88'. 8888     `88.    . 8888     `88.                                   
,8 8888       `8. 8 8888      88 ,8 8888       `8. 8 8888   ,88',8 8888       `8b  ,8 8888       `8b                                  
88 8888           8 8888      88 88 8888           8 8888  ,88' 88 8888        `8b 88 8888        `8b                                 
88 8888           8 8888      88 88 8888           8 8888 ,88'  88 8888         88 88 8888         88                                 
88 8888           8 8888      88 88 8888           8 8888 88'   88 8888         88 88 8888         88                                 
88 8888           8 8888      88 88 8888           8 888888<    88 8888        ,8P 88 8888        ,8P                                 
`8 8888       .8' ` 8888     ,8P `8 8888       .8' 8 8888 `Y8.  `8 8888       ,8P  `8 8888       ,8P                                  
   8888     ,88'    8888   ,d8P     8888     ,88'  8 8888   `Y8. ` 8888     ,88'    ` 8888     ,88'                                   
    `8888888P'       `Y88888P'       `8888888P'    8 8888     `Y8.  `8888888P'         `8888888P'                                     
""")

    logos.append("""
jow   ls  u koo
   XXX   . .   
   X.X   . .   
   ..X   . .   
   ..X   . .   
   ..X   . .   
   ...   . .   
               
jowabels cuckoo
               
""")

    logos.append("""
_________ _______           _______  ______   _______  _       _______    _______           _______  _        _______  _______ 
\__    _/(  ___  )|\     /|(  ___  )(  ___ \ (  ____ \( \     (  ____ \  (  ____ \|\     /|(  ____ \| \    /\(  ___  )(  ___  )
   )  (  | (   ) || )   ( || (   ) || (   ) )| (    \/| (     | (    \/  | (    \/| )   ( || (    \/|  \  / /| (   ) || (   ) |
   |  |  | |   | || | _ | || (___) || (__/ / | (__    | |     | (_____   | |      | |   | || |      |  (_/ / | |   | || |   | |
   |  |  | |   | || |( )| ||  ___  ||  __ (  |  __)   | |     (_____  )  | |      | |   | || |      |   _ (  | |   | || |   | |
   |  |  | |   | || || || || (   ) || (  \ \ | (      | |           ) |  | |      | |   | || |      |  ( \ \ | |   | || |   | |
|\_)  )  | (___) || () () || )   ( || )___) )| (____/\| (____/Y\____) |  | (____/\| (___) || (____/\|  /  \ \| (___) || (___) |
(____/   (_______)(_______)|/     \||/ \___/ (_______/(_______|_______)  (_______/(_______)(_______/|_/    \/(_______)(_______)
                                                                                                                               
""")

    logos.append("""
                   o                  o           o      
                   O                 O           O       
                   o                 O           o       
                   o                 o           O       
.oOo  O   o  .oOo  O  o  .oOo. .oOo. OoOo. .oOo. o  .oOo 
O     o   O  O     OoO   O   o O   o O   o OooO' O  `Ooo.
o     O   o  o     o  O  o   O o   O o   O O     o      O
`OoO' `OoO'o `OoO' O   o `OoO' `OoO' `OoO' `OoO' Oo `OoO'
                                                         """)

    print(color(random.choice(logos), random.randrange(31, 37)))
    print
    print(" Cuckoo Sandbox %s" % yellow(CUCKOO_VERSION))
    print(" www.cuckoosandbox.org")
    print(" Copyright (c) 2010-2015")
    print
    sys.stdout.flush()
