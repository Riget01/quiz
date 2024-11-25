from telebot import TeleBot, types
import random

# Создаем бота
bot = TeleBot("7129058339:AAGg633TgnNaEV192RcG2gMy2ieTnY-z57Y")


# Данные для викторины
questions = [
    {"question": "Какое обещание дано Партнёрам?", 
     "answers": ["Обеспечить будущее кофейной индустрии", "Дорога в успешное будущее", "Делать каждый день лучше для Гостей", "Позитивный вклад в сообщество"], 
     "correct": "Дорога в успешное будущее"},
    {"question": "Что обещано Гостям?", 
     "answers": ["Долгосрочная прибыль", "Обеспечение будущего кофейной индустрии", "Делать каждый их день лучше", "Отдавать больше, чем забирать"], 
     "correct": "Делать каждый их день лучше"},
    {"question": "Кому обещано обеспечить будущее кофейной индустрии?", 
     "answers": ["Партнерам", "Гостям", "Фермерам", "Окружающей среде"], 
     "correct": "Фермерам"},
    {"question": "Какой вклад обещается сообществу?", 
     "answers": ["Долгосрочная прибыль", "Отдавать больше, чем забирать", "Позитивный вклад", "Дорога в успешное будущее"], 
     "correct": "Позитивный вклад"},
    {"question": "Что обещано акционерам?", 
     "answers": ["Обеспечить будущее кофе", "Делать каждый день лучше", "Позитивный вклад", "Долгосрочная прибыль, превосходя ожидания"], 
     "correct": "Долгосрочная прибыль, превосходя ожидания"},
    {"question": "Какое обещание дано окружающей среде?", 
     "answers": ["Делать каждый день лучше", "Дорога в успешное будущее", "Отдавать больше, чем забирать", "Позитивный вклад"], 
     "correct": "Отдавать больше, чем забирать"},
    {"question": "Какую основную задачу выполняет первая звезда в STAR SKILLS?", 
     "answers": ["Уменьшает самоуважение", "Поддерживает и повышает самоуважение", "Игнорирует самоуважение"], 
     "correct": "Поддерживает и повышает самоуважение"},
    {"question": "Что следует делать, чтобы подтвердить услышанное?", 
     "answers": ["Молча слушать", "Проигнорировать информацию", "Слушать и подтверждать услышанное"], 
     "correct": "Слушать и подтверждать услышанное"},
    {"question": "Какой навык подразумевает обращение за помощью?", 
     "answers": ["Изоляция", "Принятие помощи и сотрудничество", "Игнорирование проблем"], 
     "correct": "Принятие помощи и сотрудничество"},
    {"question": "Какое из следующих утверждений верно о STAR SKILLS?", 
     "answers": ["Они не имеют значения в общении", "Они способствуют укреплению доверия и взаимопонимания", "Все три навыка независимы друг от друга"], 
     "correct": "Они способствуют укреплению доверия и взаимопонимания"},
    {"question": "В каком году была основана компания Starbucks?", 
     "answers": ["1965", "1971", "1980", "1990"], 
     "correct": "1971"},
    {"question": "Кто из следующих людей не является одним из создателей Starbucks?", 
     "answers": ["Джерри Болдуин", "Зев Сигл", "Гордон Боукер", "Альфред Пит"], 
     "correct": "Альфред Пит"},
    {"question": "В каком городе был открыт первый магазин Starbucks?", 
     "answers": ["Нью-Йорк", "Сан-Франциско", "Сиэтл", "Лос-Анджелес"], 
     "correct": "Сиэтл"},
    {"question": "Какое значение имеет название 'Starbucks'?", 
     "answers": ["Это имя одного из создателей компании", "Это имя помощника капитана Ахава из книги 'Моби Дик'", "Это слово, обозначающее 'кофе' в древнем языке", "Это название места продажи кофе"], 
     "correct": "Это имя помощника капитана Ахава из книги 'Моби Дик'"},
    {"question": "Каково значение логотипа Starbucks?", 
     "answers": ["Двухвостые сирены убивают людей", "Двухвостые сирены показывают путь морякам, спасая их жизнь", "Логотип не имеет значения", "Двухвостые сирены завлекают моряков в ловушки"], 
     "correct": "Двухвостые сирены показывают путь морякам, спасая их жизнь"},
    {"question": "Кто был первым поставщиком зеленых кофейных зерен для Starbucks?", 
     "answers": ["Джерри Болдуин", "Зев Сигл", "Альфред Пит", "Гордон Боукер"], 
     "correct": "Альфред Пит"}
]

