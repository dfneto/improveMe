from tkinter import *
from datetime import date

# ---------------------------- SAVE DAY ------------------------------- #
def save():

    current_day = date.today().strftime("%Y.%m.%d")

    intro = intro_entry.get()
    agradecimento1 = agradecimento1_entry.get()
    agradecimento2 = agradecimento2_entry.get()
    agradecimento3 = agradecimento3_entry.get()

    with open(f"{current_day}.html", "w") as file:
        file.write(f"<title>{current_day} - Diário de gratidão</title>"
                   f"<b>{intro}</b></br>"
                   f"<ul>"
                   f"<li> {agradecimento1}</li>"
                   f"<li> {agradecimento2}</li>"
                   f"<li> {agradecimento3}</li>"
                   f"</ul>")

    intro_entry.delete(0, END)
    agradecimento1_entry.delete(0, END)
    agradecimento2_entry.delete(0, END)
    agradecimento3_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Improve me")
window.config(padx=20, pady=20)


# Labels
agradecimento1_label = Label(text="Agradecimento 1:")
agradecimento1_label.grid(row=1, column=0)
agradecimento2_label = Label(text="Agradecimento 2:")
agradecimento2_label.grid(row=2, column=0)
agradecimento3_label = Label(text="Agradecimento 3:")
agradecimento3_label.grid(row=3, column=0)


# Entries
intro_entry = Entry(width=50)
intro_entry.grid(row=0, column=0, columnspan=3)
agradecimento1_entry = Entry(width=35)
agradecimento1_entry.grid(row=1, column=1, columnspan=2)
agradecimento1_entry.focus()
agradecimento2_entry = Entry(width=35)
agradecimento2_entry.grid(row=2, column=1, columnspan=2)
agradecimento3_entry = Entry(width=35)
agradecimento3_entry.grid(row=3, column=1, columnspan=2)

save_button = Button(text="Add", width=50, command=save)
save_button.grid(row=4, column=0, columnspan=3)

window.mainloop()