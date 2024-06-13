import time
import os

def hello():
  print("\033[0;31m")
  print("███████╗ ██████╗ ██████╗      ██████╗██╗██╗  ██╗██╗     ███████╗     ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗")
  print("██╔════╝██╔═══██╗██╔══██╗    ██╔════╝██║██║ ██╔╝██║     ██╔════╝     ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║")
  print("█████╗  ██║   ██║██████╔╝    ██║     ██║█████╔╝ ██║     ███████╗     ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║")
  print("██╔══╝  ██║   ██║██╔══██╗    ██║     ██║██╔═██╗ ██║     ╚════██║     ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║")
  print("██║     ╚██████╔╝██║  ██║    ╚██████╗██║██║  ██╗███████╗███████║▄█╗  ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║ ██╗██╗██╗")
  print("╚═╝      ╚═════╝ ╚═╝  ╚═╝     ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═╝╚═╝╚═╝")
  print("\033[1;37m","\033[0;37m")

def noteikumi():
  print("  ░█▀█░█▀█░▀█▀░█▀▀░▀█▀░█░█░█░█░█▄█░▀█▀░█")
  print("  ░█░█░█░█░░█░░█▀▀░░█░░█▀▄░█░█░█░█░░█░░▀")
  print("  ░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀")
  print("\033[1;37m")
  print("    ","\033[1;33m","✴","\033[1;37m"," Tavs uzdevums ir izpildit testu un atbildēt uz jautājumiem par FOR ciklu!","\033[1;33m","✴","\033[1;37m")
  print()
  print("  ","\033[1;33m","✦","\033[1;37m","Tiek uzdoti 10 jautājumi par tēmu: 'Cikls ar priekšnosacījumu programmēšanas valodā Python' \n","\033[1;33m","  ✦","\033[1;37m","Doti 4 atbilžu varianti, taču tikai viens no tiem ir pareizs \n","\033[1;33m","  ✦","\033[1;37m","Uz katru jautājumu jāatbild vienu reizi \n","\033[1;33m","  ✦","\033[1;37m","Uz jautājumiem atbildat ar vajadzīgo burtu \n","\033[1;33m","  ✦","\033[1;37m","Atbilžu varianti tiks parādīti pēc testa izpildes")
  print()

def clear3S():
  time.sleep(3)
  os.system('clear')

def getName():
  while True:
    name = input("Ievadiet savu vārdu: ")
    print()
    if len(name) > 1 and not any(char.isdigit() for char in name):
      return name
    else:
      print("Nepareizi ievadīts vārds!")

