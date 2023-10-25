
import tkinter
import time
import random
from tkinter import messagebox

game = tkinter.Tk()
game.title('Guessing Gaming')
count = 0  # Initialize the guess count
num = random.randint(0, 100)

Frame1 = tkinter.Frame(game)
Frame1.pack()
Frame2 = tkinter.Frame(game)
Frame2.pack()
Frame3 = tkinter.Frame(game)
Frame3.pack()
Frame4 = tkinter.Frame(game)
Frame4.pack()

Label1 = tkinter.Label(Frame2, text='Guess the random number between 0 and 100:')
Label1.pack()
frame = tkinter.LabelFrame(Frame1, text="test frame")
Label2 = tkinter.Label(Frame3)
Label2.pack()
Label3 = tkinter.Label(Frame4, text="fill it jit")
Label3.pack()
x = 0

# Create a label to display the guess count
count_label = tkinter.Label(game, text=f"Guess Count: {count}")
count_label.pack(side="bottom", anchor="w")


def guess():
    global count  # Use the global count variable
    try:
        value = int(Textbox.get())

        if value > 100 or value < 0:
            Label3(text= "Number is not in a valid range")
        elif value > num and value < 100:
            Label3(text= "Your number is too high")
            count += 1  # Increment the guess count
            count_label.config(text=f"Guess Count: {count}")
        elif value < num and value > 0:
            Label3(text= "Your number is too low")
            count += 1  # Increment the guess count
            count_label.config(text=f"Guess Count: {count}")
        elif value == num:
            count += 1  # Increment the guess count
            Label3(text= f"Congrats, you guessed it right!\nGuess Count: {count}")
            # Update the guess count label
            count_label.config(text=f"Guess Count: {count}")

    except ValueError:
        messagebox.showinfo("Please enter a valid number")


ButtonTest = tkinter.Button(Frame2, text="Click me for test", command=guess)
ButtonTest.pack()
Textbox = tkinter.Entry(Frame2, width=10)
Textbox.pack()

time.sleep(1)
game.mainloop()
