from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Викторина")
root.geometry("400x200")

score = 0

question = ["Что из перечисленного относится \nк несистематизированному типу мировоззрения?",
            "Кто из философов утверждал: вода не может \nбыть началом всего, так как\n она не беспредельна?",
            "Кто из философов был основателем атомистики?",
            "Философия схожа с религией в том, что…",
            ]

def q_1():
    question = Label(root, text=question[0], font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Научное", command=lambda: game_false(q_2))
    btn_2 = Button(root, text="Религиозное", command=lambda: game_false(q_2))
    btn_3 = Button(root, text="Мифологическое", command=lambda: game_true(q_2))
    btn_4 = Button(root, text="Философское", command=lambda: game_false(q_2))
    question.grid(row=1)
    btn_1.grid(row=2)
    btn_2.grid(row=4)
    btn_3.grid(row=6)
    btn_4.grid(row=8)

    def game_true(q_2):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_2()

    def game_false(q_2):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_2()


def q_2():
    question = Label(root, text=question[1], font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Гераклит", command=lambda: game_false(q_3))
    btn_2 = Button(root, text="Анаксимандр", command=lambda: game_true(q_3))
    btn_3 = Button(root, text="Пифагор", command=lambda: game_false(q_3))
    btn_4 = Button(root, text="Фалес", command=lambda: game_false(q_3))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_3):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_3()

    def game_false(q_3):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_3()


def q_3():
    question = Label(root, text=question[2], font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Протагор", command=lambda: game_false(q_4))
    btn_2 = Button(root, text="Аристотель", command=lambda: game_false(q_4))
    btn_3 = Button(root, text="Сократ", command=lambda: game_false(q_4))
    btn_4 = Button(root, text="Демокрит", command=lambda: game_true(q_4))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_4):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_4()

    def game_false(q_4):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_4()


def q_4():
    question = Label(root, text=question[3], font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Основывается на иррациональных, \nнедоказуемых тезисах, а \nне рациональных аргументах", command=lambda: game_false(q_5))
    btn_2 = Button(root, text="Спасает душу, а не постигает истину", command=lambda: game_false(q_5))
    btn_3 = Button(root, text="Задается радикальными вопросами\n и имеет уникальный характер", command=lambda: game_true(q_5))
    btn_4 = Button(root, text="Имеет коллективный, а не\n индивидуальный характер", command=lambda: game_false(q_5))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_5):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_5()

    def game_false(q_5):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_5()


def q_5():
    question = Label(root, text="Интеллектуалы-гуманисты эпохи Ренессанса\n отличались от интеллектуалов-клириков эпохи\n Средневековья и интеллектуалов-философов\n Античности тем, что…", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Предпочитали не рисковать", command=lambda: game_false(q_6))
    btn_2 = Button(root, text="Способствовали формированию национального\n самосознания и национальной идентичности", command=lambda: game_true(q_6))
    btn_3 = Button(root, text="Защищали гуманистические идеалы", command=lambda: game_false(q_6))
    btn_4 = Button(root, text="Вели богемный образ жизни", command=lambda: game_false(q_6))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_6):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_6()

    def game_false(q_6):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_6()


def q_6():
    question = Label(root, text="Чем философские категории отличаются от \nпонятий?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Они более алогичны, чем понятия", command=lambda: game_false(q_7))
    btn_2 = Button(root, text="Они менее определенны и двусмысленны", command=lambda: game_false(q_7))
    btn_3 = Button(root, text="Они имеют предельно общий характер", command=lambda: game_true(q_7))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)

    def game_true(q_7):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        q_7()

    def game_false(q_7):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        q_7()


def q_7():
    question = Label(root, text="Этику Сократа называли интеллектуальной, \nпотому что", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Согласно Сократу, добрым может быть\n только высокоинтеллектуальный человек", command=lambda: game_false(q_8))
    btn_2 = Button(root, text="Согласно Сократу, знать добро и быть\n добрым - одно и то же", command=lambda: game_true(q_8))
    btn_3 = Button(root, text="Согласно Сократу, добро очень сложно\n для понимания", command=lambda: game_false(q_8))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)

    def game_true(q_8):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        q_8()

    def game_false(q_8):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        q_8()

def q_8():
    question = Label(root, text="Античный космоцентризм - это такая\n онтология…", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Когда в центре космос", command=lambda: game_false(q_9))
    btn_2 = Button(root, text="Когда все, что существует, существует\n в границах чувственно и мысленно\n воспринимаемого космоса", command=lambda: game_true(q_9))
    btn_3 = Button(root, text="Это учение о космосе, который расположен\n в центре вселенной", command=lambda: game_false(q_9))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)

    def game_true(q_9):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        q_9()

    def game_false(q_9):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        q_9()


