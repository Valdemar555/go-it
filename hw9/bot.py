contact_book = {
    "Valera": "648546",
    "Olga": "124560",
    "Anna":"346765"
    }

def menu():  
        print ('\nPlease select from the following command:\n')  
        print('add... Add new contact. Enter name and phone number, separated by a space')  
        print('phone... Display you contact. Enter name contact')  
        print('change... Сhange an existing contact. Enter name and phone number, separated by a space')  
        print('show all. View existing contacts')
        print('hello. Greetings')
        print('exit. Exit the program\n')



def parser(user_input:str):
    if user_input.lower().startswith("add"):
        command = add_func
        data = user_input.split()[1:]
        return command, data
    elif user_input.lower().startswith("phone"):
        command = phone_func
        data = user_input.split()[1]
        return command, data
    elif user_input.lower().startswith("change"):
        command = change_func
        data = user_input.split()[1:]
        return command, data
    elif user_input.lower().startswith("show all"):
        command = show_func
        data = []
        return command, data   
    elif user_input.lower().startswith("close"):
        command = close_func
        data = "exit"
        return command, data
    elif user_input.lower().startswith("hello"):
        command = hello_func
        data = []
        return command, data   
        
    else:
        command = unknown
        data = []
        return command, data

def error_handler(func):
    def wrapper(*args):
        try:
            return func(*args)
        except ValueError as e:
            print(e)
        
    return wrapper

@error_handler
def add_func(*args):
    name, phone = args[0]
    contact_book[name] = phone
    print("Contact add successfully.")

def show_func(*args):
    print(contact_book)

def change_func(*args):
    name, phone = args[0]
    contact_book[name] = phone
    print("Contact add successfully.")

def phone_func(*args):
    name = str(args[0])
    print(contact_book.get(name))

def hello_func(*args):
    print ("How can I help you?")

def close_func(*args):
    print("Good bye!") 

def unknown(*args):
    print("Unknown command, please try again")

def main():
    
    menu()
    
    while True:
        user_command = input("Please, give me a command:")
        command, data = parser(user_command)
        if data in ["god bye","close","exit"]:
            close_func()
            break
        command(data)
        
if __name__ == "__main__":
    main()