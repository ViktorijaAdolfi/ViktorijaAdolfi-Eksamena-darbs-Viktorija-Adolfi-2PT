from funkcijas import hello, noteikumi, clear5S, getName, jaut1, jaut2, jaut3, jaut4, jaut5, jaut6, jaut7, jaut8, jaut9, jaut10, checkAnswers


punkti = 0
tekstsss =""
answers = []
rightans = []
hello()
noteikumi()
username = getName()
print("Esi sveicināts " + username + "! \nLai tev veicas testā!")
clear5S()

answers.append(jaut1())
answers.append(jaut2())
answers.append(jaut3())
answers.append(jaut4())
answers.append(jaut5())
answers.append(jaut6())
answers.append(jaut7())
answers.append(jaut8())
answers.append(jaut9())
answers.append(jaut10())
tekstsss, points = checkAnswers(answers) 
print("iegūtie punkti: ",points)
# checkAnswers(answers)
print(tekstsss)
