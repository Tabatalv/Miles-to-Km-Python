from tkinter import *

def button_clicked():
    miles = float(input.get())
    km = round(miles * 1.609)
    label_result.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")

input = Entry()
input.grid(column=1, row=0)



label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equals = Label(text="is equal to ")
label_equals.grid(column=0, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

label_result = Label(text="0")
label_result.grid(column=1, row=1)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)












window.mainloop()
