# AS92004_Zoe_S
1.1 create a computer program
~  ~  ~   ~  ~  ~   ~  ~

"""
Title: 1.1 AS92004 
By: Zoe Steer
Date: 29/04/25 - 
Version 1
"""

#ask a question and check the answer
def ask_question(question, options, correct_answer):
    print(question)
    print("1.", options[0])
    print("2.", options[1])
    print("3.", options[2])
    print("4.", options[3])
    

#main part of the quiz
print("Welcome to the Russian language and history Quiz!\n")

ready = input("Are you ready to play? (yes/no): ").lower()

if ready != "yes":
    print("Okay, maybe next time!")
else:
    score = 0
