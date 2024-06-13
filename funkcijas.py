import time
import os

def hello():
  print()
  print("      ░█▀▀░█▀█░█▀▄░░░█▀▀░▀█▀░█░█░█░░░█▀▀░░░░  ░█▀█░█░█░▀█▀░█░█░█▀█░█▀█  "
  )
  print("      ░█▀▀░█░█░█▀▄░░░█░░░░█░░█▀▄░█░░░▀▀█░░░░  ░█▀▀░░█░░░█░░█▀█░█░█░█░█  ")
  print("      ░▀░░░▀▀▀░▀░▀░░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀▀▀░▄▀░  ░▀░░░░▀░░░▀░░▀░▀░▀▀▀░▀░▀  ")
  print()

def noteikumi():
  print("  ░█▀█░█▀█░▀█▀░█▀▀░▀█▀░█░█░█░█░█▄█░▀█▀░█")
  print("  ░█░█░█░█░░█░░█▀▀░░█░░█▀▄░█░█░█░█░░█░░▀")
  print("  ░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀")
  print()
  print("    Tavs uzdevums ir izpildit testu un atbildēt uz jautājumiem par FOR ciklu!")
  print("  ✦ Tiek uzdoti 10 jautājumi par tēmu: 'Cikls ar priekšnosacījumu programmēšanas valodā Python' \n  ✦ Doti 4 atbilžu varianti, taču tikai viens no tiem ir pareizs \n  ✦ Uz katru jautājumu jāatbild vienu reizi \n  ✦ Uz jautājumiem atbildat ar vajadzīgo burtu \n  ✦ Atbilžu varianti tiks parādīti pēc testa izpildes")
  print()

def clear5S():
  time.sleep(5)
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
  print("░░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░▀█░░░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░░█░░░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░▀▀▀░▀░░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print()
  print("Kurš no šiem ir pareizs cikls ar skaitītāju Python valodā, kas izdrukā skaitļus no 1 līdz 5?")
  print("  A) for i in range(5): print(i)\n  B) for i in range(1, 5): print(i)\n  C) for i in range(1, 6): print(i - 1)\n  D) for i in range(1, 6): print(i)\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut2():
  print("░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░▀▀▄░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░▄▀░░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░▀▀▀░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print()
  print("Kāds ir funkcijas range(2, 10, 2) rezultāts?")
  print("  A) [2, 4, 6, 8] \n  B) [2, 4, 6, 8, 10]\n  C) [2, 3, 4, 5, 6, 7, 8, 9]\n  [2, 4, 8]\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut3():
  print("░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░▀▀█░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░░▀▄░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░▀▀▀░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print()
  print("Kas tiek izdrukāts, ja tiek izpildīts šāds kods: for i in range(3): print(i)?")
  print("  A) 0, 1, 2 \n  B) 1, 2, 3\n  C) 0, 1, 2, 3\n  D) 1, 2\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut4():
  print("░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░█░█░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░░▀█░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░░░▀░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print()
  print("Ko dara šis cikls: for i in range(5, 0, -1): print(i)?")
  print("  A) Izdrukā skaitļus no 5 līdz -1\n  B) Izdrukā skaitļus no 5 līdz\n  C) Izdrukā skaitļus no 1 līdz 5\n  D) Izdrukā skaitļus no 0 līdz -5\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut5():
  print("░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░█▀▀░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░▀▀▄░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░▀▀░░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print()
  print("Kas ir pareizais intervāls, lai cikls izdrukātu pāra skaitļus no 2 līdz 10?")
  print("  A) range(1, 10, 2)\n  B) range(2, 10, 2)\n  C) range(2, 11, 2) \n  D) range(2, 12, 3)\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut6():
  print("░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░▄▀▀░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░█▀▄░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░▀▀▀░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print()
  print("Kurš no šiem cikliem izdrukā katru elementu no saraksta [1, 2, 3, 4, 5]?")
  print("  A) for i in [1, 2, 3, 4, 5]: print(i)\n  B) for i in range(5): print(i)\n  C) for i in range(1, 5): print(i)\n  D) for i in range(1, 6): print(i - 1)\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut7():
  print("░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░▀▀█░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░▄▀░░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░▀░░░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print()
  print("Kā izdrukāt katru otro elementu no saraksta [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]?")
  print("  A) for i in range(1, 9, 1): print(i)\n  B) for i in range(1, 10, 1): print(i)\n  C) for i in range(0, 9, 2): print(i)\n  D) for i in range(0, 10, 1): print(i) \n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut8():
  print("░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░▄▀▄░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░▄▀▄░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░░▀░░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print()
  print("Kāda ir for cikla galvenā funkcija Python valodā")
  print("  A) Lai izpildītu kodu tikai vienreiz\n  B) Lai izpildītu kodu noteiktu reižu skaitu \n  C) Lai pārtrauktu programmas izpildi\n  D) Lai izveidotu mainīgo\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut9():
  print("░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░▄▀▄░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░░▀█░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░▀▀░░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print()
  print("Ko izdrukā šis kods: for i in 'Python': print(i)?")
  print("  A) Katru burtu atsevišķā rindā\n  B) Vārdu 'Python' vienā rindā\n  C) Katru burtu un tā indeksu atsevišķā rindā\n  D) Burtus ar atstarpi vienā rindā\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def jaut10():
  print("░░░░░░░░░░░ ░░░░░░░░░░░░░░░░░▀▀▀░░░░░░░░░░░░░░░░")
  print("░▀█░░▄▀▄░░░ ░▀▀█░█▀█░█░█░▀█▀░█▀█░▀▀█░█░█░█▄█░█▀▀")
  print("░░█░░█/█░░░ ░░░█░█▀█░█░█░░█░░█▀█░░░█░█░█░█░█░▀▀█")
  print("░▀▀▀░░▀░░▀░ ░▀▀░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀")
  print()
  print("Kāda ir atšķirība starp for ciklu un while ciklu Python valodā")
  print("  A) while cikls nostrādā konkrētu reižu skaitu, bet for cikls izpildās tikmēr, kamēr nosacījums ir patiess\n  B) for cikls nostrādā konkrētu reižu skaitu, bet while cikls izpildās tikmēr, kamēr nosacījums ir patiess\n  C) for cikls izpildās vienu reizi, bet while cikls atkārtojas\n  D) for cikls ir ātrāks par while ciklu\n")

  while True:
    answer = input("Ievadiet savu atbildi: ").upper()
    if answer in ('A', 'B', 'C', 'D'):
      return answer
    else:
      print("Nepareizi ievadīts burts!")

def checkAnswers(answers):
  answerText = ""
  points = 0
  rightans = ['D', 'A', 'A', 'B', 'C', 'A', 'D', 'B', 'A', 'B']
  for i in range(len(answers)):

    if (rightans[i] == answers[i]):
      answerText = answerText + "\nPareizi\n"+str((i)+1)+". jautājums: \nJūsu atbilde: " + str(answers[i]) + "\nPareizā atbilde: " + str(rightans[i])
      points = points + 1
    else:
      answerText = answerText + "\nNepareizi\n"+str((i)+1)+" jautājums: \nJūsu atbilde: " + str(answers[i]) + "\nPareizā atbilde: " + str(rightans[i])

  return answerText, points