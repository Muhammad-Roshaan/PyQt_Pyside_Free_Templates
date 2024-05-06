# print("Hello World")
# A = "Hamza"
# B = 3j
# C = 2 + 3j
# print(type(B))
# Complex = complex(2 ,3)

# print(Complex)

# x,y,z = "Ali"
# print(x , y ,z)
# # print(y)
# # print(z)
# name = ["ali","hamza","saad"]
# s1,s2,s3 = name
# print(s1,s2,s3)

# var1 = "raza"
# var2 = 39
# print(var1 ,var2)

# myRange = range(6)
# print(myRange)

# class2

# userName = input("Enter your name:")
# userAge = input("Enteere your age:")
# userheight = input("Enter your heght:")
# print("The user",userName,"are",userAge,"year old and his height is",userheight)

# inputNumber1 = int(input("Enter Number1:"))
# inputNumber2 = int(input("Enter Number2:"))

# sum = inputNumber1 + inputNumber2
# min = inputNumber1 - inputNumber2
# mul = inputNumber1 * inputNumber2
# div = inputNumber1 / inputNumber2
# Dmul = inputNumber1 ** inputNumber2
# Ddiv = inputNumber1 // inputNumber2
# mod = inputNumber1 % inputNumber2
# print("The sum of given numbers:",sum,"\nThe subtraction is:",min,"\nThe modulous is:",mod,"\nThe multiplication is:",mul,"\nthe devision is:",div,"\nthe Ddevision is:",Ddiv,"\nthe Dmultiplication is:",Dmul)

# a = 2
# b = 4

# a += b
# a -= b
# a *= b
# a /= b
# a == b
# print(a)

# class3


# A = [23,22,21]
# sum = 0
# for item in A:
#     sum += item
# print(sum)

# a = int(input("Enter a number:"))

# if(a % 2==0):
#  print("The given number is even:",a)
# else:
#  print("The given number is odd:",a)

# a = int(input("Enter a number:"))
# def checkEvenOdd(num):
#     if(a % 2==0):
#       print("The given number is even:",a)
#     else:
#       print("The given number is odd:",a)
# checkEvenOdd(a)

# a = int(input("Enter a number:"))
# def checkEvenOdd(num):
#     num = num % 2
#     return num
# if (checkEvenOdd(a) == 0):
#     print("The given number is even:", a)
# else:
#     print("The given number is odd:", a)

# list = [20,10]
# result = []
# for i in range(len(list) - 1):
#     result.append(list[i] / list[i+1])
# print("Result aftrer dividing each item by the next item:",result)

# class4 STRING

# indexing
# name = input("Enter Your Name:")
# print(name[2])
# print(name[2:4])
# print(name[ :5])
# print(name[2: ])

# looping
# for x in "I llove python":
#     print(x)

# # searching
# string = "I am here for Python"
# if "Python" in string:
#     print("\n yes it exist\n")
# else:
#     print("it does not exist")

# # length of string
# print(len(string))

# text = 'it\'s\' my code'
# print(text)

# String-built in functions
# text2 = "My Name is \"Python\".I am here to Code"
# print(text2.capitalize())
# print(text2.casefold())
# print(text2.lower())
# print(text2.upper())
# print(text2.find("is"))
# print(text2.replace("My","is"))
# print(text2.count("a"))
# print(text2.title())
# print(text2.isalnum())
# print(text2.isascii())
# print(text2.isdigit())
# print(text2.isnumeric())
# print(text2.islower())
# print(text2.split())
# print(text2.zfill(40))
# print(text2.swapcase())
# print()

# delete all string
# text2 = "My Name is \"Python\".I am here to Code"
# print(text2)
# del text2

# Listclass5

# list1 = [10, 20, [300, 4000, [500, 6], 500], 30, 40]
# print(list1[2][2][1])

# myList = ["Hamza", "Faseeh", "hello","Raza","amna"]
# # print(myList[3:])

# # myList[2] = "pakistan"
# # print(myList)

# # myList[2:4] = "Ali", "Umar"
# myList.insert(3,"Ahsan")
# print(myList)
# myList.append("Abdullah")
# print(myList)
# myList.remove("amna")
# myList.pop()
# print(myList)
# del myList[2]
# print(myList)
# myList.sort()
# print(myList)
# myList.sort(reverse=True)
# print(myList)

# anotherList = ["Faheem","Ibrahim"]
# myList.extend(anotherList)
# print(myList)

