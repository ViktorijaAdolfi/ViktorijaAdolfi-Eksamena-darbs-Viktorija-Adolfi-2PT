import time
import os

def hello():
  print()
  print("      ░█▀▀░█▀█░█▀▄░░░█▀▀░▀█▀░█░█░█░░░█▀▀░░░░  ░█▀█░█░█░▀█▀░█░█░█▀█░█▀█  ")
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

def get_valid_name():
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
  print("Kurš no šiem ir pareizs cikls ar skaitītāju Python valodā, kas izdrukā skaitļus no 1 līdz 5?")
  print("  A) for i in range(5): print(i)\n  B) for i in range(1, 5): print(i)\n  C) for i in range(1, 6): print(i - 1)\n  D) for i in range(1, 6): print(i)\n")

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
  print("Kurš no šiem ir pareizs cikls ar skaitītāju Python valodā, kas izdrukā skaitļus no 1 līdz 5?")
  print("  A) for i in range(5): print(i)\n  B) for i in range(1, 5): print(i)\n  C) for i in range(1, 6): print(i - 1)\n  D) for i in range(1, 6): print(i)\n")

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
  print("Kurš no šiem ir pareizs cikls ar skaitītāju Python valodā, kas izdrukā skaitļus no 1 līdz 5?")
  print("  A) for i in range(5): print(i)\n  B) for i in range(1, 5): print(i)\n  C) for i in range(1, 6): print(i - 1)\n  D) for i in range(1, 6): print(i)\n")

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
  print("Kurš no šiem ir pareizs cikls ar skaitītāju Python valodā, kas izdrukā skaitļus no 1 līdz 5?")
  print("  A) for i in range(5): print(i)\n  B) for i in range(1, 5): print(i)\n  C) for i in range(1, 6): print(i - 1)\n  D) for i in range(1, 6): print(i)\n")

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
  print("Kurš no šiem ir pareizs cikls ar skaitītāju Python valodā, kas izdrukā skaitļus no 1 līdz 5?")
  # atbildes
  print("  A) for i in range(5): print(i)\n  B) for i in range(1, 5): print(i)\n  C) for i in range(1, 6): print(i - 1)\n  D) for i in range(1, 6): print(i)\n")

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
  print("Kurš no šiem ir pareizs cikls ar skaitītāju Python valodā, kas izdrukā skaitļus no 1 līdz 5?")
  print("  A) for i in range(5): print(i)\n  B) for i in range(1, 5): print(i)\n  C) for i in range(1, 6): print(i - 1)\n  D) for i in range(1, 6): print(i)\n")

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
  print("Kurš no šiem ir pareizs cikls ar skaitītāju Python valodā, kas izdrukā skaitļus no 1 līdz 5?")
  print("  A) for i in range(5): print(i)\n  B) for i in range(1, 5): print(i)\n  C) for i in range(1, 6): print(i - 1)\n  D) for i in range(1, 6): print(i)\n")

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
  print("Kurš no šiem ir pareizs cikls ar skaitītāju Python valodā, kas izdrukā skaitļus no 1 līdz 5?")
  print("  A) for i in range(5): print(i)\n  B) for i in range(1, 5): print(i)\n  C) for i in range(1, 6): print(i - 1)\n  D) for i in range(1, 6): print(i)\n")

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
  print("Kurš no šiem ir pareizs cikls ar skaitītāju Python valodā, kas izdrukā skaitļus no 1 līdz 5?")
  print("  A) for i in range(5): print(i)\n  B) for i in range(1, 5): print(i)\n  C) for i in range(1, 6): print(i - 1)\n  D) for i in range(1, 6): print(i)\n")

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
    if (rightans[i] == rightans[i]):
      points = points + 1

    if (rightans[i] == rightans[i]):
      answerText = answerText + "\nPareizi\n1. jautājums: \nJūsu atbilde: " + str(
          answers[i]) + "\nPareizā atbilde: " + str(rightans[i])
    elif (rightans[i] != rightans[i]):
      answerText = answerText + "\nNepareizi\n1. jautājums: \nJūsu atbilde: " + str(
          answers[i]) + "\nPareizā atbilde: " + str(rightans[i])

  return answerText


punkti = 0
answers = []
rightans = []
hello()
noteikumi()
username = get_valid_name()
print("Esi sveicināts " + username + "! \nLai tev veicas testā!")
clear5S()
answers.append(jaut1())
answers.append(jaut2())
# checkAnswers(answers)
print(checkAnswers(answers))
