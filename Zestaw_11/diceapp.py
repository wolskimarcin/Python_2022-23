import tkinter as tk
import random


class DiceApp:
    def __init__(self):
        self.images = None
        self.root = tk.Tk()
        self.root.title("Rzut kostką")
        self.root.geometry("400x200")
        self.label = tk.Label(self.root, text="Kliknij przycisk, aby rzucić kostką")
        self.label.pack()
        self.button = tk.Button(self.root, text="Rzuć", command=self.roll_dice)
        self.button.pack()
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

    def roll_dice(self):
        roll = random.randint(1, 6)
        self.image_label.configure(image=self.images[roll])
        self.label.config(text=f"Wyrzucono: {roll}")

    def run(self):
        self.images = {
            1: tk.PhotoImage(file="dice1.png"),
            2: tk.PhotoImage(file="dice2.png"),
            3: tk.PhotoImage(file="dice3.png"),
            4: tk.PhotoImage(file="dice4.png"),
            5: tk.PhotoImage(file="dice5.png"),
            6: tk.PhotoImage(file="dice6.png")
        }
        self.root.mainloop()


if __name__ == "__main__":
    app = DiceApp()
    app.run()
