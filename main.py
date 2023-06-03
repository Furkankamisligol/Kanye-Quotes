from tkinter import *
import requests


def get_quote():
    quote = requests.get(url="https://api.kanye.rest")
    quote.raise_for_status()
    kanye_quote = quote.json()["quote"]
    canvas.itemconfig(quote_text, text=f"{kanye_quote}")



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=460, height=620)
background_img = PhotoImage(file="background.png")
canvas.create_image(230, 310, image=background_img)
quote_text = canvas.create_text(230, 310, text="", width=400, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()