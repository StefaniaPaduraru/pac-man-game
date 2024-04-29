import tkinter as tk
from PIL import ImageTk, Image
import clips

root = tk.Tk()
root.title("Pac-Man")
root.configure(background="pink")
	

def create_matrix(facts):
    matrix = []
    for i in range(1,12):
        row = []
        for j in range(1,12):
            facts = env.facts()
            perete_fact = None
            for fact in facts:
                if fact.template.name == "este-pe" and fact[0] == j and fact[1] == i and fact[2] == 1:
                    perete_fact = fact
                    break

            if perete_fact:
                image_path = "\\your path\\SBC_perete.jpg"
                image = Image.open(image_path)
                image = image.resize((100, 60))
                photo = ImageTk.PhotoImage(image)

                cell = tk.Label(root, image=photo, width=100, height=60, bg="pink", relief="raised", borderwidth=2)
                cell.image = photo
                cell.grid(row=i, column=j)
                row.append(cell)
            else:
                cell = tk.Label(root, width=14, height=4, bg="pink", relief="ridge", borderwidth=0.5)
                cell.grid(row=i, column=j)
                row.append(cell)
        matrix.append(row)
    return matrix

def create_pacman():
    for i in range(1,12):
        row = []
        for j in range(1,12):
            facts = env.facts()
            pm_fact = None
            for fact in facts:
                if fact.template.name == "este-pe" and fact[0] == j and fact[1] == i and fact[2] == 'PM':
                    pm_fact = fact
                    break
            if pm_fact:
                image_path = "\\your path\\SBC_Pac_Man.png"
                image = Image.open(image_path)
                image = image.resize((60, 60))
                photo = ImageTk.PhotoImage(image)

                cell = tk.Label(root, image=photo, width=100, height=60, bg="pink", relief="raised", borderwidth=2)
                cell.image = photo
                cell.grid(row=i, column=j)
                row.append(cell)

def create_kiwi():
    for i in range(1,12):
        row = []
        for j in range(1,12):
            facts = env.facts()
            kiwi_fact = None
            for fact in facts:
                if fact.template.name == "este-pe" and fact[0] == j and fact[1] == i and fact[2] == 'kiwi':
                    kiwi_fact = fact
                    break
            if kiwi_fact:
                image_path = "\\your path\\SBC_kiwi.png"
                image = Image.open(image_path)
                image = image.resize((60, 60))
                photo = ImageTk.PhotoImage(image)

                cell = tk.Label(root, image=photo, width=100, height=60, bg="pink", relief="raised", borderwidth=2)
                cell.image = photo
                cell.grid(row=i, column=j)
                row.append(cell)
				
def create_fantoma():
    for i in range(1,12):
        row = []
        for j in range(1,12):
            facts = env.facts()
            kiwi_fact = None
            for fact in facts:
                if fact.template.name == "este-pe" and fact[0] == j and fact[1] == i and fact[2] == 'f':
                    kiwi_fact = fact
                    break
            if kiwi_fact:
                image_path = "\\your path\\SBC_fantoma.png"
                image = Image.open(image_path)
                image = image.resize((60, 60))
                photo = ImageTk.PhotoImage(image)

                cell = tk.Label(root, image=photo, width=100, height=60, bg="pink", relief="raised", borderwidth=2)
                cell.image = photo
                cell.grid(row=i, column=j)
                row.append(cell)

def create_bila_alba():
    for i in range(1,12):
        row = []
        for j in range(1,12):
            facts = env.facts()
            kiwi_fact = None
            for fact in facts:
                if fact.template.name == "este-pe" and fact[0] == j and fact[1] == i and fact[2] == 'ba':
                    kiwi_fact = fact
                    break
            if kiwi_fact:
                image_path = "\\your path\\SBC_bila_alba.png"
                image = Image.open(image_path)
                image = image.resize((60, 60))
                photo = ImageTk.PhotoImage(image)

                cell = tk.Label(root, image=photo, width=100, height=60, bg="pink", relief="raised", borderwidth=2)
                cell.image = photo
                cell.grid(row=i, column=j)
                row.append(cell)

def miscari():
    filename = "\\your path\\date.txt"
    with open(filename, "r") as file:
        file_contents = file.read()
        text_widget.insert("1.0", file_contents)


def update_gui(event=None):
    global facts, matrix
    if matrix:
        for row in matrix:
            for cell in row:
                cell.destroy()
	# facts = env.facts()
    matrix = create_matrix(facts)
    create_pacman()
    create_kiwi()
    create_fantoma()
    create_bila_alba()


env = clips.Environment()
env.clear()
env.load("\\your path\\e3.clp")
env.reset()

facts = env.facts()
matrix = create_matrix(facts)
create_pacman()
create_kiwi()
create_fantoma()
create_bila_alba()

root.bind('<KeyPress>', lambda event: update_gui())

text_widget = tk.Text(root, width=32, height=30)
text_widget.grid(row=1, column=13, rowspan=12)
text_widget.configure(font=("Courier New", 15))
miscari()

env.run()

root.quit()
root.mainloop()