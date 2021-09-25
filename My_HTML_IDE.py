from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background='#6699CC')

open_image = ImageTk.PhotoImage(Image.open('open.png'))
save_image = ImageTk.PhotoImage(Image.open('save.png'))
exit_image = ImageTk.PhotoImage(Image.open('exit.jpg'))

label1 = Label(root,text='File Name:')
label1.place(relx=0.28,rely=0.03,anchor=CENTER)

inputFileName = Entry(root)
inputFileName.place(relx=0.5,rely=0.03,anchor=CENTER)

my_text = Text(root,height=35,width=80,bg='white',fg='black')
my_text.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()