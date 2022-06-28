from tkinter import *
from translate import Translator

#Translator function
def translate():
    translator= Translator(from_lang=lan1.get(),to_lang=lan2.get())
    translation = translator.translate(var.get())
    var1.set(translation)

#Tkinter root Window with title
root = Tk()
root.title("Translator")

#Creating a Frame and Grid to hold the Content
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S))

mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(ipadx = 50, ipady = 50)
mainframe.pack(padx = 300, pady = 100)

#variables for dropdown list
lan1 = StringVar(root)
lan2 = StringVar(root)
#choices to show in dropdown menu
choices = { 'English','Hindi','Gujarati','Spanish','German'}
#default selection for dropdownlists
lan1.set('English')
lan2.set('Hindi')

#creating dropdown and arranging in the grid
lan1menu = OptionMenu( mainframe, lan1, *choices)
Label(mainframe,text="Select a language",font="segoe 15 bold").grid(row = 0, column = 1,padx=10,pady=10)
lan1menu.grid(row = 1,column =1,ipadx=10,ipady=10,padx=20,pady=10,)

lan2menu = OptionMenu( mainframe, lan2, *choices)
Label(mainframe,text="Select a language",font="segoe 15 bold ").grid(row = 0, column = 2)
lan2menu.grid(row = 1, column =2,padx=20,pady=20,ipadx=10,ipady=10)

#Text Box to take user input
Label(mainframe, text = "Enter Word/Text",font="segoe 10 bold",bg="pink").grid(row=2,column=0,ipadx=10,ipady=10)
var = StringVar()
textbox = Entry(mainframe, textvariable=var).grid(row=2,column=1,ipadx=10,ipady=10)

#textbox to show output
#label can also be used
Label(mainframe, text = "Output",font="segoe 10 bold",bg="pink").grid(row=2,column=2,pady=5,ipadx=20,ipady=10)
var1 = StringVar()
textbox = Entry(mainframe, textvariable=var1,width=20).grid(row=2,column=3,padx=10,ipadx=10,ipady=10)

#creating a button to call Translator function
b=Button(mainframe,text='Translate',font="segoe 8 bold",bg="yellow",command=translate).grid(row=3,column=1,columnspan=2,pady=30,ipadx=20)
root.configure(bg='green')
root.mainloop()