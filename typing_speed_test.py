from tkinter import *
from tkinter import ttk
import time
import random
import difflib

class MainWindow:
    def __init__(self, root):
        self.text = ["The moonlit sky shimmered with a thousand stars, casting a serene glow over the sleeping world.",
                     "Racing against time, the brave firefighter dashed into the burning building to save lives",
                     "A warm cup of cocoa, a cozy blanket, and a good book – the perfect recipe for a relaxing evening",
                     "If life were predictable it would cease to be life, and be without flavor.",
                     "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
                     "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
                     "Life is what happens when you're busy making other plans.",
                     "One day the people that don’t even believe in you will tell everyone how they met you.",
                     "The true meaning of life is to plant trees, under whose shade you do not expect to sit.",
                     "Laughter echoed through the playground as children played, their innocence filling the air with joy."]
        self.speed = 0
        self.accuracy = 0
        self.time_start = 0
        self.time_end = 0
        root.title("Typing Speed Calculator")
        root.minsize(500, 500)
        for row in range(5):
            root.grid_rowconfigure(row, weight=1)
        for col in range(3):
            root.grid_columnconfigure(col, weight=1)
        self.label_text = Label(
            root, text="Welcome to Typing Speed Calculator.", wraplength=500,font=("Courier",13))
        self.label_text.grid(row=0, column=0, columnspan=3,sticky="nsew")

        self.user_text = Text(root,font=("Courier",15))
        self.user_text.grid(column=0, row=1, columnspan =3, sticky="nsew")

        self.btn_start = Button(root, text="Start/Restart", command=self.start,font=("Courier",13))
        self.btn_start.config(bg="green")
        self.btn_start.grid(column=0, row=2, columnspan=1, sticky="nsew")
        self.btn_stop = Button(root, text="Stop", command=self.stop,font=("Courier",13))
        self.btn_stop.config(bg="red")
        self.btn_stop.grid(column=1, row=2, columnspan=1, sticky="nsew")
        self.btn_newtext = Button(root, text="New Text", command=self.new_text,font=("Courier",13))
        self.btn_newtext.config(bg="green")
        self.btn_newtext.grid(column=2, row=2, columnspan=1, sticky="nsew")

        self.label_speed = Label(
            root, text=f"Your typing speed is {self.speed} WPM",font=("Courier",13))

        self.label_speed.grid(row=3, column=0, columnspan=3, sticky="nsew")

        self.label_accuracy = Label(
            root, text=f"Your typing accuracy is {self.speed} %",font=("Courier",13))
        self.label_accuracy.grid(row=4, column=0, columnspan=3, sticky="nsew")

    def start(self):
        self.time_start = time.time()

    def stop(self):
        self.time_end = time.time()
        words = self.label_text.cget("text").split(' ')
        self.speed = round(len(words)/((self.time_end - self.time_start)/60))
        self.label_speed.config(
            text=f"Your typing Speed is {self.speed} WPM")
        self.accuracy = round(difflib.SequenceMatcher(None, self.label_text.cget(
            "text"), self.user_text.get("1.0", 'end-1c')).ratio()*100)
        self.label_accuracy.config(
            text=f"Your typing accuracy is {self.accuracy} %")

    def new_text(self):
        self.label_text.config(
            text=self.text[random.randint(0, len(self.text)-1)])
        self.user_text.delete('1.0', END)


def main():
    root = Tk()
    myapp = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