# myList.reverse()
# print(myList)
# new = myList.copy()
# print(new)
# if new == myList:
#     print("yes copied")
# else:
#     print("not copied")
# # myList.clear()
# print(myList)

# list1 = [10,20,30,40,50]
# list2 = [60,70,80,90,10]
# list3 = [11,12,13,14,15]

# new_list = list1+list2+list3

# print(new_list)
# print(new_list.count(10))

# x = list1.index(40)
# print(x)

#-=-=-=-=-tupplepractice-=-=-=-=-
# tup = (1,"abcd",3.14,False)
# print(type(tup))
# print(tup)
# tup[0]=2   #this will give an error because tuples are immutable

# def  create_tuple():
#     tup = ()
#     for i in range(2):
#         item = input("enter any thing which you want in your tuple:")
#         tup += (item,)
#     return tup

# print(create_tuple())
# print(type(create_tuple()))

# my_integers = (1, 2, 5, 7, 9, 2, 3, 7, 11)


# def count_items(my_integers, item):
#     return my_integers.count(item)


# print("Counting how many times item 7 exist in tuple ",
#       my_integers, " -> ", count_items(my_integers, 7))
# print("")

# def create_set_from_input():
#     # Get input from the user
#     user_input = input("Enter elements separated by spaces: ")
    
#     # Split the input into a list of elements
#     elements = user_input.split()
    
#     # Create a set from the list of elements
#     user_set = set(elements)
    
#     return user_set

# # Example usage
# new_set = create_set_from_input()
# print("New set:", new_set)

#-=-=-=-=-=-25-March-2024-=-=-=-=-=-
#--try_exception practice
# a = input("Enter any number:")
# b = input("Enter another number:")
# def try_except():
#     try:
#         c=int(a)+int(b)
#     except Exception  as e:
#         print("Error occurred:",e)
#         print("One or both inputs are not numbers" + "\nPlease enter numeric values.")
#     else:
#         print("The sum is:",c)
#     finally:
#         print("This block runs irrespective of an exception being raised or not.")
# try_except()
# print("end of code")
# try:
#     c=int(a)+int(b)
# except ValueError:
#     print("You didn't enter numbers!")
# else:   
#     print("The sum is:",c) 
# finally:
#     print("End.")

# x = -1
# if x < 0:
#     raise  Exception("Input must be positive")

# x = "hello"
# if not type(x) is int:
#     raise  TypeError("Input must be integer")

# sum = 0
# lst = [1,4,6,8,9]
# for i in lst:
#     sum =  sum+i
    
# print(sum)

# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     elif age < 18:
#         raise ValueError("You must be 18 or older.")

# # check_age(int(input("Enter your age:")))
# try:
#     check_age(-5)
# except ValueError as e:
#     print(f"Error: {e}")
    
# class CustomError(Exception):
#     def __init__(self, message):
#      self.message = message

# try:
#     raise CustomError("Custom exception message")
# except CustomError as e:
#     print(f"Custom error occurred: {e.message}")
    
# try:
#     file = open("nonexistent_file.txt")
# except FileNotFoundError:
#     print("Error: File not found!")
# except Exception as e:
#     print(f"An error occurred: {e}")

# def pass_by_value(x):
#     return x*2
# def pass_by_reference(lst):
#     lst[0]=37

# num=5
# print(f"Before calling function with value: {num} ")
# print(pass_by_value(num))
# print(f"\nAfter calling function with value: {num}\n")
# print(num)

# mylist=[9]
# print(f"Before calling function with reference: {mylist[0]}")
# pass_by_reference(mylist)
# print(f"After calling function with reference: {mylist[0]}\n")
# print(mylist)


# def function1(a):
#     def  nested_function(b):
#         return a*b
#     return nested_function
# result=function1(5)(6)
# print(f"Result from nested function: {result}")

# lst = []
# for i in range(5):
#     element = input("enter 5 element:")
#     lst.append(element)
# print(lst)
# def find_element(list,index):
#     return list.index(index)
# index = int(input("enter any number:"))
# try:
#     if index == len(lst):
#         find_element(lst,index)
#     else:
#         raise IndexError
# except IndexError:
#     print("Index out of range")
# def double_number(x):
#     return x * 2
# if __name__=="__main__":
#     numbers = [4, 8, 7, 3, 1]
#     print(numbers)
#     print(double_number(numbers))
#     print(numbers)
#     numbers = double_number(numbers)
#     print(numbers)
#     new_numbers = map(double_number, numbers)
#     print(new_numbers)
#     for num in new_numbers:
#         print(num)
#     print(type(new_numbers))
# import tkinter as tk

