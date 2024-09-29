# Quiz Game
print("Fashion Quiz Game")
# Tuple of questions:
questions = ("Who designed Mary Lincoln's 1861-62 purple velvet dress?: ",
             "Which fashion icon from the 1900s encouraged women to dress individually?: ",
             "The Letty Lynton dress was worn by whom?: ",
             "Which dressmaker is credited with the invention of the bias cut?: ",
             "Who was the father of Haute Couture?: ")

# 2D Tuple of options:
options = (("A. ANN LOWE", "B. MAIJA ISOLA", "C. ELIZABETH KECKLEY ", "D. PATRICK KELLY"),
           ("A. DENISE POIRET", "B. EDWARD, PRINCE OF WALES", "C. JOAN CRAWFORD ", "D. ANNA MUTHESIUS"),
           ("A. JOAN CRAWFORD", "B. GINGER ROGERS", "C. MARLENE DIETRICHE", "D. GRETA GARBO"),
           ("A. MADELEINE VIONNET", "B. ELSA SCHIAPARELLI", "C. GABRIELLE CHANEL", "D.  ALIX BARTON"),
           ("A. JEAN PAUL GAULTIER", "B. CHARLES FREDERICK WORTH", "C. CHARLES JAMES", "D. JEAN-PHILIPPE WORTH"))

# Tuple of answers:
answers = ("C", "D", "A", "A", "B")

# List:
guesses = []

# Variables:
score = 0
question_number = 0

# Iterate over tuple of questions:
for question in questions:
    print("--------------------------------------------------")
    print(question)
    for option in options[question_number]: # index operator-> question_number
        print(option) # using options will display  the 2D list of options

# Ask user:
    guess = input("Enter (A, B, C, D):  ").upper() # upper method
    guesses.append(guess) # append method
    if guess == answers[question_number]:
        score +=1
        print("Correct! YAY!!")
    else:
        print("Incorrect!! :( ")
        print(f"{answers[question_number]} is the correct answer") # f-string
# Increment question_number:
    question_number +=1

print("--------------------------------------------------")
print("                     RESULTS                      ")
print("--------------------------------------------------")

# ITERATE:
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# len function
# TYPECAST THE FORMULA:
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%") # f-string

