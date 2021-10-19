from tkinter import *
from tkinter import messagebox
def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        tk.destroy()
tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("КОМПЛИМЕНТЫ")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=1000, height=600, bg="pink", highlightthickness=0)
canvas.pack()
def start_window_1():
    import telebot
    import random 
    bot = telebot.TeleBot("1751574264:AAGA4ls4j-5dx3cEqsiMTqZ1o96I7iH2X1E")
    from telegram.ext import Updater
    def message_handler():
     chat_id='652837347'
     updater=Updater("1751574264:AAGA4ls4j-5dx3cEqsiMTqZ1o96I7iH2X1E",use_context=True)
     a = ["Твои глаза и улыбка просто обворожительны","Ты умница! Ты красавица! ...","Все девушки—ангелы. Но ты особенный ангел!","У меня нет слов, чтобы выразить восхищение! Ты меня обезоружила!","Ты — моя сладкая конфетка! Я превращаюсь в сладкоежку…","Ты выглядишь как супер-модель перед важной фотосессией!","Блеск! Потрясающе! Превосходно выглядишь!","Такое ощущение, что в твоих милых руках сосредоточена доброта: от твоих прикосновений становится тепло и уютно.","Ты очень вкусно пахнешь","Я очень сильно ценю тебя.","Мне очень нравятся твои причуды.","Ты заслуживаешь объятия прямо сейчас.","С тобой мне всегда очень комфортно.","Ты как магнит притягиваешь к себе.","Ты важна для меня"]
     updater.bot.send_message(chat_id=chat_id,text=random.choice(a))
    if __name__ == '__main__':
     message_handler()
b0 = Button(tk,width=50, height=20, bg="red",text="Сделать комплимент", command=start_window_1)
b0.place(x=300, y=150)
tk.mainloop()
