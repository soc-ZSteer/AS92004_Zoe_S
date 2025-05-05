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
    
    answer = input("Enter the number of your answer: ")
    
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
