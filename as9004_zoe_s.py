"""
Title: 1.1 AS92004 
By: Zoe Steer
Date: 29/04/25 - 
Version 1
"""

# Ask a question and check the answer
def ask_question(question, options, correct_answer):
    print(question)
    print("1.", options[0])
    print("2.", options[1])
    print("3.", options[2])
    print("4.", options[3])
    
    while True:
        answer = input("Enter the number of your answer (1-4): ")
        if answer in ["1", "2", "3", "4"]:
            break
        else:
            print("Invalid input. Please enter a number from 1 to 4.")
    
if options[int(answer) - 1].lower() == correct_answer.lower():
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer is {correct_answer}.\n")
        return False

# Main part of the quiz
print("Welcome to the Russian Language and History Quiz!\n")

ready = input("Are you ready to play? (yes/no): ").lower()

if ready != "yes":
    print("Okay, maybe next time!")
else:
    score = 0

    # Section 1: Russian language questions
    print("\nSection 1: Russian Language\n")
    
while True:
    ready = input("Are you ready to play? (yes/no): ").strip().lower()
    if ready in ["yes", "no"]:
        break
    print("Please enter 'yes' or 'no'.")

if ready != "yes":
    print("Okay, maybe next time!")
else:
    
    language_questions = [
        ["What does 'Привет' mean?", ["Goodbye", "Hello", "Please", "Thank you"], "Hello"],
        ["How do you say 'Good morning' in Russian?", ["Добрый день", "Доброе утро", "Спокойной ночи", "Добрый вечер"], "Доброе утро"],
        ["Which of these is the correct word for 'book' in Russian?", ["Книга", "Тетрадь", "Лист", "Стол"], "Книга"],
        ["What is the Russian word for 'thank you'?", ["Пожалуйста", "Спасибо", "Здравствуй", "До свидания"], "Спасибо"],
        ["How do you say 'How are you?' in Russian?", ["Как ты?", "Где ты?", "Что ты делаешь?", "Сколько тебе лет?"], "Как ты?"],
        ["Which word means 'water' in Russian?", ["Молоко", "Сок", "Вода", "Чай"], "Вода"],
        ["What does 'Я не понимаю' mean?", ["Sorry", "Please", "I don't understand", "Excuse me"], "I don't understand"],
        ["What does 'До свидания' mean?", ["Good morning", "Goodbye", "Please", "Excuse me"], "Goodbye"],
        ["Which one means 'milk' in Russian?", ["Сок", "Вода", "Чай", "Молоко"], "Молоко"],
        ["How do you say 'good night' in Russian?", ["Доброе утро", "Спокойной ночи", "Добрый вечер", "Здравствуйте"], "Спокойной ночи"]
    ]
    
    for question in language_questions:
        if ask_question(question[0], question[1], question[2]):
            score += 1
    # Section 2: Russian History questions
    print("\nSection 2: Russian History\n")
    history_questions = [
        ["Who was the first Tsar of Russia?", ["Peter the Great", "Nicholas II", "Ivan the Terrible", "Catherine the Great"], "Ivan the Terrible"],
        ["Which year did the Russian Revolution begin?", ["1905", "1914", "1917", "1922"], "1917"],
        ["Who led the Bolsheviks during the October Revolution?", ["Stalin", "Lenin", "Trotsky", "Gorbachev"], "Lenin"],
        ["What was the name of the last Russian emperor?", ["Alexander III", "Nicholas II", "Ivan IV", "Peter II"], "Nicholas II"],
        ["Which event marked the beginning of the Soviet Union?", ["World War I", "The 1917 Revolution", "Cold War", "Fall of the Berlin Wall"], "The 1917 Revolution"],
        ["Who was the leader of the USSR during World War II?", ["Lenin", "Khrushchev", "Stalin", "Gorbachev"], "Stalin"],
        ["What does KGB stand for?", ["Committee for National Affairs", "People’s Secret Police", "Comite for State Security", "Federal Security Bureau"], "Comite for State Security"],
        ["Which Russian leader introduced ‘glasnost’ and ‘perestroika’?", ["Putin", "Brezhnev", "Stalin", "Gorbachev"], "Gorbachev"],
        ["What was the capital city of Russia before Moscow?", ["Kazan", "Stalingrad", "Novgorod", "St Petersburg"], "St Petersburg"],
        ["What year did the Soviet Union officially collapse?", ["1989", "1991", "1993", "2000"], "1991"]
    ]

for question in history_questions:
        if ask_question(question[0], question[1], question[2]):
            score += 1

    # Final score
    total_questions = len(language_questions) + len(history_questions)
    print(f"Your final score is: {score}/{total_questions}")

    