def q_9():
    question = Label(root, text="Несубстанциальным дуализмом называется\n учение, согласно которому…", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Субстанция сознания и субстанция\n мозга взаимодействуют", command=lambda: game_false(q_10))
    btn_2 = Button(root, text="Сознание есть отличная от\n мозга субстанция", command=lambda: game_false(q_10))
    btn_3 = Button(root, text="Субстанции сознания и субстанции\n мозга не существует", command=lambda: game_false(q_10))
    btn_4 = Button(root, text="Создание есть совокупность свойств\n мозга, не сводимых к его\n физическим свойствам", command=lambda: game_true(q_10))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_10):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_10()

    def game_false(q_10):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_10()


def q_10():
    question = Label(root, text="Что такое индукция?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Рассуждение от общего к частному", command=lambda: game_false(q_11))
    btn_2 = Button(root, text="Рассуждение от частного к общему", command=lambda: game_true(q_11))
    btn_3 = Button(root, text="Рассуждение, основанное на чувствах", command=lambda: game_false(q_11))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)

    def game_true(q_11):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        q_11()

    def game_false(q_11):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        q_11()


def q_11():
    question = Label(root, text="Какому философу принадлежит цитата:\n «Призрак бродит по Европе, \nпризрак коммунизма»", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Бэкон", command=lambda: game_false(q_12))
    btn_2 = Button(root, text="Вольтер", command=lambda: game_false(q_12))
    btn_3 = Button(root, text="Маркс", command=lambda: game_true(q_12))
    btn_4 = Button(root, text="Макиавэлли", command=lambda: game_false(q_12))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_12):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_12()

    def game_false(q_12):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_12()


def q_12():
    question = Label(root, text="Что такое дескриптивность?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Рассмотрение всех явлений по\n аналогии с человеком, растворение \nего в природе", command=lambda: game_false(q_13))
    btn_2 = Button(root, text="Слитность субъективного и объективного,\n идеального и материального", command=lambda: game_false(q_13))
    btn_4 = Button(root, text="Объяснение происходящих событий \nпосредством оперирования символическими\n образами", command=lambda: game_true(q_13))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_4.grid(row=5)

    def game_true(q_13):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_4.destroy()
        q_13()

    def game_false(q_13):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_4.destroy()
        q_13()


def q_13():
    question = Label(root, text="Что относится к одному из \nосновных направлений материализма?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Объективный", command=lambda: game_false(q_14))
    btn_2 = Button(root, text="Диалектический", command=lambda: game_true(q_14))
    btn_3 = Button(root, text="Идеалистический", command=lambda: game_false(q_14))
    btn_4 = Button(root, text="Субъективный", command=lambda: game_false(q_14))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_14):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_14()

    def game_false(q_14):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_14()


def q_14():
    question = Label(root, text="Что не принято относить к типично\n человеческим чертам?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Способность создавать технику", command=lambda: game_false(q_15))
    btn_2 = Button(root, text="Абстрактное мышление", command=lambda: game_false(q_15))
    btn_3 = Button(root, text="Способность сочувствоать", command=lambda: game_true(q_15))
    btn_4 = Button(root, text="Наличие развитого языка", command=lambda: game_false(q_15))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_15):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_15()

    def game_false(q_15):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_15()


def q_15():
    question = Label(root, text="Правильны ли следующие суждения?\n А: тело - это организм \nБ: тело - это символическая система,\n генерируемая культурой", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Верно только А", command=lambda: game_false(q_16))
    btn_2 = Button(root, text="Верно только Б", command=lambda: game_false(q_16))
    btn_3 = Button(root, text="Оба неверны", command=lambda: game_false(q_16))
    btn_4 = Button(root, text="Оба верны", command=lambda: game_true(q_16))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_16):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_16()

    def game_false(q_16):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_16()


def q_16():
    question = Label(root, text="Антидогматический тип мировоззрения,\n в рамках которого вырабатываются \nодновременно знания и ценности", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Научный", command=lambda: game_false(q_19))
    btn_2 = Button(root, text="Мифологический", command=lambda: game_false(q_19))
    btn_3 = Button(root, text="Религиозный", command=lambda: game_false(q_19))
    btn_4 = Button(root, text="Философский", command=lambda: game_true(q_19))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_19):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_19()

    def game_false(q_19):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_19()


def q_19():
    question = Label(root, text="Кто автор произведения «Левиафан»?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Дж. Локк", command=lambda: game_false(q_20))
    btn_2 = Button(root, text="Дж. Беркли", command=lambda: game_false(q_20))
    btn_3 = Button(root, text="Д. Юм", command=lambda: game_false(q_20))
    btn_4 = Button(root, text="Г. Гоббс", command=lambda: game_true(q_20))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_20):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_20()

    def game_false(q_20):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_20()


