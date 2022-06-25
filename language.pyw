from tkinter import *
from tkinter import messagebox

main=Tk()
main.geometry('300x200')
main.title('language choose')

def rus():
    file=open('language.txt', 'w+')
    file.write('rus')
    file.close()
    messagebox.showinfo('выбран язык', 'выбран Русский язык')
    
def eng():
    file=open('language.txt', 'w+')
    file.write('eng')
    file.close()
    messagebox.showinfo('language', 'english language has been added')
    
eng_but=Button(main, text='english', command=eng)
rus_but=Button(main, text='русский', command=rus)
textbox=Label(main, text='choose your language')

textbox.grid(column=0, row=0)
rus_but.grid(column=0, row=1)
eng_but.grid(column=1, row=1)

mainloop()