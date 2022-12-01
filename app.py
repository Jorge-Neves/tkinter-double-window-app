import sys
from tkinter import *
import tkinter.messagebox
from io import StringIO
from pages.page01 import page_data_01
from pages.page02 import page_data_02
from pages.page03 import page_data_03
from pages.page04 import page_data_04
from pages.page05 import page_data_05
from pages.page06 import page_data_06
from pages.page07 import page_data_07
from pages.page08 import page_data_08
from pages.page09 import page_data_09
from pages.page10 import page_data_10
from pages.page11 import page_data_11
from pages.page12 import page_data_12
from pages.page13 import page_data_13
from pages.page14 import page_data_14
from pages.page15 import page_data_15

root = Tk()
root.title("Python W3schools")
root.geometry("500x250")

pages_array_1 = [page_data_01,
                 page_data_02,
                 page_data_03,
                 page_data_04,
                 page_data_05,
                 page_data_06,
                 page_data_07,
                 page_data_08,
                 page_data_09]

pages_array_2 = [page_data_10,
                 page_data_11,
                 page_data_12,
                 page_data_13,
                 page_data_14,
                 page_data_15]

current_page = 1

my_text = page_data_01


# function define for
# updating the my_label
# widget content
def update_text():
    # use global variable
    global my_text

    # configure
    myLabel.config(text=my_text)


def decrease_page_number():
    global current_page
    global pages_array_1
    global pages_array_2
    if current_page > 1:
        current_page -= 1
        if current_page < 10:
            for z in pages_array_1:
                if z[6:7] == str(current_page):
                    myLabel.config(text=z)
        if 10 <= current_page <= 15:
            for w in pages_array_2:
                if w[5:7] == str(current_page):
                    myLabel.config(text=w)


def increase_page_number():
    global current_page
    global pages_array_1
    global pages_array_2
    if current_page < 15:
        current_page += 1
        if current_page < 10:
            for z in pages_array_1:
                if z[6:7] == str(current_page):
                    myLabel.config(text=z)
        if 10 <= current_page <= 15:
            for w in pages_array_2:
                if w[5:7] == str(current_page):
                    myLabel.config(text=w)


myFrame = Frame(root)

# create a button widget and attached
# with counter function
myButton1 = Button(myFrame, text="<", command=decrease_page_number)
myButton2 = Button(myFrame, text=">", command=increase_page_number)

# create a Label widget
# Initial Label widget content
myLabel = Label(root, text="Hello GitHub")


myLabel.pack(pady=20)
myFrame.pack(pady=20)
myButton1.pack(side=LEFT)
myButton2.pack(side=RIGHT)

main = Toplevel()
main.title("Python IDE")
main.geometry('800x500')
main.resizable(height=FALSE, width=FALSE)
main.configure(bg='gray')


def clear_text():
    code.delete(1.0, END)


def run_code():
    stdout_new = sys.stdout
    output = sys.stdout = StringIO()
    exec(code.get(1.0, END))
    sys.stdout = stdout_new
    tkinter.messagebox.showinfo('Result', output.getvalue())


sidebar = Frame(main, width=80, height=500, bg='#212121')
sidebar.pack(side=RIGHT)

right_bar = Frame(main, width=720, height=500, bg='#424242')
right_bar.pack(side=LEFT)


btnClear = Button(sidebar, text="Clear", command=lambda: clear_text())
btnClear.place(x=22, y=5)
btnClear.configure(bg='gray')

btnRun = Button(sidebar, text="Run", command=lambda: run_code())
btnRun.place(x=24, y=35)
btnRun.configure(bg='gray')

code = Text(right_bar, font=('arial', 11), fg='white', bg='#424242')
code.configure(width=720, height=500)
code.pack(side=RIGHT)


root.mainloop()