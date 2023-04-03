
import random

# Функция получения данных от пользователя
def vvod():
    Error=" "
    global kolvo_HKY #Количество НКУ
    global kolvo_KA #Количество КА
    #Присваивание переменным пустого значения
    kolvo_HKY = None
    kolvo_KA = None

    #Цикл выполняется до тех пор,
    # пока все данные не будут введены без ошибок
    while Error != "no":
        try:
            #Ввод данных
            if (kolvo_HKY == None and kolvo_KA==None):
                kolvo_HKY = int(input("Введите количество НКУ "))
                kolvo_KA = int(input("Введите количество КА "))

            elif kolvo_HKY==None:
                kolvo_HKY = int(input("Введите количество НКУ "))

            elif kolvo_KA==None:
                kolvo_KA = int(input("Введите количество КА "))

            #Количество КА должно быть не больше 26,
            #так мы решили именовать КА буквами английского алфавита
            elif (kolvo_KA>26):
                print("Количество КА должно быть не больше 26")
                kolvo_KA = int(input("Введите количество КА "))

            elif kolvo_KA<=1:
                print("Количество КА должно быть больше 1")
                kolvo_KA = int(input("Введите количество КА "))

            #Корректный ввод данных
            elif (type(kolvo_HKY)==int and type(kolvo_KA)==int
                  and kolvo_KA<=26 and kolvo_KA>1):
                Error = "no"
        #Вызов исключения или ошибки????
        except ValueError:
            print("Данные введены не корректно! "
                  "Количество НКУ и КА должны быть целыми числами!")

    return kolvo_HKY, kolvo_KA

# Создание массива для хранения номеров НКУ
def name_1(kolvo_HKY):
    #Объявление массива
    name_HKY=[]

    #НКУ номеруются по порядку, начиная с 1
    for i in range(kolvo_HKY):
        name_HKY.append(i+1)
    return name_HKY


# Создание массива для хранения названия КА
def name_2(kolvo_KA):
    # Объявление массива
    name_KA = []
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F',
                'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z']

    #Добавление имен КА в массив
    for i in range(kolvo_KA):
        name_KA.append(alphabet[i])
    return name_KA


# Время сеанса КА
def time_session_KA(kolvo_KA):
    #Объявление массива для хранения времени сеанса КА
    time_session=[]
    #Начальный показатель времени
    minute=15

    for i in range(kolvo_KA):
        #Секунды сеанса задаются рандомным образом
        second = random.randint(1, 59)
        #Время в секундах
        time=minute*60+second
        #Время сессии
        time_session.append(time)
        minute+=1

    return time_session


