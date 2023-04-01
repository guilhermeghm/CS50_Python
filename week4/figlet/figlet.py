from pyfiglet import Figlet
import random
import sys 

figlet = Figlet()
fontsList = figlet.getFonts()

if len(sys.argv) <= 1:
    inputUser = input("Input: ")
    font = random.choice(fontsList)
    figlet.setFont(font=font)
    print(figlet.renderText(inputUser))
elif sys.argv[1] != "-f" or "--font" and sys.argv[2] not in fontsList:
    sys.exit("Invalid usage")
else:
    inputUser = input("Input: ")
    font = sys.argv[2]
    figlet.setFont(font=font)
    print(figlet.renderText(inputUser))   
