from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk,Image
import random
import pickle
import codecs


questions = []
buf = []
f = codecs.open("questions.txt", mode='r')
flag = False
start = False
for line in f:
    if line[-1] == '\n':
        line = line[:-1]
    if flag:
        buf.append(line)
    if line[-1] == '$':
        line = line[:-1]
        if len(buf) > 5:
            raise TypeError
        start = True
        buf.clear()
        buf.append(line)
        flag = True
    if len(buf) == 5:
        questions.append(buf.copy())
        buf.clear()
        flag = False
f.close()


root = Tk()
root.title("Викторина")
root.geometry('1000x400')
root.resizable(False,False)
i = 0
score = 0

'''
questions = [["Что из перечисленного относится к несистематизированному типу мировоззрения?",
              "Мифологическое", "Научное","Религиозное","Философское"],
             ["Кто из философов утверждал: вода не может быть началом всего, так как она не беспредельна?",
              "Анаксимандр","Гераклит","Пифагор","Фалес"],
             ["Кто из философов был основателем атомистики?",
              "Демокрит","Протагор","Аристотель","Сократ"],
             ["Философия схожа с религией в том, что…",
              "Задается радикальными вопросами и имеет уникальный характер","Основывается на иррациональных, недоказуемых тезисах, а не рациональных аргументах","Спасает душу, а не постигает истину","Имеет коллективный, а не индивидуальный характер"],
             ["Интеллектуалы-гуманисты эпохи Ренессанса отличались от интеллектуалов-клириков эпохи Средневековья и интеллектуалов-философов Античности тем, что…",
              "Способствовали формированию национального самосознания и национальной идентичности","Предпочитали не рисковать", "Защищали гуманистические идеалы","Вели богемный образ жизни"],
             ["Чем философские категории отличаются от понятий?",
              "Они имеют предельно общий характер","Они менее определенны и двусмысленны","Они более алогичны, чем понятия","Они имеют менее общий характер"],
             ["Этику Сократа называли интеллектуальной, потому что…",
              "Согласно Сократу, знать добро и быть добрым - одно и то же","Согласно Сократу, добрым может быть только высокоинтеллектуальный человек","Согласно Сократу, добро очень сложно для понимания","Согласно Сократу, разум абсолютное понятие"],
             ["Несубстанциальным дуализмом называется учение, согласно которому…",
              "Создание есть совокупность свойств мозга, не сводимых к его физическим свойствам","субстанция сознания и субстанция мозга взаимодействуют","Сознание есть отличная от мозга субстанция","Субстанции сознания и субстанции мозга не существует"],
             ["Какому философу принадлежит цитата: «Призрак бродит по Европе, призрак коммунизма»",
              "Маркс","Бэкон","Вольтер","Макиавэлли"],
             ["Что относится к одному из основных направлений материализма?",
              "Диалектический","объективный","Идеалистический","Субъективный"],
             ["Что не принято относить к типично человеческим чертам?",
              "Способность сочувствоать","Наличие развитого языка","способность создавать технику","Абстрактное мышление"],
             ["Антидогматический тип мировоззрения, в рамках которого вырабатываются одновременно знания и ценности",
              "Философский","Религиозный","Мифологический","Научный"],
             ["Кто автор произведения «Левиафан»?",
              "Г. Гоббс","Д. Юм","Дж. Локк","Дж. Беркли"],
             ["Что не относится к основным произведениям Канта?",
              "«Опыт о человеческом разуме»","«Критика чистого разума»","«Критик способности суждения»","«Критики практического разума»"],
             ["Кто из философов был основателем спиритуалистической философии?",
              "Беркли","Вольтер","Эпикур","Авенариус"],
             ["Какой тип рациональности дольше всех доминировал в науке?",
              "Классический","Постклассический","Постнеклассический","Неклассический"],
             ["Традиционно человек рассматривался как единство…",
              "Тела, души и духа","Тела, души и разума","Тела и духа","Тела, духа и разума"],
             ["Сколько этапов выделяют в истории позитивизма?",
              "4","1","2","3"],
             ["Кому из философов принадлежит фраза: «Благородный муж следует долгу и закону, Низкий человек думает, как бы получше устроиться и получить выгоду.»",
              "Конфуций","Фрейд","Аристотель","Гегель"],
             ["Кто был учителем Александра Македонского?",
              "Аристотель","Сократ","Платон","Диоген"],
             ["Что из перечисленного характерно для софистов?",
              "все утверждения характерны","являлись платными учителями мудрости","Преподавали риторику","Считали, что истины не существует, есть только знания"],
             ["Кто из философов считал, что вещи следуют из идей?",
              "Платон","Сократ","Аристотель","Фалес"]]
'''

