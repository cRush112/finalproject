import tkinter as tk
from tkinter import ttk
from Database import Staff 

class Main(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.init_main()

    def init_main(self):
        global refresh
        toolbar = tk.Frame(bd=2, bg='gray') # приборная строка
        toolbar.pack(side='top', fill='x')




        # таблица с записями из базы данных

        self.treeview = ttk.Treeview(self, columns=('id', 'full_name', 'email', 'phone_number', 'salary'), height=45, show='headings') 
        
        self.treeview.column('id', width=100, anchor='center')
        self.treeview.column('full_name', width=250, anchor='center')
        self.treeview.column('email', width=250, anchor='center')
        self.treeview.column('phone_number', width=150, anchor='center')
        self.treeview.column('salary', width=150, anchor='center')
        
        self.treeview.heading('id', text='id')
        self.treeview.heading('full_name', text='ФИО')
        self.treeview.heading('email', text='Email')
        self.treeview.heading('phone_number', text='Номер телефона')
        self.treeview.heading('salary', text='Зарплата')




        # добавление в таблицу записей из базы данных
        
        for staff in Staff().order(): 
            self.treeview.insert('', tk.END, values=staff)

        def refresh():
            self.treeview.delete(*self.treeview.get_children()) # Для начала удаляем все записи
            for staff in Staff().order(): # Берем все записи из бд
                self.treeview.insert('', tk.END, values=staff) # Потом вставляем, таким образом
                                                               # Удаленные, добавленные, измененные сотрудники будут видны 
        
        # таблица с записями из базы данных
        # кнопочки

        self.add_image = tk.PhotoImage(file='E:/питочник/4 модуль/myfinalproject/images/add.png') # Картинка для кнопки
        # Кнопка для вызова окна добавления
        btn_call_add = tk.Button(toolbar, bd=0, bg='green', image=self.add_image,
                                    command=self.open_add, cursor='hand2')
        btn_call_add.pack(side='left')

        self.update_img = tk.PhotoImage(file='E:/питочник/4 модуль/myfinalproject/images/update.png')
        btn_call_update = tk.Button(toolbar, bd=0, bg='green', image=self.update_img,
                                    command=self.open_update, cursor='hand2')
        btn_call_update.pack(side='left')

        self.search_img = tk.PhotoImage(file='E:/питочник/4 модуль/myfinalproject/images/search.png')
        btn_call_search = tk.Button(toolbar, bd=0, bg='blue', image=self.search_img,
                                    command=self.open_search, cursor='hand2')
        btn_call_search.pack(side='right')

        self.refresh_img = tk.PhotoImage(file='E:/питочник/4 модуль/myfinalproject/images/refresh.png')
        btn_call_refresh = tk.Button(toolbar, bd=0, bg='blue', image=self.refresh_img,
                                    command=refresh, cursor='hand2')
        btn_call_refresh.pack(side='right')

        self.delete_img = tk.PhotoImage(file='E:/питочник/4 модуль/myfinalproject/images/delete.png')
        btn_call_delete = tk.Button(toolbar, bd=0, bg='red', image=self.delete_img,
                                    command=self.open_delete, cursor='hand2')
        btn_call_delete.pack(side='top')

        self.treeview.pack(side='left')





    # методы для открытия окон    
    def open_add(self):
        Add()

    def open_update(self):
        Update()

    def open_delete(self):
        Delete()

    def open_search(self):
        Search()
    




# класс диалогового окна для наследования другими классами 
class Child(tk.Toplevel):	
    def __init__(self):
        super().__init__()
        self.geometry('300x200')        
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        
    def init_child(self):
        self.geometry('300x200')        
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()




# классы диалоговых окон для соответсвующих запросов

# Добавление сотрудника
class Add(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_add()

    def init_add(self):
        global add_info, email_entry, salary_entry, phone_number_entry, full_name_entry
        self.configure(bg='#C0C0C0')
        self.title('Добавить')
        self.geometry('400x400')
        add_info = tk.Label(self, bg='#C0C0C0', text='Здесь вы можете добавить сотрудника') # Информация о запросе
        add_info.pack(pady=10, side='top')

        toolbar = tk.Frame(self, bd=10, bg='#C0C0C0')
        toolbar.pack(side='top', fill='x')

        # виджеты и поля для ввода
        full_name_label = tk.Label(toolbar, text='ФИО:')
        full_name_label.pack(anchor='center')
        full_name_entry = tk.Entry(toolbar, cursor='hand2', width=40)
        full_name_entry.pack(anchor='center', pady=10)

        email_label = tk.Label(toolbar, text='Email:')
        email_label.pack(anchor='center')
        email_entry = tk.Entry(toolbar, cursor='hand2', width=40)
        email_entry.pack(anchor='center', pady=10)

        phone_number_label = tk.Label(toolbar, text='Номер телефона:')
        phone_number_label.pack(anchor='center')
        phone_number_entry = tk.Entry(toolbar, cursor='hand2', width=25)
        phone_number_entry.pack(anchor='center', pady=10)

        salary_label = tk.Label(toolbar, text='Зарплата:')
        salary_label.pack(anchor='center')
        salary_entry = tk.Entry(toolbar, cursor='hand2')
        salary_entry.pack(anchor='center', pady=10)
        # виджеты и поля для ввода

        # кнопка для добавления
        add_button = tk.Button(toolbar, command=self.add_staff, text='Добавить', cursor='hand2', bg='green')
        add_button.pack(anchor='center')
    
    # метод для добавления
    def add_staff(self):
        # берём значения из полей для воода
        full_name = full_name_entry.get()
        email = email_entry.get()
        phone_number = phone_number_entry.get()
        salary = int(salary_entry.get())

        # обработка ошибок при выполнении запроса
        try:
            Staff().insert(full_name, email, phone_number, salary)
            add_info.configure(text='Сотрудник успешно добавлен!')
        except Exception as exception:
            add_info.configure(text='Произошла ошибка. Проверьте правильность заполнения полей')

# удаление сотрудника
class Delete(Child):
    def __init__(self):
        super().__init__()
        self.init_delete()

    def init_delete(self):
        global id_for_delete_entry, delete_info
        self.configure(bg='#C0C0C0')
        self.title('Удалить')
        self.geometry('400x400')
        delete_info = tk.Label(self, bg='#C0C0C0', text='Здесь вы можете удалить сотрудника')  # Информация о запросе
        delete_info.pack(pady=10, side='top')

        toolbar = tk.Frame(self, bd=10, bg='#C0C0C0')
        toolbar.pack(side='top', fill='x')
        
        # виджеты и поля для ввода
        id_for_delete = tk.Label(toolbar, text='Введите id сотрудника для удаления:')
        id_for_delete.pack(anchor='center')
        id_for_delete_entry = tk.Entry(toolbar, cursor='hand2')
        id_for_delete_entry.pack(anchor='center', pady=10)

        # кнопка для удаления
        delete_button = tk.Button(toolbar, text='Удалить', bg='red', command=self.delete_staff, cursor='hand2')
        delete_button.pack(anchor='center')

    # метод для удаления
    def delete_staff(self):
        # берём значения из полей для ввода
        id = id_for_delete_entry.get()

        # обработка ошибок при выполнении запроса
        try:
            Staff().delete(id=id)
            delete_info.configure(text='Сотрудник успешно удален')
        except Exception as exception:
            delete_info.configure(text='Произошла ошибка, проверьте правильность заполнения полей')

# изменения данных о сотруднике
class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_update()

    def init_update(self):
        global new_email_entry, new_full_name_entry, new_phone_number_entry, new_salary_entry, id_for_update_entry, update_info
        self.configure(bg='#C0C0C0')
        self.title('Обновить')
        self.geometry('400x400')
        update_info = tk.Label(self, bg='#C0C0C0', text='Здесь вы можете обновить данные сотрудника') # Информация о запросе
        update_info.pack(pady=10, side='top')

        toolbar = tk.Frame(self, bd=10, bg='#C0C0C0')
        toolbar.pack(side='top', fill='x')

        # виджеты и поля для ввода
        id_for_update_label = tk.Label(toolbar, text='Введите id сотрудника для изменения данных:')
        id_for_update_label.pack(anchor='center')
        id_for_update_entry = tk.Entry(toolbar, cursor='hand2')
        id_for_update_entry.pack(anchor='center', pady=10)

        new_full_name_label = tk.Label(toolbar, text='Новые ФИО:')
        new_full_name_label.pack(anchor='center')
        new_full_name_entry = tk.Entry(toolbar, cursor='hand2', width=40)
        new_full_name_entry.pack(anchor='center', pady=10)

        new_email_label = tk.Label(toolbar, text='Новый Email:')
        new_email_label.pack(anchor='center')
        new_email_entry = tk.Entry(toolbar, cursor='hand2', width=40)
        new_email_entry.pack(anchor='center', pady=10)

        new_phone_number_label = tk.Label(toolbar, text='Новый номер телефона:')
        new_phone_number_label.pack(anchor='center')
        new_phone_number_entry = tk.Entry(toolbar, cursor='hand2', width=25)
        new_phone_number_entry.pack(anchor='center', pady=10)

        new_salary_label = tk.Label(toolbar, text='Новая зарплата:')
        new_salary_label.pack(anchor='center')
        new_salary_entry = tk.Entry(toolbar, cursor='hand2')
        new_salary_entry.pack(anchor='center', pady=10)

        # кнопка для изменения
        update_button = tk.Button(toolbar, command=self.update_staff, text='Изменить', cursor='hand2', bg='green')
        update_button.pack(anchor='center')

    def update_staff(self):
        # берём значения из полей для ввода
        id = id_for_update_entry.get()
        full_name = new_full_name_entry.get()
        email = new_email_entry.get()
        phone_number = new_phone_number_entry.get()
        salary = int(new_salary_entry.get())

        # обработка ошибок при выполнении запроса
        try:
            Staff().update(id, full_name, email, phone_number, salary)
            update_info.configure(text='Данные успешно изменены!')
        except Exception as exception:
            update_info.configure(text='Произошла ошибка, проверьте правильность заполнения полей')
            print(exception)

# поиск сотрудника
class Search(Child):
    def __init__(self):
        super().__init__()
        self.init_search()

    def init_search(self):
        global id_search_entry, full_name_search_entry, toolbar, search_info
        self.configure(bg='#C0C0C0')
        self.title('Поиск')
        self.geometry('900x300')
        search_info = tk.Label(self, bg='#C0C0C0', text='Здесь вы можете найти данные о сотруднике')   # Информация о запросе
        search_info.pack(pady=10, side='top')

        toolbar = tk.Frame(self, bd=10, bg='#C0C0C0')
        toolbar.pack(side='top', fill='x')
        
        # виджеты и поля для ввода
        id_search_label = tk.Label(toolbar, text='Введите id сотрудника для поиска:')
        id_search_label.pack(anchor='center')
        id_search_entry = tk.Entry(toolbar, cursor='hand2')
        id_search_entry.pack(anchor='center', pady=10)

        full_name_search_label = tk.Label(toolbar, text='Введите ФИО сотрудника для поиска:')
        full_name_search_label.pack(anchor='center')
        full_name_search_entry = tk.Entry(toolbar, cursor='hand2', width=40)
        full_name_search_entry.pack(anchor='center', pady=10)

        # кнопка для поиска
        search_button = tk.Button(toolbar, command=self.search_staff, text='Найти', cursor='hand2', bg='blue')
        search_button.pack(anchor='center')
    
    # метод для поиска
    def search_staff(self):
        # берём значения из полей для ввода
        id = id_search_entry.get()
        full_name = full_name_search_entry.get()
        
        # данные о сотруднике
        staff_info = Staff().search(full_name, id)
        search_info.configure(text='Сотрудник успешно найден!')
        
        # таблица с данными о сотруднике
        staff_table = ttk.Treeview(self, columns=('id', 'full_name', 'email', 'phone_number', 'salary'), height=45, show='headings') 

        # добавляем столбцы
        staff_table.column('id', width=100, anchor='center')
        staff_table.column('full_name', width=250, anchor='center')
        staff_table.column('email', width=250, anchor='center')
        staff_table.column('phone_number', width=150, anchor='center')
        staff_table.column('salary', width=150, anchor='center')

        # добавляем заголовки
        staff_table.heading('id', text='id')
        staff_table.heading('full_name', text='ФИО')
        staff_table.heading('email', text='Email')
        staff_table.heading('phone_number', text='Номер телефона')
        staff_table.heading('salary', text='Зарплата')

        # добавляем данные о найденном сотруднике в таблицу для вывода
        staff_table.insert('', tk.END, values=staff_info)

        staff_table.pack(side='left')

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('900x450')
    app = Main(window)
    app.pack()
    window.title('Телефонная книга')
    tk.mainloop()