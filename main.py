from tkinter import *
from tkinter import messagebox
from calc import UPS_calc
from Excel_creator import excel_create

root = Tk()
root.title("Калькулятор ИБП - Унибелус")
root.iconbitmap("Unibelus_ico.ico")
root.geometry("800x500+600+250")
root.resizable(True, False)


#setting up a menu
mainmenu = Menu(root)
root.config(menu=mainmenu)
helpmenu = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Справка", menu=helpmenu)
helpmenu.add_command(label="О программе", command = lambda : version())

def version():
    message_text = f"Калькулятор ИБП.\n" \
                   f"\nПри возникновении ошибок, сообщите:\nПеревощиков Василий \n+375 29 500-2000 вн. 262 \n262@unibelus.com"
    messagebox.showinfo("О программе", message_text)


############ Setting up the main elements ###################

#labels
label_model = Label(root, text="Модель ИБП", pady=3, justify=RIGHT)
label_UPS_batteries_capacity = Label(root, text="Ёмкость одной аккумуляторной батареи 12В в ИБП, Ач", pady=3, justify=RIGHT)
label_UPS_batteries_num = Label(root, text="Число аккумуляторов 12В в ИБП, шт", pady=3, justify=RIGHT)
label_UPS_ext_model = Label(root, text="Модель аккумуляторного расширения", pady=3, justify=RIGHT)
label_batteries_UPS_ext = Label(root, text="Ёмкость одной АКБ в аккумуляторном расширении, Ач", pady=3, justify=RIGHT)
label_batteries_ext_num = Label(root, text="Число аккумуляторов в расширении, шт", pady=3, justify=RIGHT)
label_UPS_ext_num = Label(root, text="Число аккумуляторных расширений, шт", pady=3, justify=RIGHT)
label_efficiency = Label(root, text="КПД ИБП при работе от батарей, %", pady=3, justify=RIGHT)
label_power = Label(root, text="Нагрузка, Вт:", pady=3, justify=RIGHT)
label_max_power = Label(root, text="Макс. выходная мощность ИБП, Вт:", pady=3, justify=RIGHT)

#placing the lables
label_model.place(relx=0.02, rely=0.05)
label_UPS_batteries_capacity.place(relx=0.02, rely=0.15)
label_UPS_batteries_num.place(relx=0.02, rely=0.25)
label_UPS_ext_model.place(relx=0.02, rely=0.35)
label_batteries_UPS_ext.place(relx=0.02, rely=0.45)
label_batteries_ext_num.place(relx=0.02, rely=0.55)
label_UPS_ext_num.place(relx=0.02, rely=0.65)
label_efficiency.place(relx=0.02, rely=0.75)
label_power.place(relx=0.02, rely=0.85)
label_max_power.place(relx=0.3, rely=0.05)

# #setting up the message field
# label_message = Label(root, fg="green", text="Введите параметры", padx=3)
# label_message.place(relx=0.6, rely=0.075)

#entry fields for Parameters
entry_model = Entry(root)
entry_UPS_batteries_capacity = Entry(root)
entry_UPS_batteries_num = Entry(root)
entry_UPS_ext_model = Entry(root)
entry_batteries_UPS_ext = Entry(root)
entry_batteries_ext_num = Entry(root)
entry_UPS_ext_num = Entry(root)
entry_efficiency = Entry(root)
entry_power = Entry(root)
entry_max_power = Entry(root)

#placing the parameters entry fields
entry_model.place(relx=0.02, rely=0.10, width = 200)
entry_UPS_batteries_capacity.place(relx=0.02, rely=0.20, width = 200)
entry_UPS_batteries_num.place(relx=0.02, rely=0.30, width = 200)
entry_UPS_ext_model.place(relx=0.02, rely=0.40, width = 200)
entry_batteries_UPS_ext.place(relx=0.02, rely=0.50, width = 200)
entry_batteries_ext_num.place(relx=0.02, rely=0.60, width = 200)
entry_UPS_ext_num.place(relx=0.02, rely=0.70, width = 200)
entry_efficiency.place(relx=0.02, rely=0.80, width = 200)
entry_power.place(relx=0.02, rely=0.90, width = 200)
entry_max_power.place(relx=0.33, rely=0.10, width = 50)

#getting the values from the data file
f = open('data.txt', 'r', encoding="utf-8")

