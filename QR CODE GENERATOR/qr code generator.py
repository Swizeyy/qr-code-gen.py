from colorama import Fore
from pyfade import Fade
import qrcode
import sys, qrcode
from qrcode import main
from qrtools import *
from PIL import Image
from pyzbar import pyzbar
import os
from time import *
from slowprint.slowprint import *

def clear():
        os.system("cls")

clear()

name = """           ██████╗ ██████╗      ██████╗ ██████╗ ██████╗ ███████╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
          ██╔═══██╗██╔══██╗    ██╔════╝██╔═══██╗██╔══██╗██╔════╝    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
          ██║   ██║██████╔╝    ██║     ██║   ██║██║  ██║█████╗      ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
          ██║▄▄ ██║██╔══██╗    ██║     ██║   ██║██║  ██║██╔══╝      ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
          ╚██████╔╝██║  ██║    ╚██████╗╚██████╔╝██████╔╝███████╗    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
           ╚══▀▀═╝ ╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                                                       """



proposition1 = "             [1] créer un QR-code"
proposition2 = "                              [2] détails d'un QR-code"
proposition3 = "                              [3] aide pour obtenir les détails d'un QR-code"

print(Fore.LIGHTRED_EX + name)

print(Fore.LIGHTYELLOW_EX + proposition1 + Fore.GREEN + proposition2 + Fore.LIGHTCYAN_EX + proposition3 + Fore.RESET )

print('')

choise = input(Fore.LIGHTMAGENTA_EX + 'option' +Fore.LIGHTWHITE_EX + ' > ' + Fore.RESET)

if choise == "1" :
      lien = input(Fore.GREEN + 'lien >' + Fore.RESET)
      qrcode.QRCode(version=25)
      image = qrcode.make(lien)
      image.save('result/qrcode.png')
      print(Fore.GREEN + "Votre qrcode viens d'être crée avec le lien : " + lien )
      finish = input(Fore.LIGHTBLACK_EX + 'appuyez sur entrée pour fermer le programe' + Fore.RESET)

elif choise == "2" :

    img = Image.open('qrcode/qrcode.png')
    output = pyzbar.decode(img)
    print("")
    print(output)
    finish = input(Fore.LIGHTBLACK_EX + 'appuyez sur entrée pour fermer le programe' + Fore.RESET)


Fore.RESET

if choise == "3" :
    qrcode = "qrcode.png"
    slowprint(Fore.LIGHTBLUE_EX + "pour vérifier un QR-Code, il faut que le fichier se nomme \n"  + Fore.LIGHTRED_EX + qrcode + Fore.LIGHTBLUE_EX + "\nune fois rennomé , placez le dans le dossier qrcode \n" "ensuite relancer le programme et choissisez l'option 2" + Fore.LIGHTGREEN_EX + "\nVoila les détails du qrcode sont a vous :)" + Fore.RESET, 0.3)
    finish = input(Fore.LIGHTBLACK_EX + 'appuyez sur entrée pour fermer le programe' + Fore.RESET)