# root = tk.Tk()
# label = tk.Label(root, text="Hello, Tkinter!")
# label.pack()
# root.mainloop()
# import tkinter as tk

# # Create a Tkinter window
# window = tk.Tk()
# window.title("Hello Tkinter")
# label = tk.Label(window, text="Hello, Tkinter!")
# label.pack()

# # Run the Tkinter event loop
# window.mainloop()
# import tkinter as tk

# def button_clicked():
#     print("Button clicked!")
# def quit_window():
#     window.destroy()

# # Create the main window
# window = tk.Tk()
# window.title("Simple GUI")

# # Create a label
# label = tk.Label(window, text="Hello, Tkinter!")
# label.pack()

# listbox = tk.Listbox(window)
# listbox.pack()

# # Add items to the Listbox
# items = ["Item 1", "Item 2", "Item 3", "Item 4"]
# for item in items:
#     listbox.insert(tk.END, item)

# # Create a button
# button = tk.Button(window, text="Click Me", command=button_clicked)
# button.pack()

# quit_button = tk.Button(window, text="Quit", command=quit_window)
# quit_button.pack()

# # Run the main loop
# window.mainloop()



## budget management project
# import datetime
# import speech_recognition as sr # type: ignore

# # Initialize the speech recognizer
# recognizer = sr.Recognizer()

# # Function to recognize speech and convert it to text
# def recognize_speech():
#     with sr.Microphone() as source:
#         print("Speak now...")
#         audio = recognizer.listen(source)

#     try:
#         text = recognizer.recognize_google(audio)
#         return text
#     except sr.UnknownValueError:
#         print("Sorry, could not understand the audio.")
#     except sr.RequestError:
#         print("Speech recognition service unavailable.")

# # Function to add a new task
# def add_task(tasks):
#     print("Please speak the task details.")
#     task_name = recognize_speech()
#     description = recognize_speech()
#     due_date = recognize_speech()
#     priority = recognize_speech()
#     status = "Pending"
#     tasks.append({
#         'task_name': task_name,
#         'description': description,
#         'due_date': due_date,
#         'priority': priority,
#         'status': status
#     })
#     print("Task added successfully!")

# # Function to view all tasks
# def view_tasks(tasks):
#     if not tasks:
#         print("No tasks found.")
#     else:
#         for index, task in enumerate(tasks, start=1):
#             print(f"Task {index}:")
#             print(f"Name: {task['task_name']}")
#             print(f"Description: {task['description']}")
#             print(f"Due Date: {task['due_date']}")
#             print(f"Priority: {task['priority']}")
#             print(f"Status: {task['status']}")
#             print("-" * 20)

# # Function to set a reminder for upcoming tasks
# def set_reminder(tasks):
#     today = datetime.date.today()
#     upcoming_tasks = [task for task in tasks if datetime.datetime.strptime(task['due_date'], "%Y-%m-%d").date() > today]
#     if not upcoming_tasks:
#         print("No upcoming tasks found.")
#     else:
#         print("Upcoming Tasks:")
#         for task in upcoming_tasks:
#             print(f"Task: {task['task_name']}")
#             print(f"Due Date: {task['due_date']}")
#             print("-" * 20)
#         print("Reminder set successfully!")

# # Main function
# def main():
#     tasks = []
#     while True:
#         print("\nTask Manager Menu:")
#         print("1. Add Task")
#         print("2. View Tasks")
#         print("3. Set Reminder")
#         print("4. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             add_task(tasks)
#         elif choice == '2':
#             view_tasks(tasks)
#         elif choice == '3':
#             set_reminder(tasks)
#         elif choice == '4':
#             print("Exiting Task Manager.")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

# import speech_recognition as sr
# # recognizer = sr.Recognizer()
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for Microphone(device_index={0})".format(index, name))


## Finance tracking system
# import json
# from datetime import datetime

# class FinanceTracker:
#     def __init__(self):
#         self.income = 0
#         self.expenses = []
#         self.budgets = {}
#         self.investments = []

#     def add_income(self, amount):
#         self.income += amount

#     def add_expense(self, category, amount, description):
#         self.expenses.append({
#             'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             'category': category,
#             'amount': amount,
#             'description': description
#         })

#     def set_budget(self, category, limit):
#         self.budgets[category] = limit

#     def add_investment(self, asset, amount, type):
#         self.investments.append({
#             'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             'asset': asset,
#             'amount': amount,
#             'type': type  # 'stock' or 'cryptocurrency'
#         })