# Сессии пользователей и комнаты для мультиплеера
user_sessions = {}
multiplayer_sessions = {}

# Обработка команды /start
@bot.message_handler(commands=['start'])
def start_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Одиночная игра 🎮", "Мультиплеер 🧑‍🤝‍🧑")
    bot.send_message(message.chat.id, "Добро пожаловать в викторину! Выберите режим игры:", reply_markup=markup)

# Одиночная игра
@bot.message_handler(func=lambda message: message.text == "Одиночная игра 🎮")
def start_singleplayer(message):
    bot.send_message(message.chat.id, "Введите ваше имя:")
    bot.register_next_step_handler(message, get_singleplayer_name)

def get_singleplayer_name(message):
    user_sessions[message.chat.id] = {
        "name": message.text,
        "questions": random.sample(questions, 5),
        "current_index": 0,
        "correct": 0
    }
    send_singleplayer_question(message.chat.id)

def send_singleplayer_question(chat_id):
    session = user_sessions[chat_id]
    if session["current_index"] < len(session["questions"]):
        question = session["questions"][session["current_index"]]
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        for option in question["answers"]:
            markup.add(option)
        bot.send_message(chat_id, question["question"], reply_markup=markup)
    else:
        bot.send_message(chat_id, f"Игра окончена! Вы ответили правильно на {session['correct']} из {len(session['questions'])} вопросов.")
        show_main_menu(chat_id)

@bot.message_handler(func=lambda message: message.chat.id in user_sessions)
def singleplayer_answer(message):
    session = user_sessions[message.chat.id]
    question = session["questions"][session["current_index"]]
    if message.text == question["correct"]:
        session["correct"] += 1
        bot.send_message(message.chat.id, "Верно! ✅")
    else:
        bot.send_message(message.chat.id, f"Неверно! ❌ Правильный ответ: {question['correct']}")
    session["current_index"] += 1
    send_singleplayer_question(message.chat.id)

# Мультиплеер
@bot.message_handler(func=lambda message: message.text == "Мультиплеер 🧑‍🤝‍🧑")
def multiplayer_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Создать комнату 🏠", "Войти в комнату 🚪", "Главное меню")
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Создать комнату 🏠")
def create_room(message):
    bot.send_message(message.chat.id, "Введите ваше имя:")
    bot.register_next_step_handler(message, get_host_name)

def get_host_name(message):
    room_code = str(random.randint(1000, 9999))  # Генерация кода комнаты
    multiplayer_sessions[room_code] = {
        "host": message.chat.id,
        "host_name": message.text,
        "players": [],
        "players_names": {},  # Добавляем поле players_names
        "questions": random.sample(questions, 5),  # Выбираем 5 случайных вопросов
        "current_index": 0,
        "correct": {}
    }
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Главное меню")
    bot.send_message(message.chat.id, f"Комната с кодом {room_code} была создана. Дождитесь игроков.", reply_markup=markup)
    
    # Добавляем кнопку для начала викторины
    start_quiz_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_quiz_markup.add("Начать викторину 🎮")
    
    # Отправляем сообщение с кнопкой "Начать викторину" только хозяину комнаты
    bot.send_message(message.chat.id, "Нажмите 'Начать викторину', когда все игроки будут готовы.", reply_markup=start_quiz_markup)

@bot.message_handler(func=lambda message: message.text == "Войти в комнату 🚪")
def join_room(message):
    bot.send_message(message.chat.id, "Введите код комнаты:")
    bot.register_next_step_handler(message, join_room_code)

def join_room_code(message):
    room_code = message.text
    if room_code in multiplayer_sessions:
        # Запрашиваем имя игрока
        bot.send_message(message.chat.id, "Введите ваше имя:")
        bot.register_next_step_handler(message, join_room_name, room_code)
    else:
        bot.send_message(message.chat.id, "Комната с таким кодом не найдена.")