def day(kolvo_HKY, kolvo_KA, time_session):
    # Количество сеансов в сутки
    KOLVO_SESSION = 50

    # Массивы, хранящие объекты в зоне отдыха
    relax_KA=[]
    relax_HKY=[]

    # Массив, хранящий время, до которого КА отдыхает
    relax_KA_time = []

    # Массив, хранящий время, до которого НКУ отдыхает
    relax_HKY_time = []

    # Время в данный момент
    time_now=random.randint(1,1800) #Время от 1 секунды до 30 минут
    time_start=0
    time_finish=0

    # Создание массива, хранящего данные расписания
    spisok = []

    for i in range(KOLVO_SESSION):
        # Выбор КА для управления
        Err = None
        while Err != "no":
            kolvo_error = 0
            KA_now = random.choice(name_2(kolvo_KA))
            # Проверка на то, что КА не в зоне отдыха
            for i in range(len(relax_KA)):
                if relax_KA[i] == KA_now:
                    # Ошибка! Этот КА в зоне отдыха
                    kolvo_error += 1

            if kolvo_error == 0:
                Err = "no"

        # Выбор HKY для управления
        Err = None
        while Err != "no":
            kolvo_error = 0
            HKY_now = random.choice(name_1(kolvo_HKY))
            # Проверка на то, что НКУ не в зоне отдыха
            for i in range(len(relax_HKY)):
                if relax_HKY[i] == HKY_now:
                    # Ошибка! Этот НКУ в зоне отдыха
                    kolvo_error += 1

            if kolvo_error == 0:
                Err = "no"

        # ВРЕМЯ СТАРТА И ФИНИША

        # Обновление переменных времени
        time_start = time_now
        i=0
        while KA_now == name_2(kolvo_KA):
            i+=1
        time_finish = time_start + time_session[1]
        time_now = time_finish + random.randint(-3600, 3600)

        # Преобразование времени старта
        hour_start = time_start // 3600  # Время в часах
        #Делаем время в виде двух цифр
        if hour_start < 10:
            hour_start = str(hour_start)
            hour_start = '0' + hour_start
        ostatok = time_start % 3600
        minute_start = ostatok // 60  # Время в минутах
        if minute_start < 10:
            minute_start = str(minute_start)
            minute_start = '0' + minute_start
        ostatok = ostatok % 60
        second_start = ostatok
        if second_start < 10:
            second_start = str(second_start)
            second_start = '0' + second_start

        #Запись строки вида 00:00:00
        time_start_formatted = str(hour_start) + ":" + str(minute_start) + ":"+ str(second_start)

        # Преобразование времени финиша
        hour_finish = time_finish // 3600  # Время в часах
        if hour_finish < 10:
            hour_finish = str(hour_finish)
            hour_finish = '0' + hour_finish
        ostatok = time_finish % 3600
        minute_finish = ostatok // 60  # Время в минутах
        if minute_finish < 10:
            minute_finish = str(minute_finish)
            minute_finish = '0' + minute_finish
        ostatok = ostatok % 60
        second_finish = ostatok
        if second_finish < 10:
            second_finish = str(second_finish)
            second_finish = '0' + second_finish

        time_finish_formatted = str(hour_finish) + ":" + str(minute_finish) + ":" + str(second_finish)

        # ЗАПИСЬ ДАННЫХ В СПИСОК

        spisok.append(KA_now)
        spisok.append(HKY_now)
        spisok.append(time_start_formatted)
        spisok.append(time_finish_formatted)


        # ЗАНЕСЕНИЕ ОБЪЕКТОВ В ЗОНУ ОТДЫХА

        # Занесение КА в зону отдыха
        relax_KA.append(KA_now)

        # До скольки отдыхает данный КА
        time_relax = time_finish + 3600  # Время отдыха не менее 1 часа
        relax_KA_time.append(time_relax)

        # Занесение НКУ в зону отдыха
        relax_HKY.append(HKY_now)

        # До скольки отдыхает данный КА
        time_relax = time_finish + 9000  # Время отдыха не менее 2.5 часов
        relax_HKY_time.append(time_relax)

        # УДАЛЕНИЕ ОБЪЕКТОВ ИЗ ЗОН ОТДЫХА

        # Удаление КА из зоны отдыха
        # Обновление массива индексов для удаления
        index_delete = []
        for i in range(len(relax_KA_time)):
            if relax_KA_time[i] < time_now:
                index_delete.append(i)

        # Удаление КА
        relax_KA_time.pop(i)
        relax_KA.pop(i)

        # Удаление НКУ из зоны отдыха
        # Обновление массива индексов для удаления
        index_delete = []
        for i in range(len(relax_HKY_time)):
            if relax_HKY_time[i] < time_now:
                index_delete.append(i)

        # Удаление НКУ
        relax_HKY_time.pop(i)
        relax_HKY.pop(i)

    return spisok


def formatted_100(spisok):
    probel1 = "      "
    probel2 = "                   "
    probel3 = "                          "

    liner = []

    for i in range(0,200,4):
        l = probel1 + str(spisok[i]) + probel2 + \
                  str(spisok[1+i]) + probel3 + \
                  str(spisok[2+i]) + probel3 + str(spisok[3+i])
        liner.append(l)


    return liner


if __name__=="__main__":
    vvod()
    formatted_100(day(kolvo_HKY, kolvo_KA, time_session_KA(kolvo_KA)))


