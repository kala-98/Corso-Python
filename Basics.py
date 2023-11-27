

# title = input("Enter title: ")

# lunghezza = len(title)

# if lunghezza <= 100:

#     print(f"Ottimo! {title} ha una lunghezza di {lunghezza} caratteri")

# else:
#     print(f"Mi spiace stronzo ma è troppo lungo")


# lista = []

# while True:
#     todo = input("Enter a todo: ")
#     lista.append(todo)
#     print(lista)


#passwordCorretta = "12345"
#counter = 0
# while True:

#     domanda = input("Inserisci la password per accedere giovanotto: ")
#     if domanda == passwordCorretta:
#         print("Ottimo lavoro soldato, sei dentro!")
#         break
#     else:
#         print("Lol fai attenzione, riprova!")
#     counter += 1

#     if counter == 5:
#         print("Hey buzzurro guarda che non hai più tentativi")
#         break

# filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentation.txt"]

# for file in filenames:
#     file = file.replace(".", " - ", 1)
#     print(file)



# todos = []

# while True:
#     todo = input("Type add, show, edit, complete or exit: ")
#     todo = todo.strip()
#     match todo:
#         case "add":
#             todo = input("Enter a todo: ") + "\n"
            
#             # recuperiamo eventuali dati precedenti dal file
#             file = open("todos.txt", "r")
#             todos = file.readlines() 
#             # è best practice chiudere il file
#             file.close()

#             # sintassi con il with (non serve più chiudere il file)
            #   with open("todos.txt", "r") as file:
            #       todos = file.readLines()
            
#             todos.append(todo)
            
#             # salviamo i nuovi dati nel file
#             file = open("todos.txt", "w")
#             file.writelines(todos)
#             file.close()
#         case "show":
#             file = open("todos.txt", "r")
#             count = 0
#             todos = file.readlines()
#             file.close()
#             for index, item in enumerate(todos, 1):
#                 item = item.replace("\n", "")
#                 print(f"{index} - {item.strip()}")
#         case "edit":
#             number = int(input("Number of the todo to edit: "))
#             new_todo = input(f"Insert the new activity which is going to replace {todos[number-1]}: ")
#             todos[number - 1] = new_todo
#         case "complete":
#             number = int(input("Number of the todo to complete: "))
#             todos.pop(number-1)
#         case "exit":
#             print("Bye!")
#             break


# contents = ["Inserire nel file 1", "Inserire nel file 2", "Inserire nel file 3"]
# filenames = ["test1.txt", "test2.txt", "test3.txt"]

# for i in range(len(filenames)):
#     #counter = 0
#     for content in contents:
#         scritturaFile = open(filenames[i], "w")
#         scritturaFile.writelines(filenames[i])
#         break



# newMember = input("Add a new member: ") + "\n"
# with open("members.txt", "r") as file:

#     membri = file.readlines()
#     file.close()

# with open("members.txt", "w") as file2:
#     membri.append(newMember)
#     file2.close()
# print(membri)


# date = input("Enter today's date: ") 
# path = "journal/" + date
# lista = []
# rate = input("How do you rate the quality of this day from 1 to 10? ")
# thought = input("Let your thoughts flow: ") + "\n"
# with open(path, "w") as file:
#     file.write(rate + 2 * "\n")
#     file.write(thought)


# password = input("Enter password to check its strength: ")
# length_psw = len(password)
# result = {}

# # check length
# if length_psw >= 8:
#     #result.append(True)
#     result["length"] = True
# else:
#     #result.append(False)
#     result["length"] = False

# # check if it contains a number
# digit = False

# for i in password:
#     if i.isdigit():
#         digit = True
# #result.append(digit)
# result["digits"] = digit

# #check if it has an upper letter
# upper = False

# for i in password:
#     if i.isupper():
#         upper = True
# #result.append(upper)
# result["upper"] = upper

# # count = result.count(True)

# print(result)

# if all(result.value()):
#     print("Strong password")
# else:
#     print("Weak password")

# if count == 3:
#     print("Congrats, your password is very strong!")

# elif count == 2 or count == 1:
#     print("Password is decent but you can improve it")

# else:
#     print("Your password is very unsecure, please change it quickly!")



# def get_average():
#     with open("journal/data.txt", "r") as file:
#         numbers = file.readlines()[1::]
#         list_numbers = [float(number) for number in numbers]
#         result = sum(list_numbers) / len(list_numbers)
#         return result

# avg = get_average()
# print(avg)


# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     massimo = max(grades)
#     minimo = min(grades)
#     message = f"Max {massimo}, Min {minimo}"
#     return message

# print(get_max())

# import time 

# tempo = time.strftime("%H:%M:%S %Y/%m/%d")
# print(tempo)

# import glob 
# # find a pattern
# myfiles = glob.glob("journal/*.txt")
# print(myfiles)


# import csv 

# with open("weather.csv", "r") as file:
#     data = list(csv.reader(file))
   

# cities = []
# temperatures = []
# for row in data[1::]:
#     cities.append(row[0])
#     temperatures.append(row[1])

# # print(cities)
# # print(temperatures)

# city = input("Enter a city: ")

# citta = cities.index(city)
# print(f"The temperature of {cities[citta]} is {temperatures[citta]}")


# import shutil 

# shutil.make_archive("output", "zip", "files")


# import webbrowser
# # simple browser search program
# user_term = input("Enter a search term: ")

# url = "https://www.google.com/search?q="
# webbrowser.open(url + user_term)