def jaut1():
  print("\033[0;31m")
  print("░░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░▀█░░░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░░█░░░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░▀▀▀░▀░░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print("\033[1;37m")
  print("\033[1;33m","✴","\033[1;37m","Kurš no šiem ir pareizs cikls ar skaitītāju Python valodā, kas izdrukā skaitļus no 1 līdz 5?")
  print("  A) for i in range(5): print(i)\n  B) for i in range(1, 5): print(i)\n  C) for i in range(1, 6): print(i - 1)\n  D) for i in range(1, 6): print(i)\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      os.system('clear')
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut2():
  print("\033[0;31m")
  print("░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░▀▀▄░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░▄▀░░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░▀▀▀░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print("\033[1;37m")
  print("\033[1;33m","✴","\033[1;37m","Kāds ir funkcijas range(2, 10, 2) rezultāts?")
  print("  A) [2, 4, 6, 8] \n  B) [2, 4, 6, 8, 10]\n  C) [2, 3, 4, 5, 6, 7, 8, 9]\n  D) [2, 4, 8]\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      os.system('clear')
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut3():
  print("\033[0;31m")
  print("░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░▀▀█░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░░▀▄░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░▀▀▀░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print("\033[1;37m")
  print("\033[1;33m","✴","\033[1;37m","Kas tiek izdrukāts, ja tiek izpildīts šāds kods: for i in range(3): print(i)?")
  print("  A) 0, 1, 2 \n  B) 1, 2, 3\n  C) 0, 1, 2, 3\n  D) 1, 2\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      os.system('clear')
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut4():
  print("\033[0;31m")
  print("░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░█░█░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░░▀█░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░░░▀░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print("\033[1;37m")
  print("\033[1;33m","✴","\033[1;37m","Ko dara šis cikls: for i in range(5, 0, -1): print(i)?")
  print("  A) Izdrukā skaitļus no 5 līdz -1\n  B) Izdrukā skaitļus no 5 līdz\n  C) Izdrukā skaitļus no 1 līdz 5\n  D) Izdrukā skaitļus no 0 līdz -5\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      os.system('clear')
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut5():
  print("\033[0;31m")
  print("░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░█▀▀░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░▀▀▄░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░▀▀░░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print("\033[1;37m")
  print("\033[1;33m","✴","\033[1;37m","Kas ir pareizais intervāls, lai cikls izdrukātu pāra skaitļus no 2 līdz 10?")
  print("  A) range(1, 10, 2)\n  B) range(2, 10, 2)\n  C) range(2, 11, 2) \n  D) range(2, 12, 3)\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      os.system('clear')
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut6():
  print("\033[0;31m")
  print("░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░▄▀▀░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░█▀▄░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░▀▀▀░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print("\033[1;37m")
  print("\033[1;33m","✴","\033[1;37m","Kurš no šiem cikliem izdrukā katru elementu no saraksta [1, 2, 3, 4, 5]?")
  print("  A) for i in [1, 2, 3, 4, 5]: print(i)\n  B) for i in range(5): print(i)\n  C) for i in range(1, 5): print(i)\n  D) for i in range(1, 6): print(i - 1)\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      os.system('clear')
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut7():
  print("\033[0;31m")
  print("░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░▀▀█░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░▄▀░░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░▀░░░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print("\033[1;37m")
  print("\033[1;33m","✴","\033[1;37m","Kā izdrukāt katru otro elementu no saraksta [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]?")
  print("  A) for i in range(1, 9, 1): print(i)\n  B) for i in range(1, 10, 1): print(i)\n  C) for i in range(0, 9, 2): print(i)\n  D) for i in range(0, 10, 1): print(i) \n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      os.system('clear')
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut8():
  print("\033[0;31m")
  print("░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░▄▀▄░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░▄▀▄░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░░▀░░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print("\033[1;37m")
  print("\033[1;33m","✴","\033[1;37m","Kāda ir for cikla galvenā funkcija Python valodā")
  print("  A) Lai izpildītu kodu tikai vienreiz\n  B) Lai izpildītu kodu noteiktu reižu skaitu \n  C) Lai pārtrauktu programmas izpildi\n  D) Lai izveidotu mainīgo\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      os.system('clear')
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut9():
  print("\033[0;31m")
  print("░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░▄▀▄░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░░▀█░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░▀▀░░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print("\033[1;37m")
  print("\033[1;33m","✴","\033[1;37m","Ko izdrukā šis kods: for i in 'Python': print(i)?")
  print("  A) Katru burtu atsevišķā rindā\n  B) Vārdu 'Python' vienā rindā\n  C) Katru burtu un tā indeksu atsevišķā rindā\n  D) Burtus ar atstarpi vienā rindā\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      os.system('clear')
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut10():
  print("\033[0;31m")
  print("░░░░░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░▀█░░▄▀▄░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░░█░░█/█░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░▀▀▀░░▀░░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print("\033[1;37m")
  print("\033[1;33m","✴","\033[1;37m","Kāda ir atšķirība starp for ciklu un while ciklu Python valodā")
  print("  A) while cikls nostrādā konkrētu reižu skaitu, bet for cikls izpildās tikmēr, kamēr nosacījums ir patiess\n  B) for cikls nostrādā konkrētu reižu skaitu, bet while cikls izpildās tikmēr, kamēr nosacījums ir patiess\n  C) for cikls izpildās vienu reizi, bet while cikls atkārtojas\n  D) for cikls ir ātrāks par while ciklu\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      os.system('clear')
      return answer
    else:
      print("Nepareizi ievadīts burts!")
      os.system('clear')

def checkAnswers(answers):
  answerText = ""
  points = 0
  rightans = ['D', 'A', 'A', 'B', 'C', 'A', 'D', 'B', 'A', 'B']
  
  for i in range(len(answers)):
    if (rightans[i] == answers[i]):
      points = points + 1
    else:
      answerText = answerText + "\n✦ "+str((i)+1)+". jautājums\nJūsu atbilde: "+str(answers[i])+"\nPareizā atbilde: "+str(rightans[i])+"\n"

  return answerText, points

def iegutie():
  print("\033[0;31m")
  print("░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░ ░░░")
  print("░▀█▀░█▀▀░█▀▀░█░█░▀█▀░▀█▀░█▀▀░  ░█▀█░█░█░█▀█░█░█░▀█▀░▀█▀░░ ░░░")
  print("░░█░░█▀▀░█░█░█░█░░█░░░█░░█▀▀░  ░█▀▀░█░█░█░█░█▀▄░░█░░░█░░░ ░▀░")
  print("░▀▀▀░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀▀░  ░▀░░░▀▀▀░▀░▀░▀░▀░░▀░░▀▀▀░░ ░▀░")
  print("\033[1;37m")

def nepareizais():
  print("\033[0;31m")
  print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░ ░░░")
  print("░█▀█░█▀▀░█▀█░█▀█░█▀▄░█▀▀░▀█▀░▀▀█░▀█▀░ ░█▀█░▀█▀░█▀▄░▀█▀░█░░░█▀▄░█▀▀░▀█▀░▀█▀░█▀▀░░ ░░░")
  print("░█░█░█▀▀░█▀▀░█▀█░█▀▄░█▀▀░░█░░▄▀░░░█░░ ░█▀█░░█░░█▀▄░░█░░█░░░█░█░█▀▀░░█░░░█░░█▀▀░░ ░▀░")
  print("░▀░▀░▀▀▀░▀░░░▀░▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░ ░▀░▀░░▀░░▀▀░░▀▀▀░▀▀▀░▀▀░░▀▀▀░░▀░░▀▀▀░▀▀▀░░ ░▀░")
  print("\033[1;37m")

def skaitli(points):
  if(points == 1):
    print("\033[1;35m")
    print("\t\t\t\t\t\t\t ████")
    print("\t\t\t\t\t\t\t░░███")
    print("\t\t\t\t\t\t\t ░███")
    print("\t\t\t\t\t\t\t ░███")
    print("\t\t\t\t\t\t\t ░███")
    print("\t\t\t\t\t\t\t ░███")
    print("\t\t\t\t\t\t\t █████")
    print("\t\t\t\t\t\t\t ░░░░░")
    print("\033[1;37m")
  elif(points==2):
    print("\033[1;35m")
    print("\t\t\t\t\t\t\t  ████████")
    print("\t\t\t\t\t\t\t ███░░░░███")
    print("\t\t\t\t\t\t\t ░░░    ░███")
    print("\t\t\t\t\t\t\t   ███████")
    print("\t\t\t\t\t\t\t ███░░░░")
    print("\t\t\t\t\t\t\t ███      █")
    print("\t\t\t\t\t\t\t░██████████")
    print("\t\t\t\t\t\t\t ░░░░░░░░░░")
    print("\033[1;37m")
  elif(points==3):
    print("\033[1;35m")
    print("\t\t\t\t\t\t\t  ████████")
    print("\t\t\t\t\t\t\t ███░░░░███")
    print("\t\t\t\t\t\t\t ░░░    ░███")
    print("\t\t\t\t\t\t\t     ██████░ ")
    print("\t\t\t\t\t\t\t  ░░░░░░███")
    print("\t\t\t\t\t\t\t ███   ░███")
    print("\t\t\t\t\t\t\t░░████████")
    print("\t\t\t\t\t\t\t ░░░░░░░░  ")
    print("\033[1;37m")
  elif(points==4):
    print("\033[1;35m")
    print("\t\t\t\t\t\t\t  █████ █████ ")
    print("\t\t\t\t\t\t\t ░░███ ░░███ ")
    print("\t\t\t\t\t\t\t  ░███  ░███ █")
    print("\t\t\t\t\t\t\t  ░███████████")
    print("\t\t\t\t\t\t\t  ░░░░░░░███░█")
    print("\t\t\t\t\t\t\t        ░███░ ")
    print("\t\t\t\t\t\t\t        █████ ")
    print("\t\t\t\t\t\t\t        ░░░░░")
    print("\033[1;37m")
  elif(points==5):
    print("\033[1;35m")
    print("\t\t\t\t\t\t\t ██████████")
    print("\t\t\t\t\t\t\t░███░░░░░░█")
    print("\t\t\t\t\t\t\t░███     ░ ")
    print("\t\t\t\t\t\t\t░█████████ ")
    print("\t\t\t\t\t\t\t░░░░░░░░███")
    print("\t\t\t\t\t\t\t ███   ░███")
    print("\t\t\t\t\t\t\t░░████████")
    print("\t\t\t\t\t\t\t ░░░░░░░░  ")
    print("\033[1;37m")
  elif(points==6):
    print("\033[1;35m")
    print("\t\t\t\t\t\t\t  ████████ ")
    print("\t\t\t\t\t\t\t ███░░░░")
    print("\t\t\t\t\t\t\t░█████████ ")
    print("\t\t\t\t\t\t\t░███░░░░███")
    print("\t\t\t\t\t\t\t░███   ░███")
    print("\t\t\t\t\t\t\t░░████████ ")
    print("\t\t\t\t\t\t\t ░░░░░░░░  ")
    print("\033[1;37m")
  elif(points==7):
    print("\033[1;35m")
    print("\t\t\t\t\t\t\t ██████████")
    print("\t\t\t\t\t\t\t░███░░░░███")
    print("\t\t\t\t\t\t\t░░░    ███ ")
    print("\t\t\t\t\t\t\t      ███  ")
    print("\t\t\t\t\t\t\t     ███   ")
    print("\t\t\t\t\t\t\t    ███    ")
    print("\t\t\t\t\t\t\t   ███     ")
    print("\t\t\t\t\t\t\t  ░░░      ")
    print("\033[1;37m")
  elif(points==8):
    print("\033[1;35m")
    print("\t\t\t\t\t\t\t  ████████ ")
    print("\t\t\t\t\t\t\t ███░░░░███")
    print("\t\t\t\t\t\t\t░███   ░███")
    print("\t\t\t\t\t\t\t░░████████ ")
    print("\t\t\t\t\t\t\t ███░░░░███")
    print("\t\t\t\t\t\t\t░███   ░███")
    print("\t\t\t\t\t\t\t░░████████ ")
    print("\t\t\t\t\t\t\t ░░░░░░░░  ")
    print("\033[1;37m")
  elif(points==9):
    print("\033[1;35m")
    print("\t\t\t\t\t\t\t  ████████ ")
    print("\t\t\t\t\t\t\t ███░░░░███")
    print("\t\t\t\t\t\t\t░███   ░███")
    print("\t\t\t\t\t\t\t░░█████████")
    print("\t\t\t\t\t\t\t ░░░░░░░███")
    print("\t\t\t\t\t\t\t ███   ░███")
    print("\t\t\t\t\t\t\t ░░███████ ")
    print("\t\t\t\t\t\t\t ░░░░░░░░  ")
    print("\033[1;37m")
  else:
    print("\033[1;35m")
    print("\t\t\t\t\t\t\t ████     █████   ")
    print("\t\t\t\t\t\t\t░░███   ███░░░███ ")
    print("\t\t\t\t\t\t\t ░███  ███   ░░███")
    print("\t\t\t\t\t\t\t ░███ ░███    ░███")
    print("\t\t\t\t\t\t\t ░███ ░███    ░███")
    print("\t\t\t\t\t\t\t ░███ ░░███   ███ ")
    print("\t\t\t\t\t\t\t █████ ░░░█████░  ")
    print("\t\t\t\t\t\t\t░░░░░    ░░░░░░   ")
    print("\033[1;37m")

def nobeigums(name):
  print("\033[0;31m")
  print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▀▀░░░░░▀▀▀░░░░ ░░░░░░░░░░░░░░░░░░░░  ░░ ")
  print("░█▀█░█▀█░█░░░█▀▄░▀█▀░█▀▀░█▀▀░░░ ░█░█░█▀█░░░█▀█░▀█▀░█░░░█▀▄░▀█▀░▀▀█░█▀█░▀█▀ ░▀█▀░█▀▀░█▀▀░▀█▀░█░█  ░█")
  print("░█▀▀░█▀█░█░░░█░█░░█░░█▀▀░▀▀█░░░ ░█▀▄░█▀█░░░█▀▀░░█░░█░░░█░█░░█░░░░█░█▀█░░█░ ░░█░░█▀▀░▀▀█░░█░░█░█  ░▀")
  print("░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀░▄▀ ░▀░▀░▀░▀░░░▀░░░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀▀░░▀░▀░░▀░ ░░▀░░▀▀▀░▀▀▀░░▀░░▀▀▀  ░▀")
  print("\033[1;37m","\033[0;35m")
  print("░░░░░░░░░░░░░░░░░░░░░░░▀▄▀░░░░░░░░░░░░░░░░░░░░░░")
  print("░█░█░▀▀█░░░▀█▀░▀█▀░█░█░█▀▀░█▀█░█▀█░█▀█░█▀▀░░░░░░")
  print("░█░█░▄▀░░░░░█░░░█░░█▀▄░▀▀█░█▀█░█░█░█░█░▀▀█░░░░░░")
  print("░▀▀▀░▀▀▀░░░░▀░░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░░▀░","\033[1;37m",name,"\033[0;31m","!")
  print("\033[1;37m")

def pareizi10():
  print("\033[0;31m")
  print("░█▀█░█▀█░█▀▀░█░█░█▀▀░▀█▀░█▀▀░█░█░░░░░░░█░█░▀█▀░█▀▀░█▀▀░░░█▀█░█▀█░█▀▄░█▀▀░▀█▀░▀▀█░▀█▀░█")
  print("░█▀█░█▀▀░▀▀█░▀▄▀░█▀▀░░█░░█░░░█░█░░░░░░░▀▄▀░░█░░▀▀█░▀▀█░░░█▀▀░█▀█░█▀▄░█▀▀░░█░░▄▀░░░█░░▀")
  print("░▀░▀░▀░░░▀▀▀░░▀░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▄▀░░░░░▀░░▀▀▀░▀▀▀░▀▀▀░░░▀░░░▀░▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀")
  print("\033[1;37m")
