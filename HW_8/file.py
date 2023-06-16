# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна: 
# 1. Выводить данные
# 2. Сохранять данные в текстовом файле
# 3. Поиск определенной записи (Например имя или фамилию человека)
# 4. Возможность изменения и удаления данных.
# 5. Вводить имя или фамилию
                                                                         
path = 'file.txt'

def add_new_contact():
    print("\n Введите данные нового контакта")
    f = open(path,'a', encoding='utf-8')
    try:
        last_name = input('Фамилия: ')
        first_name = input('Имя: ')
        middle_name = input('Отчество: ')
        number_phone = input('Телефон: ')
        f.seek(0)
        f.write(f"\n {last_name} {first_name} {middle_name} {number_phone} ;")
    finally:
        f.close()
        print("\n Информация успешно добавлена в справочник")


def find_info():
    f = open(path,'r', encoding='utf-8')
    try:
        find_contact = input('\n Введите данные для поиска контакта: ')
        f.seek(0)
        full_data = f.read()
        lst1 = full_data.split(";")
        find_cont = list()
        for i in lst1:
            lst2 = i.split()
            for j in lst2:
                if j == find_contact:
                    find_cont.append(i)
        if (find_cont !=  []):
            print("\n В справочнике найдены следующие контакты: ")
            for i in find_cont:
                print(f"{i}", end='')
        elif (find_cont ==  []):
            print("\n В справочнике нет такого контакта!")
    finally:
        f.close()

def change_record(ff,str,str1, p):
    ff = open('file.txt','r+', encoding='utf-8')
    print("Зашел")
    try:
        full_data = ff.readlines()
        ff.seek(0)
        for i in full_data:
            if  (str[1:-1] != i[:-1]):
                if (str[1:-3] != i[:-2]):
                    # print(f" elif2 str {list(str[1:-3])} --> i {list(i[:-2])}")
                    ff.write(i)
            elif (str[1:-1] == i[:-1]):
                i = " " + str1 + " ;\n"
                p = True
                print("Заменилось1")
                ff.write(i)
            if (str[1:-3] == i[:-2]):
                i = " " + str1 + " ;\n"
                p = True
                print("Заменилось2")
                ff.write(i)
        ff.truncate()             
    finally:
        return ff,p

def change_info():
    find_contact = input("\n Введите фамилию или имя или отчество или телефон контакта для внесения изменения: ")
    f = open(path,'r+', encoding='utf-8')
    try:
        f.seek(0)
        full_data = f.read()
        lst1 = full_data.split(";")
        find_cont = list()
        for i in lst1:
            lst2 = i.split()
            for j in lst2:
                if j == find_contact:
                    find_cont.append(i)
        k = 0
        if (find_cont !=  []):
            print("\n В справочнике найдены следующие контакты: ")
            for i in find_cont:
                k += 1 
                print(f"\n {k} {i}", end='')
            nubmer_contact = int(input("\n Выберите пункт контакта для внесения изменения: "))
            change_cont = find_cont[nubmer_contact-1] + ";\n"
            print(f"Будет изменена запись {change_cont}")
            change_cont_after = input("\n Введите корректную запись: ")
            p = False
            f, p = change_record(f,change_cont,change_cont_after,p)
            if p==True:
                print(f"В файле изменена запись: {change_cont} на запись \n {change_cont_after}")
        elif (find_cont ==  []):
            print("\n В справочнике нет такого контакта!")
    finally:
        f.close()

def del_record(ff,str):
    ff = open(path,'r+', encoding='utf-8')
    try:
        full_data = ff.readlines()
        ff.seek(0)
        for i in full_data:
            if  (str[1:] != i):
                if  (str[1:] != i + '\n'):
                    ff.write(i)
        ff.truncate()     
    finally:
        return ff


def delete_info():
    find_contact = input("\n Введите данные контакта для последующего удаления: ")
    f = open(path,'r+', encoding='utf-8')
    try:
        f.seek(0)
        full_data = f.read()
        lst1 = full_data.split(";")
        find_cont = list()
        for i in lst1:
            lst2 = i.split()
            for j in lst2:
                if j == find_contact:
                    find_cont.append(i)
        k = 0
        if (find_cont !=  []):
            print("\n В справочнике найдены следующие контакты: ")
            for i in find_cont:
                k += 1 
                print(f"\n {k} {i}", end='')
            nubmer_contact = int(input("\n Введите номер контакта для немедленного удаления: "))
            del_cont = find_cont[nubmer_contact-1] + ";\n"
            del_record(f,del_cont)
            print(f"Из файла удалена запись: {del_cont}")
        elif (find_cont ==  []):
            print("\n В справочнике нет такого контакта!")
    finally:
        f.close()

def clear_all():
    f = open(path,'r+', encoding='utf-8')
    try:
        f.truncate()
        print("\n Справочник полностью очищен")
    finally:
        f.close()

def read_all():
    f = open(path,'r', encoding='utf-8')
    try:
        full_data = f.read()
        lst1 = full_data.split(";")
        if (lst1 !=  [""]):
            print("Весь справочник")
            for i in lst1:
                print(f"{i}", end='')
        elif (lst1 ==  [""]):
                print("\n Справочник пустой!")
    finally:
        f.close()
        

def main():
    while True:
        print('Телефонный справочник')
        print('1 - добавить новый контакт')
        print('2 - поиск контакта')
        print('3 - изменить контакт')
        print('4 - удалить контакт')
        print('5 - очистить справочник')
        print('6 - показать весь справочник')
        print('7 - выйти')
        menu = int(input('Выберите нужный вариант 1-7: '))
        if menu == 1:
            add_new_contact()
            input("\n Нажмите клавишу Enter для продолжения ...")
        elif menu == 2:
            find_info()
            input("\n Нажмите клавишу Enter для продолжения ...")
        elif menu == 3:
            change_info()
            input("\n Нажмите клавишу Enter для продолжения ...")
        elif menu == 4:
            delete_info()
            input("\n Нажмите клавишу Enter для продолжения ...")
        elif menu == 5:
            clear_all()
            input("\n Нажмите клавишу Enter для продолжения ...")
        elif menu == 6:
            read_all()
            input("\n Нажмите клавишу Enter для продолжения ...")
        elif menu == 7:
            break
main()