def question_1(quest):
    question = Label(root, text=quest[0], font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text=quest[1], command=lambda: game_true(out_question))
    btn_2 = Button(root, text=quest[2], command=lambda: game_false(out_question))
    btn_3 = Button(root, text=quest[3], command=lambda: game_false(out_question))
    btn_4 = Button(root, text=quest[4], command=lambda: game_false(out_question))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=4)
    btn_3.grid(row=6)
    btn_4.grid(row=8)

    def game_true(out_question):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        out_question()

    def game_false(out_question):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        out_question()

def question_2(quest):
    question = Label(root, text=quest[0], font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text=quest[2], command=lambda: game_false(out_question))
    btn_2 = Button(root, text=quest[1], command=lambda: game_true(out_question))
    btn_3 = Button(root, text=quest[3], command=lambda: game_false(out_question))
    btn_4 = Button(root, text=quest[4], command=lambda: game_false(out_question))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=4)
    btn_3.grid(row=6)
    btn_4.grid(row=8)

    def game_true(out_question):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        out_question()

    def game_false(out_question):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        out_question()

def question_3(quest):
    question = Label(root, text=quest[0], font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text=quest[2], command=lambda: game_false(out_question))
    btn_2 = Button(root, text=quest[3], command=lambda: game_false(out_question))
    btn_3 = Button(root, text=quest[1], command=lambda: game_true(out_question))
    btn_4 = Button(root, text=quest[4], command=lambda: game_false(out_question))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=4)
    btn_3.grid(row=6)
    btn_4.grid(row=8)

    def game_true(out_question):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        out_question()

    def game_false(out_question):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        out_question()

def question_4(quest):
    question = Label(root, text=quest[0], font=("Consolas", 13), anchor=CENTER)
    btn_1 = Button(root, text=quest[2], command=lambda: game_false(out_question))
    btn_2 = Button(root, text=quest[3], command=lambda: game_false(out_question))
    btn_3 = Button(root, text=quest[4], command=lambda: game_false(out_question))
    btn_4 = Button(root, text=quest[1], command=lambda: game_true(out_question))
    question.grid(row=0)
    btn_1.grid(row=2)
    btn_2.grid(row=4)
    btn_3.grid(row=6)
    btn_4.grid(row=8)

    def game_true(out_question):
        global score
        score += 1
        messagebox.showinfo("Поздравляем!", "Правильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        out_question()

    def game_false(out_question):
        global score
        messagebox.showinfo("Ошибка!", "Неправильный ответ! У вас " + str(score) + " очков!")
        question.destroy()
        btn_1.destroy()
        btn_2.destroy()
        btn_3.destroy()
        btn_4.destroy()
        out_question()


def res():
    global score
    question = Label(root, text="Правильных ответов: " + str(score) + " !", font=("Consolas", 15), anchor=CENTER)
    question.grid(row=0)


def mix_questions():
    random.shuffle(questions)


mix_questions()


def out_question():
    global i
    if i < len(questions):
        b = random.choice(range(4))
        if b == 0:
            question_1(questions[i])  # верный ответ первый
            i += 1
        if b == 1:
            question_2(questions[i])  # верный ответ второй
            i += 1
        if b == 2:
            question_3(questions[i])  # верный ответ третий
            i += 1
        if b == 3:
            question_4(questions[i])  # верный ответ четвертый
            i += 1
    else:
        res()
        return

out_question()

root.mainloop()
