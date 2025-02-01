#python quiz game
questions = ("How many elements are on the periodic table?: ",
            "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
            "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

Options = (("A. 118 " ,"B. 260" ,"C. 71 " ,"D. 140 " ),
           ("A. Peacock " ,"B. Ostrich " ,"C. Shark " ,"D. Eagle" ),
           ("A. Oxygen " ,"B. Greenhouse gas " ,"C. Nitrogen " ,"D. Hydrogen " ),
           ("A.206 " ,"B. 355 " ,"C. 158" ,"D. 237 " ),
           ("A. Mars" ,"B. Saturn" ,"C. Uranus" ,"D. Venus" ),)

answers = ("A", "B", "C", "A", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
  print("--------------------")
  print(question)
  for option in Options[question_num]:
    print(option)

  guess = input("Enter (A, B, C, D): ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    score += 1
    print("CORRECT")
    print("Current score is: ", (score))
  else:
    print("INCORRECT")
    print("Current score is: ", (score))
    print(f"{answers[question_num]} is the correct answer")
  
  
  question_num += 1

print("-------------------------------")
print("Your final score is:", (score))
print("Thank you for playing!")