entry_model.insert(0,f.readline().replace('\n',''))
entry_UPS_batteries_capacity.insert(0,f.readline().replace('\n',''))
entry_UPS_batteries_num.insert(0,f.readline().replace('\n',''))
entry_UPS_ext_model.insert(0,f.readline().replace('\n',''))
entry_batteries_UPS_ext.insert(0,f.readline().replace('\n',''))
entry_batteries_ext_num.insert(0,f.readline().replace('\n',''))
entry_UPS_ext_num.insert(0,f.readline().replace('\n',''))
entry_efficiency.insert(0,f.readline().replace('\n',''))
entry_power.insert(0,f.readline().replace('\n',''))
entry_max_power.insert(0,f.readline().replace('\n',''))
f.close()

#text window
label_text_field = Label(root, text="Результат расчёта:", pady=3, justify=RIGHT)
label_text_field.place(relx=0.63, rely=0.15)
result_field = Text(root)
result_field.place(relx=0.47, rely=0.2, width = 400, height = 300)


btn = Button(root, text="Выполнить расчёт", width=15, command=lambda: click())
btn.place(relx=0.55, rely=0.90)

btn_create_excel = Button(root, text = "Создать файл Excel", width=15, command=lambda: click_create_excel())
btn_create_excel.place(relx=0.80, rely=0.90)

def click():
    try:
        model = entry_model.get()
        power = float(entry_power.get())
        battery_cap = float(entry_UPS_batteries_capacity.get())
        battery_num = int(entry_UPS_batteries_num.get())
        ext_model = entry_UPS_ext_model.get()
        ext_bat_num = int(entry_batteries_ext_num.get())
        ext_bat_cap = float(entry_batteries_UPS_ext.get())
        ext_num = int(entry_UPS_ext_num.get())
        efficiency = int(entry_efficiency.get())

        #writing velues to file
        write_to_file()

        result = UPS_calc(power, battery_cap, battery_num, ext_bat_num, ext_bat_cap, ext_num, efficiency)
        result_field.delete("0.0", END)
        result_field.insert("0.0",
                            f"Модель ИБП: {model} \n"
                            f"Мощность нагрузки: {power} Вт\n"
                            f"Ёмкость одной АКБ в ИБП: {battery_cap} Ач\n"
                            f"Количество АКБ в ИБП: {battery_num} шт\n"
                            f"Модель аккумуляторного расширения: {ext_model} \n"
                            f"Ёмкость АКБ в аккумуляторном расширении: {ext_bat_cap} Ач\n"
                            f"Число АКБ в аккумуляторном расширении: {ext_bat_num} шт\n"
                            f"Число аккумуляторных расширений: {ext_num} шт\n"
                            f"КПД ИБП: {efficiency} %\n\n"
                            f"Расчётное время автономной работы: {result} мин"
                            )


    except:
        result_field.delete("0.0", END)
        result = 'Ошибка. Проверьте введённые данные'
        result_field.insert("0.0", result)

def click_create_excel():
    try:
        model = entry_model.get()
        power = float(entry_power.get())
        battery_cap = float(entry_UPS_batteries_capacity.get())
        battery_num = int(entry_UPS_batteries_num.get())
        ext_model = entry_UPS_ext_model.get()
        ext_bat_num = int(entry_batteries_ext_num.get())
        ext_bat_cap = float(entry_batteries_UPS_ext.get())
        ext_num = int(entry_UPS_ext_num.get())
        efficiency = int(entry_efficiency.get())
        max_power = int(entry_max_power.get())

    #writing values to file
        write_to_file()

        excel_create(model, power, battery_cap, battery_num, ext_model, ext_bat_num, ext_bat_cap, ext_num, efficiency, max_power)

        result_field.delete("0.0", END)
        result = 'Файл Excel сохранён в каталоге с программой: \n' + model.replace(' ', '_') + '.xlsx'
        result_field.insert("0.0", result)

    except:
        result_field.delete("0.0", END)
        result = f'Ошибка. Проверьте введённые данные'
        result_field.insert("0.0", result)


def write_to_file():
    f = open('data.txt', 'w', encoding="utf-8")
    f.writelines(entry_model.get() + '\n')
    f.writelines(entry_UPS_batteries_capacity.get() + '\n')
    f.writelines(entry_UPS_batteries_num.get() + '\n')
    f.writelines(entry_UPS_ext_model.get() + '\n')
    f.writelines(entry_batteries_UPS_ext.get() + '\n')
    f.writelines(entry_batteries_ext_num.get() + '\n')
    f.writelines(entry_UPS_ext_num.get() + '\n')
    f.writelines(entry_efficiency.get() + '\n')
    f.writelines(entry_power.get() + '\n')
    f.writelines(entry_max_power.get() + '\n')
    f.close()

root.mainloop()