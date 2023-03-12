import tkinter as tk
import math


root = tk.Tk()
root.title('Calculator')
root.configure(bg='#FFEBCD')
root.resizable(width=False, height=False)


ent_field = tk.Entry(root, bg='#D3D3D3', fg='#000080', font=('Arial', 35),
                     borderwidth=5, justify="right")
ent_field.grid(row=0, columnspan=10, padx=5, pady=5,
               sticky='n'+'s'+'e'+'w')
ent_field.insert(0, '0')

FONT = ('Arial', 20, 'bold')


class SC_Calculator():
    def __init__(self):
        self.current = ''
        self.inp_value = True
        self.result = False

    def Entry(self, value):
        ent_field.delete(0, 'end')
        ent_field.insert(0, value)

    def Enter_Num(self, num):
        self.result = False
        firstnum = ent_field.get()
        secondnum = str(num)
        if self.inp_value:
            self.current = secondnum
            self.inp_value = False
        else:
            self.current = firstnum+secondnum
        self.Entry(self.current)


numberpad = "789456123"
i = 0
button = []
for j in range(1, 4):
    for k in range(3):
        button.append(tk.Button(root, text=numberpad[i], font=FONT,
                                fg="#000000", width=6, height=2,
                                highlightbackground='#ADD8E6', highlightthickness=2))
        button[i].grid(row=j, column=k, sticky='n' +
                       's'+'e' + 'w', padx=3, pady=3)
        button[i]["command"] = lambda x=numberpad[i]: sc_app.Enter_Num(x)
        i += 1



if __name__ == '__main__':

    sc_app = SC_Calculator()

    root.mainloop()
