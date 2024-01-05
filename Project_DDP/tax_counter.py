import tkinter
from tkinter import ttk


def calculate_cost():
    given_country = cs_tax.get()
    get_tax = next(item for item in data if item['country'] == given_country)[ 'tax']
    given_tax = float(get_tax)

    given_cost = float(cost.get())

    calculated_tax = given_cost*given_tax/100
    calculated_total_cost = given_cost+calculated_tax

    display_tax_value.config(text=calculated_tax)
    total_cost_value.config(text=calculated_total_cost)


root = tkinter.Tk()
root.title('tax Calculator App')
root.geometry('500x250')

cost = tkinter.StringVar()
cs_tax = tkinter.StringVar()
tax = tkinter.StringVar()
total_cost = tkinter.StringVar()
tax = '0'
total_cost = '0'

data = [
    {'country': 'India', 'tax': '18'},
    {'country': 'USA', 'tax': '20'},
    {'country': 'Australia', 'tax': '15'},
    {'country': 'Japan', 'tax': '21'},
    {'country': 'UK', 'tax': '20'},
    {'country': 'Germany', 'tax': '16'},
    {'country': 'Philippines', 'tax': '30'}
]

title = tkinter.Label(root, text='tax Calculator', font=('Arial', 20, 'bold')).place(x=150, y=10)


get_cost_label = tkinter.Label(root, text='Cost : ', font=('Arial', 20, 'bold')).place(x=100, y=70)
get_cost = tkinter.Entry(root, textvariable=cost, width=15).place(x=190, y=80)


get_tax_label = tkinter.Label(root, text='tax(%) : ', font=(
    'Arial', 20, 'bold')).place(x=100, y=110)
get_tax_box = ttk.Combobox(root, values=[item['country'] for item in data], textvariable=cs_tax).place(x=190, y=120)


btn = tkinter.Button(master=root, text='Calculate', fg='green', font=('Arial', 10, 'bold'), command=calculate_cost).place(x=230, y=150)


tax_value = tkinter.Label(root, text='Your tax : ', fg='black', font=('Arial', 15, 'bold')).place(x=30, y=200)
display_tax_value = tkinter.Label(root, text=tax, fg='black', font=('Arial', 15, 'bold'))
display_tax_value.place(x=130, y=200)


total_cost_label = tkinter.Label(root, text='Total cost : ', fg='black', font=('Arial', 15, 'bold')).place(x=250, y=200)
total_cost_value = tkinter.Label(root, text=total_cost, fg='black', font=('Arial', 15, 'bold'))
total_cost_value.place(x=370, y=200)


root.mainloop()