#     def save_data(self, filename='finance_data.json'):
#         data = {
#             'income': self.income,
#             'expenses': self.expenses,
#             'budgets': self.budgets,
#             'investments': self.investments
#         }
#         with open(filename, 'w') as file:
#             json.dump(data, file)

#     def load_data(self, filename='finance_data.json'):
#         with open(filename, 'r') as file:
#             data = json.load(file)
#             self.income = data['income']
#             self.expenses = data['expenses']
#             self.budgets = data['budgets']
#             self.investments = data['investments']

# # Usage example:
# tracker = FinanceTracker()
# tracker.add_income(5000)
# tracker.add_expense('Groceries', 200, 'Weekly grocery shopping')
# tracker.set_budget('Groceries', 300)
# tracker.add_investment('AAPL', 1000, 'stock')
# tracker.save_data()


# 2nd type
# import json
# from datetime import datetime

# class FinanceTracker:
#     def __init__(self):
#         self.income = 0
#         self.expenses = []
#         self.budgets = {}
#         self.investments = []

#     def add_income(self, amount):
#         self.income += amount

#     def add_expense(self, category, amount, description):
#         self.expenses.append({
#             'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             'category': category,
#             'amount': amount,
#             'description': description
#         })

#     def set_budget(self, category, limit):
#         self.budgets[category] = limit

#     def add_investment(self, asset, amount, type):
#         self.investments.append({
#             'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             'asset': asset,
#             'amount': amount,
#             'type': type  # 'stock' or 'cryptocurrency'
#         })

#     def save_data(self, filename='finance_data.json'):
#         data = {
#             'income': self.income,
#             'expenses': self.expenses,
#             'budgets': self.budgets,
#             'investments': self.investments
#         }
#         with open(filename, 'w') as file:
#             json.dump(data, file)

#     def load_data(self, filename='finance_data.json'):
#         with open(filename, 'r') as file:
#             data = json.load(file)
#             self.income = data['income']
#             self.expenses = data['expenses']
#             self.budgets = data['budgets']
#             self.investments = data['investments']

# # Function to display menu and get user input
# def display_menu():
#     print("===== Finance Tracker Menu =====")
#     print("1. Add Income")
#     print("2. Add Expense")
#     print("3. Set Budget")
#     print("4. Add Investment")
#     print("5. Save Data")
#     print("6. View Summary")
#     print("7. Exit")
#     choice = input("Enter your choice: ")
#     return choice

# # Usage example with user input and error handling
# tracker = FinanceTracker()
# while True:
#     choice = display_menu()
#     if choice == '1':
#         try:
#             amount = float(input("Enter income amount: "))
#             tracker.add_income(amount)
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#     elif choice == '2':
#         category = input("Enter expense category: ")
#         try:
#             amount = float(input("Enter expense amount: "))
#             description = input("Enter expense description: ")
#             tracker.add_expense(category, amount, description)
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#     elif choice == '3':
#         category = input("Enter budget category: ")
#         try:
#             limit = float(input("Enter budget limit: "))
#             tracker.set_budget(category, limit)
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#     elif choice == '4':
#         asset = input("Enter asset name: ")
#         try:
#             amount = float(input("Enter investment amount: "))
#             investment_type = input("Enter investment type (stock/cryptocurrency): ")
#             tracker.add_investment(asset, amount, investment_type)
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")
#     elif choice == '5':
#         tracker.save_data()
#         print("Data saved successfully!")
#     elif choice == '6':
#         print("===== Financial Summary =====")
#         print(f"Income: ${tracker.income}")
#         print("Expenses:")
#         for expense in tracker.expenses:
#             print(f"- {expense['category']}: ${expense['amount']} ({expense['description']})")
#         print("Budgets:")
#         for category, limit in tracker.budgets.items():
#             print(f"- {category}: ${limit}")
#         print("Investments:")
#         for investment in tracker.investments:
#             print(f"- {investment['asset']}: ${investment['amount']} ({investment['type']})")
#     elif choice == '7':
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Please try again.")
import speech_recognition as sr


def record_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        # Adjusting for ambient noise for 0.5 seconds
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Start Speaking: ")
        try:
            # Listen for audio with a timeout of 5 seconds
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            print("Timeout occurred while waiting for audio input")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
    return None


def output_text(text):
    if text:
        with open('text.txt', 'a') as f:
            f.write(text + '\n')
        print("Text written successfully")


def main():
    while True:
        text = record_text()
        if text and text.lower() == "stop":
            print("Stopping...")
            break
        output_text(text)


if _name_ == "_main_":
    main()