def q_20():
    question = Label(root, text="Что не относится к основным\n произведениям Канта?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="«Критика чистого разума»", command=lambda: game_false(q_21))
    btn_2 = Button(root, text="«Опыт о человеческом разуме»", command=lambda: game_true(q_21))
    btn_3 = Button(root, text="«Критик способности суждения»", command=lambda: game_false(q_21))
    btn_4 = Button(root, text="«Критики практического разума»", command=lambda: game_false(q_21))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_21):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_21()

    def game_false(q_21):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_21()


def q_21():
    question = Label(root, text="Какое из перечисленных утверждений\n принадлежит Фоме Аквинскому?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Все в мире движется и изменяется", command=lambda: game_false(q_22))
    btn_2 = Button(root, text="У всего существующего есть цель", command=lambda: game_false(q_22))
    btn_3 = Button(root, text="Оба суждения", command=lambda: game_true(q_22))
    btn_4 = Button(root, text="Ни одно суждение", command=lambda: game_false(q_22))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_22):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_22()

    def game_false(q_22):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_22()


def q_22():
    question = Label(root, text="Кто из философов был основателем\n спиритуалистической философии?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Эпикур", command=lambda: game_false(q_23))
    btn_2 = Button(root, text="Беркли", command=lambda: game_true(q_23))
    btn_3 = Button(root, text="Вольтер", command=lambda: game_false(q_23))
    btn_4 = Button(root, text="Авенариус", command=lambda: game_false(q_23))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_23):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_23()

    def game_false(q_23):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_23()


def q_23():
    question = Label(root, text="Какой тип рациональности дольше\n всех доминировал в науке?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Неклассический", command=lambda: game_false(q_24))
    btn_2 = Button(root, text="Постнеклассический", command=lambda: game_false(q_24))
    btn_3 = Button(root, text="Постклассический", command=lambda: game_false(q_24))
    btn_4 = Button(root, text="Классический", command=lambda: game_true(q_24))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_24):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_24()

    def game_false(q_24):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_24()


def q_24():
    question = Label(root, text="Традиционно человек рассматривался\n как единство…", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Тела и духа", command=lambda: game_false(q_26))
    btn_2 = Button(root, text="Тела, духа и разума", command=lambda: game_false(q_26))
    btn_3 = Button(root, text="Тела, души и разума", command=lambda: game_false(q_26))
    btn_4 = Button(root, text="Тела, души и духа", command=lambda: game_true(q_26))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_26):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_26()

    def game_false(q_26):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_26()


def q_26():
    question = Label(root, text="Сколько этапов выделяют в \nистории позитивизма?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="1", command=lambda: game_false(q_27))
    btn_2 = Button(root, text="2", command=lambda: game_false(q_27))
    btn_3 = Button(root, text="3", command=lambda: game_false(q_27))
    btn_4 = Button(root, text="4", command=lambda: game_true(q_27))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_27):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_27()

    def game_false(q_27):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_27()


def q_27():
    question = Label(root, text="Кому из философов принадлежит фраза:\n «Благородный муж следует долгу и закону, \nНизкий человек думает, как бы\n получше устроиться и получить\n выгоду.»", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Аристотель", command=lambda: game_false(q_28))
    btn_2 = Button(root, text="Фрейд", command=lambda: game_false(q_28))
    btn_3 = Button(root, text="Гегель", command=lambda: game_false(q_28))
    btn_4 = Button(root, text="Конфуций", command=lambda: game_true(q_28))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_28):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_28()

    def game_false(q_28):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_28()


def q_28():
    question = Label(root, text="Кто был учителем Александра\n Македонского?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Аристотель", command=lambda: game_true(q_29))
    btn_2 = Button(root, text="Сократ", command=lambda: game_false(q_29))
    btn_3 = Button(root, text="Платон", command=lambda: game_false(q_29))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)

    def game_true(q_29):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        q_29()

    def game_false(q_29):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        q_29()


def q_29():
    question = Label(root, text="Что из перечисленного характерно\n для софистов?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Являлись платными учителями мудрости", command=lambda: game_false(q_30))
    btn_2 = Button(root, text="Преподавали риторику", command=lambda: game_false(q_30))
    btn_3 = Button(root, text="Считали, что истины не существует,\n есть только знания", command=lambda: game_false(q_30))
    btn_4 = Button(root, text="Все утверждения характерны", command=lambda: game_true(q_30))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_30):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_30()

    def game_false(q_30):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_30()



