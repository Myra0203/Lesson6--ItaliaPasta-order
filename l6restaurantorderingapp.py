from tkinter import * 

window = Tk() 
window.geometry ("1000x1000")
window.configure(bg="light yellow") 

size = StringVar()
size.set("small") #default value if user doesn't select one



def BillCost():
    fettuccinealfredo = 10
    lasagne = 20
    raviolipasta = 15
    arrabbiata = 18
    spaghetti = 14
    smallsize = 0
    medium = 6
    large = 8
    totalbill = 0
    pastaselection = pastaspinbox.get()
    pastaquantity = pastaquantityspinbox.get()
    pastasize = size.get() #size is the variable that contains the value the user selected
    if pastaselection == "Fettuccine Alfredo": 
        if pastasize == "small":
            bill = smallsize * fettuccinealfredo
            totalbill = bill * pastaquantity
        elif pastasize == "medium":
            bill = medium * fettuccinealfredo
            totalbill = bill * pastaquantity
        elif pastasize == "large":
            bill = large * fettuccinealfredo
            totalbill = bill * pastaquantity
    elif pastaselection == "Lasagne alla Bolognese": 
        if pastasize == "small":
            bill = smallsize * lasagne
            totalbill = bill * pastaquantity
        elif pastasize == "medium":
            bill = medium * lasagne
            totalbill = bill * pastaquantity
        elif pastasize == "large":
            bill = large * lasagne
            totalbill = bill * pastaquantity
    elif pastaselection == "Ravioli": 
        if pastasize == "small":
            bill = smallsize * raviolipasta
            totalbill = bill * pastaquantity
        elif pastasize == "medium":
            bill = medium * raviolipasta
            totalbill = bill * pastaquantity
        elif pastasize == "large":
            bill = large * raviolipasta
            totalbill = bill * pastaquantity
    elif pastaselection == "Pasta all'Arrabbiata": 
        if pastasize == "small":
            bill = smallsize * arrabbiata
            totalbill = bill * pastaquantity
        elif pastasize == "medium":
            bill = medium * arrabbiata
            totalbill = bill * pastaquantity
        elif pastasize == "large":
            bill = large * arrabbiata
            totalbill = bill * pastaquantity
    elif pastaselection == "Spaghetti Cacio e Pepe": 
        if pastasize == "small":
            bill = smallsize * spaghetti
            totalbill = bill * pastaquantity
        elif pastasize == "medium":
            bill = medium * spaghetti
            totalbill = bill * pastaquantity
        elif pastasize == "large":
            bill = large * spaghetti
            totalbill = bill * pastaquantity

    textbox = Text(window,highlightcolor="light yellow",highlightthickness=10,width=40,height=3) 
    textbox.place(x=200,y=550)
    textbox.delete("1.0",END)
    textbox.insert(END, "Your total bill is DHS "+str(totalbill))

    
heading = Label(window, text="Welcome to Italia's Pasta", bg="light green", fg="black", font=("Arial",30)) 
heading.place(x=200,y=100)

bodytext = Label(window, text="Select the type of pasta:", bg= "red", fg="black", font=("Arial", 20)) 
bodytext.place(x=200, y=200)

pastaspinbox = Spinbox(window, values=("Fettuccine Alfredo", "Lasagne alla Bolognese", "Ravioli", "Pasta all'Arrabbiata", "Spaghetti Cacio e Pepe"), bg="white", fg="black" )
pastaspinbox.place(x=200, y=250)

pastaquantityspinbox = Spinbox(window, values=(1,2,3,4,5,6,7,8,9,10), bg="white", fg="black")
pastaquantityspinbox.place(x=200, y=300)

radiolabel = Label(window, text="Select the size of your dish", bg="light green", fg="black", font=("Arial", 20))
radiolabel.place(x=200, y= 350)

radio1 = Radiobutton(window, text="small",variable=size,value="small", bg="light yellow", fg="black")
radio2 = Radiobutton(window, text="medium",variable=size,value="medium", bg="light yellow", fg="black")
radio3 = Radiobutton(window, text="large",variable=size,value="large", bg="light yellow", fg="black")

radio1.place(x=200,y=380)
radio2.place(x=200,y=410)
radio3.place(x=200,y=440)

costbutton=Button(window,text="Calculate Total Bill",bg="red",fg="black", width=20, height=2,command= BillCost()) 
costbutton.place(x=200,y=480)


window.mainloop()