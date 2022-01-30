import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# Function for the first tab
def min_divisor_calculation():
    number = int(first_tab_number_entry.get())
    min_dev = 2
    while min_dev <= number:
        if number % min_dev == 0:
            Label(first_tab, text=f'Наименьший делитель: {min_dev}',
                  font=('Verdana', 14, 'bold'),
                  bg='#FFFFC8',
                  width=700,
                  height=5,
                  fg='green'). \
                place(relx=0.5, rely=0.84, anchor=CENTER)
            messagebox.showinfo('Успешно!', f'Ответ: {min_dev}')
            break
        min_dev += 1


# Function for the second tab
def max_degree_calculation():
    number_max_entry = float(second_tab_number_entry.get())
    start_number = 2

    temp_number = start_number
    exponent = 1

    while temp_number * start_number < number_max_entry:
        temp_number *= start_number
        exponent += 1

        Label(second_tab, text=f'Показатель степени: {exponent}\n'
                               f'Максимальная степень числа {start_number}: {temp_number}',
              font=('Verdana', 14, 'bold'),
              bg='#1f104f',
              width=700,
              height=5,
              fg='#15ff15'). \
            place(relx=0.5, rely=0.77, anchor=CENTER)
    messagebox.showinfo('Успешно!', f'Максимальная степень числа {start_number}: {temp_number}')


main_window = Tk()
university_logo = tkinter.PhotoImage(file='VSUET_logo.png')

main_window.title('Практическая работа №6')
main_window.geometry('700x500+200+100')
main_window.configure(bg='#FFFFC8')
main_window.iconphoto(False, university_logo)

tab_menu = ttk.Notebook(main_window)
tab_menu.pack(fill='both', expand=True)


# The first tab
first_tab = ttk.Frame(tab_menu)
tab_menu.add(first_tab, text="Задание №2", )

task_number = tkinter.Label(first_tab, text='Задание №5.2',
                            bg='#FFFFC8',
                            font=('Verdana', 14, 'bold'),
                            fg='#FF4700',
                            width=700,
                            height=2
                            )

task_name = tkinter.Label(first_tab, text='''Дано целое число, не меньшее 2. 
Выведите его наименьший натуральный делитель, отличный от 1.''',
                          bg='white',
                          fg='black',
                          font=('Verdana', 12, 'bold'),
                          padx=10,
                          pady=20,
                          justify='center'
                          )

task_number.pack()
task_name.place(relx=0.5, rely=0.3, anchor=CENTER)

Label(first_tab, text="Введите целое число:", font=('Verdana', 12, 'italic'), ). \
    place(relx=0.5, rely=0.47, anchor=CENTER)

first_tab_number_entry = Entry(first_tab,
                               width=10,
                               bg='#FFFFC8',
                               fg='green',
                               font=('Verdana', 20, 'bold'),
                               justify=CENTER)

first_tab_number_entry.place(relx=0.5, rely=0.55, anchor=CENTER)

Button(first_tab, text='Показать результаты вычислений',
       font=('Verdana', 11),
       command=min_divisor_calculation,
       activebackground='#FFFFC8', ).place(relx=0.5, rely=0.65, anchor=CENTER)


# The second tab
second_tab = ttk.Frame(tab_menu)
tab_menu.add(second_tab, text="Задание №3", )

Label(second_tab, text='''Задание №5.3. По данному натуральному числу N\n найдите наибольшую целую степень двойки, \
не превосходящую N. \nВыведите показатель степени и саму степень. \nОперацией возведения в степень пользоваться \
нельзя!''',
      width=700,
      bg='white',
      fg='black',
      font=['Verdana', 12, 'bold'],
      padx=10,
      pady=20,
      justify='center'
      ).pack()

Label(second_tab, text="Введите  число:", font=('Verdana', 12, 'italic'), ).place(relx=0.5, rely=0.40, anchor=CENTER)

second_tab_number_entry = Entry(second_tab, width=10,
                                bg='#b3daff',
                                font=('Verdana', 20, 'bold'),
                                justify=CENTER)

second_tab_number_entry.place(relx=0.5, rely=0.47, anchor=CENTER)

Button(second_tab, width=50,
       text='Показать результаты вычислений',
       font=('Verdana', 11),
       command=max_degree_calculation,
       activebackground='#b3daff').place(relx=0.5, rely=0.57, anchor=CENTER)

main_window.mainloop()
