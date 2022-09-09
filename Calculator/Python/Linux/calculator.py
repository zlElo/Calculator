import customtkinter

# This Program was created by zlElo
# This Program stays under the GPLv2 Licens
# GitHub: github.com/zlElo

app = customtkinter.CTk()
app.geometry('234x245')
app.title('Calculator')
customtkinter.set_default_color_theme("green")

#The item list (all buttons)
gui_items = list()
button_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                 '+', '-', '*', '/', '=']

calculation = str()


def calcu(value):
    global calculation

    if value == '=':
        global calculation
        calculate(calculation)
        calculation = str()
        return

    calculation = calculation + value
    output_label.configure(text = str(calculation))

# def for deletion button
def Button2Action():
    calculation = str()
    output_label.configure(text = '')
    return

# def for calculating
def calculate(calc):
    try:
        result = eval(calc)
        output_label.configure(text = str(result))

    except Exception as e:
        output_label.configure(text = 'Error') #Error for false input

# Def to create button
def create_button(value):
    button = customtkinter.CTkButton(text=value, padx = 4, pady = 1, command=lambda: calcu(value), width=70)
    button.grid(pady=2)
    gui_items.append(button)


for val in button_values:
    create_button(val)

#Creates the delet Button
button2 = customtkinter.CTkButton(text='Delet', command=Button2Action, width=170, fg_color="red", hover_color="#FF769c").place(x=33, y=205)

#There stays the result
output_label = customtkinter.CTkLabel(text = '')
output_label.grid(row=0, columnspan=10)

column_count = 0
row_count = 1
maximum_columns = 3

for item in gui_items:
    item.grid(row=row_count, column=column_count)

    column_count += 1
    if column_count == maximum_columns:
        column_count = 0
        row_count += 1

app.mainloop()