def join_room_name(message, room_code):
    # Проверяем, не входит ли этот игрок в комнату
    session = multiplayer_sessions[room_code]
    
    # Если игрок уже в комнате
    if message.chat.id in session["players"]:
        bot.send_message(message.chat.id, "Вы уже в этой комнате.")
        return

    # Добавляем игрока в комнату
    session["players"].append(message.chat.id)
    session["correct"][message.chat.id] = 0
    session["players_names"][message.chat.id] = message.text  # Сохраняем имя игрока
    bot.send_message(message.chat.id, f"Вы вошли в комнату с кодом {room_code}. Ждите, пока начнется викторина.")
    
    # Проверяем, если все игроки присоединились
    if len(session["players"]) > 1:  # Минимум два игрока
        # Отправляем сообщение хосту
        bot.send_message(session["host"], "Комната полна! Все игроки могут начать викторину.")
        
        # Отправляем сообщение всем игрокам
        for player in session["players"]:
            if player != session["host"]:  # Игроки получают сообщение о готовности
                bot.send_message(player, "Комната полна, викторина скоро начнется!")

def show_main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Главное меню")
    bot.send_message(chat_id, "Вы завершили игру. Выберите следующее действие:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Начать викторину 🎮")
def start_multiplayer_game(message):
    room_code = None
    for code, session in multiplayer_sessions.items():
        if session["host"] == message.chat.id:
            room_code = code
            break
    
    if not room_code:
        bot.send_message(message.chat.id, "Вы не являетесь хостом ни одной комнаты.")
        return

    session = multiplayer_sessions[room_code]
    session["current_index"] = 0

    # Отправляем первый вопрос всем участникам (кроме хоста)
    send_multiplayer_question(room_code)

    # Отправляем хосту кнопку для управления
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Следующий вопрос ➡️")
    bot.send_message(message.chat.id, "Викторина началась! Нажимайте 'Следующий вопрос' для продолжения.", reply_markup=markup)

def send_multiplayer_question(room_code):
    session = multiplayer_sessions[room_code]
    if session["current_index"] < len(session["questions"]):
        question = session["questions"][session["current_index"]]
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        for answer in question["answers"]:
            markup.add(answer)
        
        # Отправляем вопрос всем игрокам
        for player_id in session["players"]:
            if player_id != session["host"]:
                bot.send_message(player_id, question["question"], reply_markup=markup)
    else:
        # Игра окончена
        end_multiplayer_game(room_code)

@bot.message_handler(func=lambda message: message.text == "Следующий вопрос ➡️")
def next_multiplayer_question(message):
    room_code = None
    for code, session in multiplayer_sessions.items():
        if session["host"] == message.chat.id:
            room_code = code
            break

    if not room_code:
        bot.send_message(message.chat.id, "Вы не являетесь хостом ни одной комнаты.")
        return

    session = multiplayer_sessions[room_code]
    session["current_index"] += 1
    send_multiplayer_question(room_code)


@bot.message_handler(func=lambda message: any(message.chat.id in session["players"] for session in multiplayer_sessions.values()))
def multiplayer_answer(message):
    room_code = None
    for code, session in multiplayer_sessions.items():
        if message.chat.id in session["players"]:
            room_code = code
            break

    if not room_code:
        return

    session = multiplayer_sessions[room_code]
    question = session["questions"][session["current_index"]]

    if message.text == question["correct"]:
        session["correct"][message.chat.id] += 1  # Увеличиваем счетчик правильных ответов
        bot.send_message(message.chat.id, "Верно! ✅")
    else:
        bot.send_message(message.chat.id, f"Неверно! ❌ Правильный ответ: {question['correct']}")


def end_multiplayer_game(room_code):
    session = multiplayer_sessions[room_code]
    scores = "\n".join([f"{session['players_names'][player]}: {score} очков" 
                        for player, score in session["correct"].items()])
    for player in session["players"]:
        bot.send_message(player, f"Игра завершена! Итоги:\n{scores}")
    del multiplayer_sessions[room_code]


bot.polling()