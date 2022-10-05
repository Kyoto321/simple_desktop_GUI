from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')

# Create a new window
app = Tk()


def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row) 


def add_item():
    if part_text.get() == '' or customer_text.get() == '' or retailer_text.get == '' or price_text.get() =='':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    # Inserts into the database
    db.insert(part_text.get(), customer_text.get(),
              retailer_text.get(), price_text.get())
    parts_list.delete(0, END)
    # Inserts into the actual List_box
    parts_list.insert(END, (part_text.get(), customer_text.get(),
                      retailer_text.get(), price_text.get()))
    clear_text()
    populate_list()


#To select the items
def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)
    
        #To automatically fixed data into entries after being selected
        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[1])
        
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        
        retailer_entry.delete(0, END)
        retailer_entry.insert(END, selected_item[3])
        
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
        
    except IndexError:
        pass
    
    
def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()
 

def update_item():
    db.update(selected_item[0], part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    populate_list()

def clear_text():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END) 
    price_entry.delete(0, END)
    
#def clear_item():
 #   print('')
   
    

# Part (widgets)
part_text = StringVar()
part_label = Label(app, text='Part Name', font=('bold', 14), pady=20)
# placement on the GUI using .grid()
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# Customer (widgets)
customer_text = StringVar()
customer_label = Label(app, text='Customer', font=('bold', 14))
# placement on the GUI using .grid()
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# Retailer (widgets)
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer', font=('bold', 14))
# placement on the GUI using .grid()
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

# Price (widgets)
price_text = StringVar()
price_label = Label(app, text='Price', font=('bold', 14), pady=20)
# placement on the GUI using .grid()
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

# Part List (Listbox)
# To set invisible 'border=0'
parts_list = Listbox(app, height=5, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Create Scrollbar
scrollbar = Scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

#Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add Part', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Part', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Part', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

# Populate data
populate_list()


app.title('Part Manager')
app.geometry('500x300')

# Start program
app.mainloop()
