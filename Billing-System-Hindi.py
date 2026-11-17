import tkinter as tk
from tkinter import messagebox

price = {
    "Mobile":28000,
    "LCD" : 60000,
    "Fridge":38000,
    "Headphones":5000,
    "Microwave":15000
}

def add_to_cart():
    item = choice.get()
    quantityc = int(quantity.get())
    cost = price[item]
    total = quantityc*cost
    bills.insert("end",f"{item}:{quantityc}-{cost}\nTotal = {total}")
def place_order():
    messagebox.showinfo("Order Compleate","Tu mara order cul tak ajaga")



window = tk.Tk()
window.title("Gada Electronics")
window.config(bg = "Sky blue")

label = tk.Label(text="Natu Kaka Station",font=("Comic Sans MS",41))
label.pack(padx=10,pady=10)

mainframe = tk.Frame(window,bg="Black")
mainframe.pack(padx=10,pady=10,fill = "both",expand =True)
left_frame  = tk.Frame(mainframe,bg = "Blue",width=300,height=600)
left_frame.pack(padx=10,pady=10,side="left",fill="y")

right_frame  = tk.Frame(mainframe,bg = "yellow",width=300,height=600)
right_frame.pack(padx=10,pady=10,side="right",fill="both",expand=True) 

#Customer Detalies on Left frame
title1 = tk.Label(left_frame,text = "Custumber Details",font=("Comic Sans MS",20),bg="Blue",fg="White")
title1.grid(row=0,columnspan=4,padx=10,pady=10)

#Item details on right
title2 = tk.Label(right_frame,text = "Item Details",font=("Comic Sans MS",20),bg="Blue",fg="White")
title2.grid(row=0,columnspan=4,padx=10,pady=10)

#Order id

title4 = tk.Label(left_frame,text = "Order ID:",font=("Comic Sans MS",20),bg="Blue",fg="White")
title4.grid(row=1,column=0,padx=10,pady=10)

title5 = tk.Label(left_frame,text = "67",font=("Comic Sans MS",20),bg="grey",fg="black")
title5.grid(row=1,column=1,padx=10,pady=10)


#Name for customber

title3 = tk.Label(left_frame,text = "Apka Ka Nam",font=("Comic Sans MS",20),bg="Blue",fg="White")
title3.grid(row=2,column=0,padx=10,pady=10)

name = tk.Entry(left_frame,text = "",font=("Comic Sans MS",20),bg="White",fg="Black")
name.grid(row=2,column=1,padx=10,pady=10)

#Phone Number

title6 = tk.Label(left_frame,text = "Apka Ka number",font=("Comic Sans MS",20),bg="Blue",fg="White")
title6.grid(row=3,column=0,padx=10,pady=10)

phone = tk.Entry(left_frame,text = "",font=("Comic Sans MS",20),bg="White",fg="Black")
phone.grid(row=3,column=1,padx=10,pady=10)

#Items on right frame

title7 = tk.Label(right_frame,text = "App kon sae Electronic careed karaga",font=("Comic Sans MS",20),bg="Blue",fg="White")
title7.grid(row=1,column=0,padx=10,pady=10)

choice = tk.StringVar(right_frame)
choice.set("Mobile")
options = ["Mobile","LCD","Fridge","Headphone","Microwave"]
menu = tk.OptionMenu(right_frame,choice,*options)
menu.grid(row=1,column=1,pady=10,padx=10)
menu.config(width=50,font=("Comic Sans MS",20))

#Quantity

title8 = tk.Label(right_frame,text = "Quantity",font=("Comic Sans MS",20),bg="Blue",fg="White")
title8.grid(row=2,column=0,padx=10,pady=10)

quantity = tk.Entry(right_frame,text = "",font=("Comic Sans MS",20),bg="White",fg="Black")
quantity.grid(row=2,column=1,padx=10,pady=10)

#add to cart

button1 = tk.Button(right_frame,text = "Add To Cart",font=("Comic Sans MS",20),command=add_to_cart)
button1.grid(row=3,columnspan=2,padx=10,pady=10)

billsframe = tk.Frame(window,bg="Green",width=300,height=600)
billsframe.pack(pady=10)
bills = tk.Text(billsframe,width=50,height=10)
bills.pack(fill="both")

#place order button

button2 = tk.Button(window,text = "Place Order",font=("Comic Sans MS",20),command=place_order)
button2.pack(pady=10)

window.mainloop()

