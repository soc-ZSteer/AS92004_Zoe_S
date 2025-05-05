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

answer = input("Enter the number of your answer: ")
if options[int(answer) - 1] == correct_answer:
  print("Correct!\n")
  return True
  else:
    print("Wrong! The correct answer is {correct_answer}.\n")
    return False

#main part of the quiz
print("Welcome to the Russian language and history Quiz!\n")

ready = input("Are you ready to play? (yes/no): ").lower()

if ready != "yes":
  print("Okay, maybe next time!")
else:
  score = 0

# Section 1: Russian Language and Phrases
print("\n--- Section 1: Russian Language and Phrases ---")

#questions and answers
questions = [
  ["What does 'Привет' mean?", ["Goodbye", "Hello", "Please", "Thank you"], "Hello"],
  ["How do you say 'Good morning' in Russian?", ["Добрый день", "Доброе утро", "Спокойной ночи", "Добрый вечер"], "Доброе утро"],
  ["Which of these is the correct word for 'book' in Russian?", ["Книга", "Тетрадь", "Лист", "Стол"], "Книга"],
  ["What is the Russian word for 'thank you'?", ["Пожалуйста", "Спасибо", "Здравствуй", "До свидания"], "Спасибо"],
  ["How do you say 'How are you?' in Russian?", ["Как ты?", "Где ты?", "Что ты делаешь?", "Сколько тебе лет?"], "Как ты?"],
  ["Which word means 'water' in Russian?", ["Молоко", "Сок", "Вода", "Чай"], "Вода"],
  ["What does 'Спасибо' mean?", ["Sorry", "Please", "Thank you", "Excuse me"], "Thank you"],
  ["What does 'До свидания' mean?", ["Good morning", "Goodbye", "Please", "Excuse me"], "Goodbye"],
  ]
  
#Loop through the questions
for question in questions:
  if ask_question(question[0], question[1], question[2]):
    score += 1

#Final score
print("Your final score is: {score}/{len(questions)}")
  