def q_30():
    question = Label(root, text="Что из перечисленного характерно\n для софистов?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Являлись платными учителями мудрости", command=lambda: game_false(q_31))
    btn_2 = Button(root, text="Преподавали риторику", command=lambda: game_false(q_31))
    btn_3 = Button(root, text="Считали, что истины не существует,\n есть только знания", command=lambda: game_false(q_31))
    btn_4 = Button(root, text="Все утверждения характерны", command=lambda: game_true(q_31))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_31):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_31()

    def game_false(q_31):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_31()

def q_31():
    question = Label(root, text="Кто автор произведения 'Этика'?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Б. Спиноза", command=lambda: game_true(q_32))
    btn_2 = Button(root, text="Дж. Локк", command=lambda: game_false(q_32))
    btn_3 = Button(root, text="Д. Юм", command=lambda: game_false(q_32))
    btn_4 = Button(root, text="Г. Гоббс", command=lambda: game_false(q_32))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_32):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_32()

    def game_false(q_32):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_32()

def q_32():
    question = Label(root, text="Наиболее влиятельным и известным российским философом\n на Западе в XX столетии считался:?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="В. В. Розанов", command=lambda: game_false(q_33))
    btn_2 = Button(root, text="Л. И. Шестов", command=lambda: game_false(q_33))
    btn_3 = Button(root, text="В. С. Соловьев", command=lambda: game_false(q_33))
    btn_4 = Button(root, text="Н. А. Бердяев", command=lambda: game_true(q_33))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_33):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_33()

    def game_false(q_33):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_33()

def q_33():
    question = Label(root, text="Какой из философов не принадлежал\n к 1-ой философской школе?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Фалес", command=lambda: game_false(q_34))
    btn_2 = Button(root, text="Анаксимандр", command=lambda: game_false(q_34))
    btn_3 = Button(root, text="Пифагор", command=lambda: game_true(q_34))
    btn_4 = Button(root, text="Анаксимен", command=lambda: game_false(q_34))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_34):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_34()

    def game_false(q_34):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_34()

def q_34():
    question = Label(root, text="К основными чертам эпохи Возрождения относится:", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="гуманизм", command=lambda: game_false(q_35))
    btn_2 = Button(root, text="интерес к общуству", command=lambda: game_false(q_35))
    btn_3 = Button(root, text="возрождение идеала античности", command=lambda: game_false(q_35))
    btn_4 = Button(root, text="все вышеперечисленное", command=lambda: game_true(q_35))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_35):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_35()

    def game_false(q_35):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_35()

def q_35():
    question = Label(root, text="Философ, считавший естественным состоянием\n «войну всех против всех» - это:", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Локк", command=lambda: game_false(q_36))
    btn_2 = Button(root, text="Гоббс", command=lambda: game_true(q_36))
    btn_3 = Button(root, text="Макиавелли", command=lambda: game_false(q_36))
    btn_4 = Button(root, text="Кант", command=lambda: game_false(q_36))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_36):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_36()

    def game_false(q_36):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_36()

def q_36():
    question = Label(root, text="Дуализм исходит из признания", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="первичности материи", command=lambda: game_false(q_37))
    btn_2 = Button(root, text="первичности сознания", command=lambda: game_false(q_37))
    btn_3 = Button(root, text="наличия 2-х самостоятельных субстанций", command=lambda: game_true(q_37))
    btn_4 = Button(root, text="все вышеперечисленное", command=lambda: game_false(q_37))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_37):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_37()

    def game_false(q_37):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_37()

def q_37():
    question = Label(root, text="Объект и субъект - это:", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="два общающихся человека", command=lambda: game_false(q_38))
    btn_2 = Button(root, text="термины суждения", command=lambda: game_false(q_38))
    btn_3 = Button(root, text="философ и его ученик", command=lambda: game_false(q_38))
    btn_4 = Button(root, text="окружающий мир и познающий человек", command=lambda: game_true(q_38))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(q_38):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_38()

    def game_false(q_38):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        q_38()


def q_38():
    question = Label(root, text="Кто из философов считал, что\n вещи следуют из идей?", font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text="Сократ", command=lambda: game_false(res))
    btn_2 = Button(root, text="Аристотель", command=lambda: game_false(res))
    btn_3 = Button(root, text="Фалес", command=lambda: game_false(res))
    btn_4 = Button(root, text="Платон", command=lambda: game_true(res))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=3)
    btn_3.grid(row=4)
    btn_4.grid(row=5)

    def game_true(res):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        res()

    def game_false(res):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        res()


def res():
    global score
    question = Label(root, text="У вас " + str(score) + " очков!", font=("Consolas", 15), anchor=CENTER)
    question.grid(row=0)


q_1()

root.mainloop()
