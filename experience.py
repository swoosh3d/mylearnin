easy = {'yellow': 'желтый', 'red': 'красный', 'hello': 'привет', 'bye': 'пока', 'cool': 'круто'}

medium = {'beautyful': 'красивый', 'ugly': 'уродливый', 'stupid': 'глупый', 'light': 'светлый', 'darkness': 'тьма'}

hard = {'butterfly': 'бабочка', 'intellegent': 'интеллегент', 'local': 'локальный', 'important': 'важный', 'retarded': 'отсталый'}

run = True

levels = {
    0: 'откровенно слабо...',
    1: 'ты ведь даже не постарался',
    2: 'жду лучших результатов!',
    3: 'вполне неплохо.',
    4: 'хороший результат',
    5: 'отлично!'
}

answers = {}
while run:
    user_answer = input("Привет! Введи уровень сложности (легкий\средний\сложный): ").lower()

    if user_answer == 'легкий':
        words = easy
    elif user_answer == 'средний':
        words = medium
    elif user_answer == 'сложный':
        words = hard
    else:
        print("не знаю такой сложности")
        
    words_count = len(words)

    print(f'Выбран уровень сложности {user_answer}. Я предложу {words_count} слов, подберите перевод.')

    print("Для продолжения нажмите Enter")
    input()

    for word_en, word_ru in words.items():
        letter_count = len(word_ru)
        first_letter = word_ru[0]
        print(f'{word_en}, {letter_count} букв, начинается на {first_letter}...')
        user_answer = input('Ответ: ').lower()

        if user_answer == word_ru:
            print(f'Верно, {word_en} переводится как {word_ru}')
            answers[word_en] = True
        else:
            print(f'Неверно, {word_en} переводится как {word_ru}') 
            answers[word_en] = False

    correct_words = []
    incorrect_words = []

    for word_en, correct in answers.items():
        if correct:
            correct_words.append(word_en)
        else:
            incorrect_words.append(word_en)

    print('Верные слова:')
    for word in correct_words:
        print(word)

    print('Неверные слова:')
    for word in incorrect_words:
        print(word)

    result = int(len(correct_words))

    print(levels[result])

    repeat = input('Повторишь? да/нет ')
    
    if repeat == 'да':
        run = True
    else:
        break 